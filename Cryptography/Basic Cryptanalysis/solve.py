
import math

__all__ = ['get_jaro_distance']
__author__ = 'Jean-Bernard Ratte - jean.bernard.ratte@unary.ca'


def get_jaro_distance(first, second, winkler=True, winkler_ajustment=True, scaling=0.1):
    """
    :param first: word to calculate distance for
    :param second: word to calculate distance with
    :param winkler: same as winkler_ajustment
    :param winkler_ajustment: add an adjustment factor to the Jaro of the distance
    :param scaling: scaling factor for the Winkler adjustment
    :return: Jaro distance adjusted (or not)
    """
    if not first or not second:
        raise JaroDistanceException("Cannot calculate distance from NoneType ({0}, {1})".format(
            first.__class__.__name__,
            second.__class__.__name__))

    jaro = _score(first, second)
    cl = min(len(_get_prefix(first, second)), 4)

    if all([winkler, winkler_ajustment]):  # 0.1 as scaling factor
        return round((jaro + (scaling * cl * (1.0 - jaro))) * 100.0) / 100.0

    return jaro


def _score(first, second):
    shorter, longer = first.lower(), second.lower()

    if len(first) > len(second):
        longer, shorter = shorter, longer

    m1 = _get_matching_characters(shorter, longer)
    m2 = _get_matching_characters(longer, shorter)

    if len(m1) == 0 or len(m2) == 0:
        return 0.0

    return (float(len(m1)) / len(shorter) +
            float(len(m2)) / len(longer) +
            float(len(m1) - _transpositions(m1, m2)) / len(m1)) / 3.0


def _get_diff_index(first, second):
    if first == second:
        return -1

    if not first or not second:
        return 0

    max_len = min(len(first), len(second))
    for i in range(0, max_len):
        if not first[i] == second[i]:
            return i

    return max_len


def _get_prefix(first, second):
    if not first or not second:
        return ""

    index = _get_diff_index(first, second)
    if index == -1:
        return first

    elif index == 0:
        return ""

    else:
        return first[0:index]


def _get_matching_characters(first, second):
    common = []
    limit = math.floor(min(len(first), len(second)) / 2)

    for i, l in enumerate(first):
        left, right = int(max(0, i - limit)), int(min(i + limit + 1, len(second)))
        if l in second[left:right]:
            common.append(l)
            second = second[0:second.index(l)] + '*' + second[second.index(l) + 1:]

    return ''.join(common)


def _transpositions(first, second):
    return math.floor(len([(f, s) for f, s in zip(first, second) if not f == s]) / 2.0)


class JaroDistanceException(Exception):
    def __init__(self, message):
            super(Exception, self).__init__(message)


# Implementation
def patternize(word):
    lookup = {}
    i = 1
    out = []
    for char in word:
        if char not in lookup:
            lookup[char] = i
            i += 1
        out.append(str(lookup[char]))

    return ''.join(out)


# 1. Read dictionary and input
wordlist = {}
with open('dictionary.lst') as f:
    lines = f.readlines()
    for line in lines:
        word = line.strip().lower()
        pattern_word = patternize(word)
        if pattern_word in wordlist:
            wordlist[pattern_word].append(word)
        else:
            wordlist[pattern_word] = [word]

phrase = input()
words = phrase.split(' ')

# 2. Pattern match on given wordlist to build a lookup table
matched_words = {}
for word in words:
    pattern_word = patternize(word)
    if pattern_word in wordlist:
        if pattern_word in matched_words:
            matched_words[pattern_word].append(word)
        else:
            matched_words[pattern_word] = [word]

# 3. Build translation table based on word patterns.
# Start with 1:1 words mapping to build a basic monoalphabetic substitution
translation_table = {}
for pattern, matches in matched_words.items():
    if len(matches) == 1 and len(wordlist[pattern]) == 1:
        # print(pattern, matches[0], wordlist[pattern])
        encoded = matches[0]
        decoded = wordlist[pattern][0]
        # print(encoded, decoded)
        for i in range(len(encoded)):
            translation_table[ord(encoded[i])] = ord(decoded[i])

# 3. Refine the built alphabet mapping based on unmatching words
# with Jaro Wrinkler similarity to choose the correct word translation
for pattern, matches in matched_words.items():
    if len(matches) == 1:
        encoded = matches[0]
        encoded.translate(translation_table)
        decoded = encoded.translate(translation_table)
        if decoded not in wordlist[pattern]:
            max_similarity = 0
            best_candidate = decoded
            for candidate in wordlist[pattern]:
                similarity = get_jaro_distance(decoded, candidate)
                if similarity > max_similarity:
                    max_similarity = similarity
                    best_candidate = candidate

            for i in range(len(encoded)):
                translation_table[ord(encoded[i])] = ord(best_candidate[i])

print(phrase.translate(translation_table))

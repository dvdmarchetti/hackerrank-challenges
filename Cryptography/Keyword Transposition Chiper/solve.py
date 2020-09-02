def split(word):
    return [char for char in word]


def argsort(sequence):
    return sorted(range(len(sequence)), key=sequence.__getitem__)


def build_key_matrix(key):
    key = ''.join(dict.fromkeys(key))

    m = [
        split(key)
    ]

    char = ord('A')
    end = ord('Z')
    cols = len(key)
    rows = int((26 - cols) / cols) + 1
    for r in range(rows):
        row = []

        for c in range(cols):
            while chr(char) in key:
                char += 1

            if char <= end:
                row.append(chr(char))
                char += 1
            else:
                row.append(None)

        m.append(row)

    return ((rows, cols), m)

def substitution_matrix(key):
    (rows, cols), p_matrix = build_key_matrix(key)
    rows += 1

    out = []
    ordered_columns = argsort([p_matrix[0][i] for i in range(cols)])
    for col in ordered_columns:
        [out.append(p_matrix[row][col]) for row in range(rows) if p_matrix[row][col] is not None]

    return out


def decode(chipertext, permutation):
    # 0x41 = ord('A')
    return ''.join([chr(0x41 + permutation.index(char)) if char != ' ' else char for char in chipertext])


N = int(input())
for i in range(N):
    key, ciphertext = input(), input()
    substitution = substitution_matrix(key)
    plaintext = decode(ciphertext, substitution)
    print(plaintext)

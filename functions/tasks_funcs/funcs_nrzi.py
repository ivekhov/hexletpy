def decode(row):
    if not row:
        return ''
    curr = 0
    prev = 0
    def invert(x):
        if x == 0:
            return 1
        return 0

    # work
    result = []
    for symb in list(row):
        if symb == '|':
            curr = invert(curr)
        if prev == 1:
            curr = invert(curr)
        else:
            result.append(str(curr))
        prev = curr

    return ''.join(result)

# print()
# row = '_|¯|____|¯|__|¯¯¯'
# resp = '011000110100'
# print(row)
# print(decode(row))  # 010000100111  wrong
# print(resp)         # 011000110100  correct


def test_decode():
    assert decode('') == ''
    assert decode('|¯') == '1'
    assert decode('_') == '0'
    assert decode('_|¯|____|¯|__|¯¯¯') == '011000110100'
    assert decode('|¯|___|¯¯¯¯¯|___|¯|_|¯') == '110010000100111'
    assert decode('¯|___|¯¯¯¯¯|___|¯|_|¯') == '010010000100111'


if __name__ == '__main__':
    test_decode()
    pass
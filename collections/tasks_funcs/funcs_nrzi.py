def decode(row):
    return row

row = '¯|___|¯¯¯¯¯|___|¯|_|¯'
print(decode(row))


def test_decode():
    assert decode('') == ''
    assert decode('|¯') == '1'
    assert decode('_') == '0'
    assert decode('_|¯|____|¯|__|¯¯¯') == '011000110100'
    assert decode('|¯|___|¯¯¯¯¯|___|¯|_|¯') == '110010000100111'
    assert decode('¯|___|¯¯¯¯¯|___|¯|_|¯') == '010010000100111'


if __name__ == '__main__':
#     test_decode()
    pass
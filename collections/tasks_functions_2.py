def rgb2hex(r, g, b, *args):
    # 1 arguments : positional and named -- Done
    
    # 2 translation colors 
    def f(row):
        new_row = hex(row)[0] + hex(row)[2:]
        return new_row[-2::]
    
    result = list(map(f, [r, g, b]))
    return '#{}'.format(''.join(result))


def test_compose():
    assert rgb2hex(0, 0, 0) == '#000000'
    assert rgb2hex(255, 255, 255) == '#ffffff'
    assert rgb2hex(0, 132, 12) == '#00840c'
    assert rgb2hex(36, 171, 0) == '#24ab00'
    assert rgb2hex(r=84, g=63, b=171) == '#543fab'
    assert rgb2hex(r=247, b=222, g=0) == '#f700de'
    assert rgb2hex(r=198, g=1, b=35) == '#c60123'


def ip2int(ip):
    ip_list = ip.split('.')
    ip_items = list(map(int, ip_list))

    def int2bin(num):
        temp = bin(num)
        short = temp[2:]
        while len(short) < 8:
            short = '0' + short
        return short

    temp = list(map(int2bin, ip_items))
    return int(''.join(temp), 2)


def int2ip(num):
    temp_bin = bin(num)[2:]
    arr = []
    chunk = 8
    start = 0
    for i in range(1, 5):
        if temp_bin[start:chunk * i]:
            arr.append(str(temp_bin[start: chunk * i]))
            start += chunk

    while len(arr) < 4:
        arr.append('0')

    temp = list(map(lambda x: int(x, 2), arr)) 
    return '.'.join(list(map(str, temp)))

ZEROES = '0.0.0.0'  # noqa: S104


def test_ip2int():
    assert ip2int(ZEROES) == 0
    assert ip2int('128.32.10.1') == 2149583361


def test_int2ip():
    assert int2ip(0) == ZEROES
    assert int2ip(2149583361) == '128.32.10.1'


def test_round_robin():
    assert int2ip(ip2int('192.168.1.32')) == '192.168.1.32'
    assert ip2int(int2ip(2149583361)) == 2149583361


if __name__ == '__main__':
    test_ip2int()
    test_int2ip()
    test_round_robin()
    # test_compose()
    pass

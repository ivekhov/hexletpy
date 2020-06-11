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


def find_index_of_nearest(num, source):
    if not source:
        return None
    d = list(map(lambda x: abs(x - num), source))
    ix_list = list(range(len(source)))
    result_d = [k for k, v in zip(ix_list, source) if abs(v - num) == min(d)]
    return result_d[0]


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


from collections import Counter


def histo(source, min_value=None, max_value=None, bar_char='#'):
    min_value=min(source)
    max_value=max(source)    
    print(source, min_value, max_value, bar_char)


source = [1, 2, 3, 4, 5]
histo(source, min_value=42)


BIG_SAMPLE = (  # noqa: WPS317
    30, 15, 21, 19, 15, 25, 17, 27, 16, 16,
    21, 17, 24, 16, 16, 18, 20, 25, 28, 26,
    21, 21, 20, 26, 28, 27, 16, 26, 22, 15,
    20, 30, 21, 21, 19, 18, 30, 22, 24, 24,
    19, 23, 27, 15, 24, 25, 21, 16, 21, 24,
    21, 29, 27, 19, 19, 25, 26, 27, 27, 22,
    16, 23, 24, 15, 24, 23, 22, 20, 22, 17,
    21, 29, 16, 27, 18, 19, 28, 17, 18, 21,
    30, 26, 28, 22, 29, 30, 28, 30, 17, 26,
    18, 17, 17, 26, 21, 27, 20, 29, 29, 30,
)

SMALL_SAMPLE = (  # noqa: WPS317
    21, 23, 23, 25, 24, 21, 25, 24, 22, 21,
)


def test_histo():

    assert histo([], min_value=10, max_value=15) == """
10|
11|
12|
13|
14|
15|
""".strip()

    assert histo([3, 3, 5, 6, 6], min_value=1, bar_char='%') == """
1|
2|
3|%% 2
4|
5|% 1
6|%% 2
""".strip()

    assert histo(BIG_SAMPLE) == """
15|##### 5
16|######## 8
17|####### 7
18|##### 5
19|###### 6
20|##### 5
21|############ 12
22|###### 6
23|### 3
24|####### 7
25|#### 4
26|####### 7
27|######## 8
28|##### 5
29|##### 5
30|####### 7
""".strip()

    assert histo(SMALL_SAMPLE, min_value=22, max_value=27) == """
22|# 1
23|## 2
24|## 2
25|## 2
26|
27|
""".strip()



if __name__ == '__main__':
    # test_histo()
    # test_ip2int()
    # test_int2ip()
    # test_round_robin()
    # test_compose()
    pass

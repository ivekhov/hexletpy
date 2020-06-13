from collections import Counter


def histo(samples, min_value=None, max_value=None, bar_char='#'):
    loc_cnt = Counter(samples)
    result = ''
    if not min_value:
        min_value = min(loc_cnt.keys())
    if not max_value:
        max_value = max(loc_cnt.keys())

    def exclude_zero(x):
        if x == 0:
            return ''
        return ' ' + str(x)
    for num in range(min_value, max_value + 1):
        # if i need a print
        # print("{}|{} {}".format(num, bar_char * loc_cnt[num], exclude_zero(loc_cnt[num])))
        result += (str(num) + '|' + (bar_char * loc_cnt[num]) + 
            exclude_zero(loc_cnt[num]) + "\n")

    return result[:-1]


# res = histo([], min_value=10, max_value=15)
# print(res.strip())


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
    test_histo()
    pass


'''
example solution:
...
    axis = range(min_value, max_value + 1)
    counts = Counter(samples)
    
    lines = map(
        lambda value, count: '{}|{}{}'.format(
            value,
            bar_char * count,
            ' ' + str(count) if count else '',
        ),
        axis,
        map(lambda key: counts[key], axis),
    )

    return '\n'.join(lines)
...


'''

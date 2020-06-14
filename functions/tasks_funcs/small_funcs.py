from math import sqrt


'''
Реализуйте функцию filter_map, которая ведёт себя подобно filter и map, 
работающим вместе. 
filter_map должна принимать в качестве аргументов функцию и итерируемый источни
к, а возвращать должна список.

В теле filter_map к каждому значению из источника нужно применять функцию, 
которая в ответ будет возвращать пару:

Булево значение,
Некий результат.
Если булево значение (1) истинно, то результат (2) должен попадать в 
результирующий список. В противном случае второе значение пары игнорируется.

Пример использования:

# >>> def make_stars(x):
# ...     if x > 0:
# ...         return True, '*' * x
# ...     return False, ''
# ...
# >>> for s in filter_map(make_stars, [1, 0, 5, -5, 2]):
# ...     print(s)

better solution inside for cycle 
...
        keep, value = function(item)
        if keep:
            result.append(value)
...
'''


def filter_map(some_func, iterable):
    result = []
    for item in iterable:
        if some_func(item)[0] is True:
            result.append(some_func(item)[1])
    return result


def make_stars(x):
    if x > 0:
        return True, '*' * x
    return False, ''


for s in filter_map(make_stars, [1, 0, 5, -5, 2]):
    print(s)


def test_filter_map():
    def safe_sqrt(x):
        if x < 0:
            return False, 0
        return True, sqrt(x)

    assert filter_map(safe_sqrt, []) == []
    assert filter_map(safe_sqrt, [4, -5, -2, 9]) == [2.0, 3.0]  # noqa: WPS221



if __name__ == '__main__':
    test_filter_map()    
    pass
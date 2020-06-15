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


# for s in filter_map(make_stars, [1, 0, 5, -5, 2]):
#     print(s)


def test_filter_map():
    def safe_sqrt(x):
        if x < 0:
            return False, 0
        return True, sqrt(x)

    assert filter_map(safe_sqrt, []) == []
    assert filter_map(safe_sqrt, [4, -5, -2, 9]) == [2.0, 3.0]  # noqa: WPS221
###############################################################################


from operator import add, mul

'''
partial_apply
partial_apply принимает функцию от двух аргументов и первый аргумент,
 а возвращает замыкание — функцию, которая примет второй аргумент и 
 наконец применит замкнутую функцию к обоим аргументам (и вернёт результат).

Пример использования:

# >>> def greet(name, surname):
# ...     return 'Hello, {name} {surname}!'.format(name=name, surname=surname)
# ...
# >>> f = partial_apply(greet, 'Dorian')
# >>> f('Grey')
# 'Hello, Dorian Grey!'
# >>>



flip
Функция flip принимает в качестве единственного аргумента функцию от 
двух аргументов. Возвращаемое замыкание должно также принять 
два аргумента, а затем применить к ним замкнутую функцию, 
но аргументы подставить в обратном порядке.
 Таким образом flip как бы "переворачивает" ("flips") исходную функцию.

Пример использования:

# >>> def greet(name, surname):
# ...     return 'Hello, {name} {surname}!'.format(name=name, surname=surname)
# ...
# >>> f = flip(greet)
# >>> f('Christian', 'Teodor')
# 'Hello, Teodor Christian!'
'''


def partial_apply(some_func, first_arg):
    def closure(second_arg):
        return some_func(first_arg, second_arg)
    return closure


def greet(name, surname):
    return 'Hello, {name} {surname}!'.format(name=name, surname=surname)


def test_partial_apply():
    assert list(
        map(partial_apply(add, 10), [1, 2, 3]),  # noqa: WPS221
    ) == [11, 12, 13]

    assert list(
        map(partial_apply(mul, '*'), [2, 3, 4]),  # noqa: WPS221
    ) == [
        '**',
        '***',
        '****',
    ]


def flip(some_func):
    def closure(first_arg, second_arg):
        return some_func(second_arg, first_arg)
    return closure


def test_flip():
    assert flip(mul)(3, '*') == '***'


def test_both():
    assert list(
        map(partial_apply(flip(mul), 5), "!?&"),
    ) == [
        '!!!!!',
        '?????',
        '&&&&&',
    ]
###############################################################################

from functools import reduce
from operator import truth
from operator import add
from operator import getitem


def keep_truthful(source):
    try:
        return list(filter(truth, source))
    except BaseException:
        return 'All falsy values sholud be filtered out!'


def abs_sum(source):
    return reduce(add, list(map(abs, source)))


def walk(idict, iiter):
    return reduce(getitem, iiter, idict)


# walk({'a': {7: {'b': 42}}}, ["a", 7, "b"])
# # 42

# idict = {'a': {7: {'b': 42}}}
# iiter =  ["a", 7, "b"]

# walk({'a': {7: {'b': 42}}}, ["a", 7])
# # {'b': 42}

FALSES = (False, (), None, '', 0)
TRUTHS = (True, (1,), '!', -5)


def test_keep_truthful():
    assert list(keep_truthful(FALSES)) == [], (
        'All falsy values sholud be filtered out!'
    )
    assert list(keep_truthful(TRUTHS)) == list(TRUTHS), (
        'All truthful values sholud be keeped!'
    )
    assert list(keep_truthful([0, 1, 0])) == [1]


def test_abs_sum():
    assert abs_sum([0]) == 0
    assert abs_sum((-42,)) == 42
    assert abs_sum([-3, -2, -1, 0, 1, 2, 3]) == 12  # noqa: WPS221


def test_walk():
    city = {
        'Pine': {
            '5': 'School #42',
        },
        'Elm': {
            '13': {
                '1': 'Appartments #2, Elm st.13',
            },
        },
    }
    assert walk(city, ['Pine', '5']) == city['Pine']['5']
    path = ['Elm', '13', '1']
    assert walk(city, path) == city['Elm']['13']['1']


if __name__ == '__main__':
    test_keep_truthful()
    test_abs_sum()
    test_walk()
    # test_partial_apply()
    # test_flip()
    # test_both()
#     test_filter_map()
    print("Tests passed")
    pass
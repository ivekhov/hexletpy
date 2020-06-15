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
    return list(filter(truth, source))
    # try:
    #     return list(filter(truth, source))
    # except BaseException:
    #     return 'All falsy values sholud be filtered out!'


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
keep_truthful(FALSES)

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
###############################################################################


'''
Реализуйте функцию make_module так, чтобы она

принимала аргумент step со значением по умолчанию равным 1,
возвращала словарь с ключами "inc" (от "увеличить"/"increment") и "dec" (от
 "уменьшить"/"decrement"), по которым можно было бы получить лямбды, одна из 
 которых добавляет, а вторая вычитает step из своего аргумента.
Тело функции make_module должно состоять из одного выражения — return {…}. То 
есть лямбда-функции должны быть объявлены прямо в литерале словаря!

Пример использования:
# >>> m = make_module()
# >>> m['inc'](10)
# 11
# >>> m['dec'](20)
# 19
# >>> m2 = make_module(step=2)
# >>> m2['inc'](1)
'''

def make_module(step=1):
    return {
        'inc': lambda x: x + step,
        'dec': lambda x: x - step,
    }


def test_make_module():
    assert make_module()['inc'].__name__ == '<lambda>', (
        'Increment function should be the lambda!'
    )
    assert make_module()['dec'].__name__ == '<lambda>', (
        'Decrement function should be the lambda!'
    )

    assert make_module()['inc'](0) == 1
    assert make_module()['dec'](5) == 4

    inc, dec = map(make_module(step=5).get, ['inc', 'dec'])
    assert inc(inc(inc(dec(0)))) == 10
###############################################################################


'''
Вам предстоит реализовать декоратор, добавляющий функции 
мемоизацию. Мемоизация 
— это запоминание уже вычисленных результатов, для уже 
однажды встреченных 
аргументов.

Для простоты будем считать, что мемоизироваться будут 
численные функции одного 
аргумента (аргумент — число, результат — тоже число).

Примеры
>>> from solution import memoized
>>> @memoized
... def f(x):
...     print('Calculating...')
...     return x * 10
...
>>> f(1)
Calculating...
10
>>> f(1)
10
>>> f(42)
Calculating...
420
>>> f(42)
420
>>>
Заметьте, что для каждого нового аргумента выводится 
сообщение "Calculating...", но только лишь один раз.
'''


def memoized(ifunc):
    def inner(iarg):
        if result.get(str(iarg)):
            return result.get(str(iarg))
        print("Calculating...")
        iresult = ifunc(iarg)
        result[str(iarg)] = iresult
        return iresult
    result = {}
    return inner


def test_memoized():
    counter = [0]

    @memoized
    def xor(byte):
        counter[0] += 1
        return 255 ^ byte

    assert xor(xor(42)) == 42
    assert counter == [2], "At this moment xor should be called twice"

    assert xor(42) + xor(xor(42)) == 255
    assert counter == [2], "No extra xor calls should be happened"

    assert xor(127) == 128
    assert xor(128) == 127
    assert counter == [4], "Total number of calls should be four"


def test_memoized_independency():
    @memoized
    def double(x):
        return x * 2

    @memoized
    def triple(x):
        return x * 3

    argument = 42
    first_result = double(argument)
    second_result = triple(argument)
    assert argument * 3 != first_result, (
        "First function should not provide result for the second one"
    )
    assert double(argument) != second_result, (
        "Second function should not affect memory of first function"
    )
###############################################################################

'''
В этот раз вы снова будете реализовывать мемоизирующий 
декоратор "memoizing". Но на этот раз декоратор должен 
принимать аргумент, задающий максимальное количество 
запоминаемых значений. При превышении количества 
запомненных значений лишние должны быть отброшены, причём 
сначала — самые старые!

Напоминаю, мемоизируемые функции считать численными 
функциями одного аргумента. И не забудьте про 
functools.wraps!
'''


from functools import wraps
from time import time
from time import sleep


def memoizing(imax):
    def wrapper(ifunc):
        result = {}
        @wraps(ifunc)
        def inner(iarg):
            if result.get(str(iarg)):
                return result.get(str(iarg))[0]
            print("Calculating...")
            iresult = ifunc(iarg)
            if len(result.keys()) >= imax:
                oldest_time = time()
                oldest_item = ''
                for k, v in result.items():
                    if v[1] < oldest_time:
                        oldest_time = v[1]
                        oldest_item = k
                print(result)
                print(oldest_item)
                result.pop(oldest_item)
            result[str(iarg)] = []
            result[str(iarg)].append(iresult)
            sleep(0.5)
            result[str(iarg)].append(time())
            return iresult
        return inner
    return wrapper


arguments = []
@memoizing(3)
def inc(argument):
    arguments.append(argument)
    return argument + 1


def test_memoizing():
    arguments = []
    @memoizing(3)
    def inc(argument):
        arguments.append(argument)
        return argument + 1

    assert inc(inc(inc(0))) == 3
    assert arguments == [0, 1, 2]

    _ = inc(inc(inc(0)))
    assert arguments == [0, 1, 2], "All resluts sholud be got from memory!"

    assert inc(10) == 11
    assert arguments == [0, 1, 2, 10], "New argument should be added!"

    assert inc(0) == 1
    assert arguments == [0, 1, 2, 10, 0], (
        "Result for zero should be recalculated!",
    )


def test_memoizing_wrapping():
    @memoizing(3)
    def foo():
        """Return bar."""

    assert foo.__name__ == "foo", (
        "Wrapper should preserve function's name!",
    )
    assert foo.__doc__ == "Return bar.", (
        "Wrapper should preserve function's docstring!",
    )



if __name__ == '__main__':
    test_memoizing()
    test_memoizing_wrapping()
    # test_memoized()
    # test_memoized_independency()
    # test_make_module()
    # test_keep_truthful()
    # test_abs_sum()
    # test_walk()
    # test_partial_apply()
    # test_flip()
    # test_both()
    # test_filter_map()
    print("Tests finished")


#################################

# def memoizing(imax):
#     def wrapper(ifunc):
#         result = {}
#         def inner(iarg):
#             if result.get(str(iarg)):
#                 return result.get(str(iarg))[0]
#             print("Calculating...")
#             iresult = ifunc(iarg)

#             if len(result.keys()) >= imax:
#                 oldest_time = time()
#                 oldest_item = ''
#                 for k, v in result.items():
#                     if v[1] < oldest_time:
#                         oldest_time = v[1]
#                         oldest_item = k
#                 result.pop(oldest_item)
#             result[str(iarg)] = []
#             result[str(iarg)].append(iresult)
#             result[str(iarg)].append(time())
            
#             #
#             print(result.keys(), len(result.keys()))
#             print(result)
#             #

#             return iresult
#         return inner
#     return wrapper
##############################


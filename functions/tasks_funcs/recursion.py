

'''
В упражнении вам нужно будет реализовать две взаимно рекурсивные функции (то есть использующие косвенную рекурсию):

is_odd должна возвращать True, если число нечётное,
is_even должна возвращать True, если число чётное.
Для простоты считаем, что аргументы всегда будут неотрицательными.

Вы, конечно, можете реализовать функции независимыми. Но задание призывает попробовать именно косвенную рекурсию!
# P@$$Temp_2020

'''

def is_even_s(num):
    if num == 0:
        return True
    if num == 1:
        return False
    return is_even(num % 2)


def is_odd_s(num):
    if num == 1:
        return True
    if num == 0:
        return False
    return is_odd(num % 2)

######## bad

def is_even(num):
    if num == 0:
        return True
    if is_odd(num - 1):
        return False
    return is_even(num % 2)


def is_odd(num):
    if num == 1:
        return True
    if is_even(num - 1):
        return False
    return is_odd(num % 2)

##############

def is_odd_x(number):
    return False if number == 0 else is_even(number - 1)


def is_even_x(number):
    return True if number == 0 else is_odd(number - 1)
#######################################################3


def test_is_odd():
    assert not is_odd(42)
    assert is_odd(99)


def test_is_even():
    assert not is_even(99)
    assert is_even(42)

if __name__ == '__main__':
    test_is_odd()
    test_is_even()
    print('Tests passed')
    



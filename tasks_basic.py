def is_vertical(coords):
    return (coords[0][0] == coords[1][0]) & (coords[0][1] != coords[1][1])


def is_horizontal(coords):
    return (coords[0][1] == coords[1][1]) & (coords[0][0] != coords[1][0])


def is_inclined(coords):
    return (coords[0][1] != coords[1][1]) & (coords[0][0] != coords[1][0])


def is_degenerated(coords):
    return (coords[0][0] == coords[1][0]) & (coords[0][1] == coords[1][1])

#### EXAMPLE SOLUTION




####

def rotate_left(triple):
    return (triple[1], triple[-1], triple[0])


def rotate_right(triple):
    return (triple[-1], triple[0], triple[1])


#### EXAMPLE SOLUTION

def rotate_left2(triple):
    elem1, elem2, elem3 = triple
    return (elem2, elem3, elem1)


def rotate_right2(triple):
    elem1, elem2, elem3 = triple
    return (elem3, elem1, elem2)

####

def test_triple():
    test = ('A', 'B', 'C')
    print(rotate_left(test))
    print(rotate_right(test))

####

# Напишите функцию diff, которая принимает два угла (int) со значениями в диапазоне от 0 до 360, и возвращает наименьшую
# разницу между ними.

def diff_00(a, b):

    def module(x):
        if x > 0:
            return x
        return -x

    if module(a - b) <= 180:
        return module(a - b)
    else:
        return 360 - module(a - b)


def diff(a, b):
    if abs(a - b) <= 180:
        return abs(a - b)
    elif abs(a - b) > 360:
        temp = abs(a - b) % 360
        if temp <= 180:
            return temp
        return 360 - temp
    return 360 - abs(a - b)

# Example solution
def diff_x(a1, a2):
    return min(
        (a1 - a2) % 360,
        (a2 - a1) % 360
    )
#

def diff_test():
    test = [
                (0, 45), (0, 180), (0, 190), (120, 180),
                (720, 0), (-720, 0), (730, 0), (930, 0),
                (60, 30), (125, 120), (300, 340), (200, 199),
                (90, 0), (-15, 15), (315, 45),
                (0, 0), (30, 270), (30, 240), (240, 30)
            ]
    for elem in test:
        print(diff(elem[0], elem[1]))


#
def is_power_of_three(num):
    if num == 1:
        return True
    temp = []
    for i in range(2, 100):
        temp.append(3 ** i)
    if num in temp:
        return True
    return False


def is_power_of_three_test():
    test = [
        1, 2, 9, 27, 81
    ]
    for elem in test:
        print(is_power_of_three(elem))


## FASAD TASK


import solution
from solution import numbers1, numbers2, numbers3

def test_names():
    assert hasattr(solution, 'add')  # noqa: WPS421
    assert hasattr(solution, 'mul')  # noqa: WPS421
    assert hasattr(solution, 'power')  # noqa: WPS421
    assert hasattr(solution, 'sqrt')  # noqa: WPS421
    assert hasattr(solution, 'sub')  # noqa: WPS421


def test_references():
    assert solution.add is numbers2.add2
    assert solution.mul is numbers1.mul1
    assert solution.power is numbers2.power2
    assert solution.sqrt is numbers3.sqrt3
    assert solution.sub is numbers2.sub2


def test_all_metavar():
    assert 'add' in solution.__all__  # noqa: WPS609
    assert 'mul' in solution.__all__  # noqa: WPS609
    assert 'power' in solution.__all__  # noqa: WPS609
    assert 'sqrt' in solution.__all__  # noqa: WPS609
    assert 'sub' in solution.__all__  # noqa: WPS609


if __name__ == "__main__":
    pass
    # test_names()
    # test_references()
    # test_all_metavar()
    # test_triple()
    # diff_test()
    # is_power_of_three_test()

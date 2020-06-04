def compose(f1, f2):
    # def inner(arg):
        # return f1(f2(arg))
    # return inner
    
    return lambda x: f1(f2(x))

def add5(x):
    return x + 5


def mul3(x):
    return x * 3


def test_compose():
    assert compose(mul3, add5)(1) == 18
    assert compose(add5, mul3)(1) == 8
    assert compose(mul3, str)(1) == '111'
    assert compose(str, mul3)(1) == '3'


if __name__ == "__main__":
    test_compose()
    print(compose(str, mul3)(2))
    pass
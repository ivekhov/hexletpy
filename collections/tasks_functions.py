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


from collections import Counter


def filter_anagrams(word, collection):
    result = []
    if word == '':
        for item in collection:
            if item == word:
                result.append(item)
        return result

    cnt = Counter(str(word))
    for item in collection:
        item_cnt = Counter(str(item))
        flag = True
        for k, v in cnt.items():
            if not item_cnt.get(k) or v > item_cnt[k]:
                flag = False
                break
        for key in item_cnt.keys():
            if not cnt.get(key) or item_cnt[key] > cnt[key]:
                flag = False
                break
        if flag:
            result.append(item)
    return result

# BEGIN
# def normalized(string):
    # return list(sorted(string))


# def filter_anagrams(word, words):
    # norm = normalized(word)
    # return filter(lambda item: normalized(item) == norm, words)
# END

from itertools import permutations


def test_filter_anagrams_with_strings():
    empty = ''
    assert list(filter_anagrams(empty, [empty, 'foo', empty])) == [empty, empty]

    assert list(filter_anagrams('laser', ['lazing', 'lazy', 'lacer'])) == []

    assert list(filter_anagrams(
        'abba', ['aabb', 'abcd', 'bbaa', 'dada'],
    )) == ['aabb', 'bbaa']

    assert list(filter_anagrams(
        'racer', ['crazer', 'carer', 'racar', 'caers', 'racer'],
    )) == ['carer', 'racer']


def test_filter_anagrams_with_tuples():
    assert list(filter_anagrams((), [(), ()])) == [(), ()]

    tri = (1, 2, 3)
    irt = tuple(reversed(tri))
    assert list(filter_anagrams(
        tri, [tri, irt, tri + (4,)],
    )) == [tri, irt]


def test_filter_anagrams_with_false_anagrams():
    assert list(filter_anagrams('bob', ['boo', 'bo', 'obbo'])) == []


def test_filter_anagrams_with_permutations():
    sample = tuple('abcd')
    sample_permutations = list(permutations(sample))
    # ^ [('a', 'b', 'c', 'd'), ('a', 'b', 'd', 'c'), ...
    # ...('d', 'c', 'a', 'b'), ('d', 'c', 'b', 'a')]
    assert len(list(filter_anagrams(
        sample, sample_permutations,
    ))) == len(sample_permutations)



def func2(num, source):
    return filter( min(list(map(lambda x: abs(x - num), source ))), source  )    

def f(x, num, source):
    return x ==  min(list(map(lambda x: abs(x - num), source )))


def find_index_of_nearest(num, source):
    # if not source:
        # return None
    
    # return filter( func2  , source)
    
    # delta al list with num
    delta = list(map(lambda x: abs(x - num), source ))
    min(delta)
    
    # filter 
    return filter( min(list(map(lambda x: abs(x - num), source ))), source  )
    
    # filter (f, collection)
    
    # f - object with minimal difference of x with elems in collection

source = [7, 5, 4, 4, 3, 6]
n = 4

# def f(x, num):
    # return x == num

# def f():
    

a = filter(f, source)
    
    
    
def test_find_index_of_solution():
    assert find_index_of_nearest(2, []) is None
    assert find_index_of_nearest(0, [10]) == 0
    assert find_index_of_nearest(0, [10, 15]) == 0
    assert find_index_of_nearest(1, [15, 10]) == 1
    assert find_index_of_nearest(12, [15, 10]) == 1
    assert find_index_of_nearest(0, [15, 10, 3, 4]) == 2
    assert find_index_of_nearest(4, [7, 5, 3, 2]) == 1
    assert find_index_of_nearest(4, [7, 5, 4, 4, 3, 6]) == 2


if __name__ == "__main__":
    test_find_index_of_solution()
    # test_filter_anagrams_with_strings()
    # test_filter_anagrams_with_permutations()
    # test_filter_anagrams_with_tuples()
    # test_filter_anagrams_with_false_anagrams()
    # test_compose()
    # print(compose(str, mul3)(2))
    pass

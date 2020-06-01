def to_rna(dna):
    rules = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }

    # result = ''
    # for nucleotid in dna:
        # result += rules[nucleotid]
    
    # better
    rna = []
    for nucleotid in dna:
        rna.append(rules.get(nucleotid))   
    return ''.join(rna)


def test_to_rna():
    assert to_rna("C") == "G"
    assert to_rna("G") == "C"
    assert to_rna("T") == "A"
    assert to_rna("A") == "U"
    assert to_rna("ACGTGGTCTTAA") == "UGCACCAGAAUU"


def build_query_string(dict_params):
    query = []
    for param in sorted(dict_params.keys()):
        temp = []
        temp.append(str(param))
        temp.append(str(dict_params[param]))
        one = '='.join(temp)
        query.append(one)
    #better
    items = []
    for key, value in sorted(dict_params.items()):
        items.append('{}={}'.format(key, value))

    # return '&'.join(query)
    return '&'.join(items)


test = {
            'a': 10,
            's': 'Wow',
            'd': 3.2,
            'z': '89',
        }
# print(build_query_string(test))


def test_build_query_string():
    assert build_query_string({}) == ''
    assert build_query_string({'page': 1}) == 'page=1'
    assert build_query_string({'per': 10, 'page': 1}) == 'page=1&per=10'
    assert build_query_string(
        {
            'a': 10,
            's': 'Wow',
            'd': 3.2,
            'z': '89',
        },
    ) == 'a=10&d=3.2&s=Wow&z=89'


from collections import Counter


def scrabble(symbols, word):
    # set_symb = set(symbols)
    # for letter in word:
        # if letter not in set_symb:
            # return False
    # return True
    
    # better :  return not (Counter(word.lower()) - Counter(string.lower()))
   
    dict_symbs = Counter(symbols.lower())
    dict_word = Counter(word.lower())
    for key, value in dict_word.items():
        if key not in dict_symbs.keys() or value > dict_symbs.get(key):
            return False
    return True
    
   
def test_scrabble():
    assert scrabble('begsdhhtsexoult', 'hexlet') is True
    assert scrabble('rkqodlw', 'world') is True
    assert scrabble('begsdhhtsexoult', 'hexlet') is True
    assert scrabble('katas', 'steak') is False
    assert scrabble('scriptjava', 'javascript') is True
    assert scrabble('scriptingjava', 'javascript') is True
    assert scrabble('scriptjavest', 'javascript') is False
    assert scrabble('', 'hexlet') is False
    assert scrabble('scriptingjava', 'JavaScript') is True
    

from collections import defaultdict


def merged(*args):
    result = defaultdict(set)
    for i in args:
        for k, v in i.items():
            result[k].add(v)
    return result


A, B, C, D = 'abcd'
from copy import deepcopy
def test_merged():

    assert merged() == {}

    assert merged({}, {}) == {}

    assert merged(
        {A: 1},
        {B: 2},
        {C: 3},
    ) == {
        A: {1},
        B: {2},
        C: {3},
    }

    assert merged(
        {A: 1},
        {A: 2},
        {A: 3},
    ) == {
        A: {1, 2, 3},
    }

    assert merged(
        {A: 1, B: 2},
        {B: 3, C: 4},
        {C: 5, D: 6},
    ) == {
        A: {1},
        B: {2, 3},
        C: {4, 5},
        D: {6},
    }

    dict1 = {A: 1, B: 2}
    dict2 = {B: 3, C: 4}
    dict1_copy = deepcopy(dict1)
    dict2_copy = deepcopy(dict2)
    assert merged(
        dict1, dict2,
    ) == {
        A: {1},
        B: {2, 3},
        C: {4},
    }
    assert dict1 == dict1_copy
    assert dict2 == dict2_copy


TITLE, AUTHOR, YEAR = 'title', 'author', 'year'
BOOKS = (
    {TITLE: 'Book of Fooos', AUTHOR: 'Foo', YEAR: 1111},
    {TITLE: 'Cymbeline', AUTHOR: 'Shakespeare', YEAR: 1611},
    {TITLE: 'The Tempest', AUTHOR: 'Shakespeare', YEAR: 1611},
    {TITLE: 'Book of Foos Barrrs', AUTHOR: 'FooBar', YEAR: 2222},
    {TITLE: 'Still foooing', AUTHOR: 'FooBar', YEAR: 333},
    {TITLE: 'Happy Foo', AUTHOR: 'FooBar', YEAR: 4444},
)


def find_where(books, request):
    if not request:
        return books[0]
    for book in books:
        if set(list(request.values())).issubset(set(list(book.values()))):
            return book
    return None

def test_find_where():
    assert find_where(BOOKS, {}) == BOOKS[0]
    assert find_where(BOOKS, {AUTHOR: 'Pushkin'}) is None
    assert find_where(BOOKS, {YEAR: 1111, AUTHOR: 'Pushkin'}) is None
    assert find_where(BOOKS, {"genre": 'Thriller'}) is None
    assert find_where(BOOKS, {YEAR: 1111},   ) == {TITLE: 'Book of Fooos', AUTHOR: 'Foo', YEAR: 1111}
    assert find_where(
        BOOKS, {AUTHOR: 'Shakespeare', YEAR: 1611},
    )[TITLE] == 'Cymbeline'

    assert find_where(BOOKS, BOOKS[2]) == BOOKS[2]


if __name__ == "__main__":
    test_find_where()
    # test_merged()
    # test_scrabble()
    # test_build_query_string()
    # test_to_rna()
    pass

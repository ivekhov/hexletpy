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


def to_roman(source):
    if source == 0:
        return ''
    arab = {
        1000:   'M',    #3      # 19 = 1 : 10, 1 : 5, 1 : 4
        500:    'D',    #1
        100:    'C',    #4
        50:     'L',    #1
        10:     'X',    #1
        5:      'V',    #1
        1:      'I',    #4   
    }
    decomp = arab.copy()
    num = source
    for delim in decomp.keys():
        order = num // delim
        if order != 0:
            residual = num % delim
            decomp[delim] = order
            num = residual
        else:
            decomp[delim] = 0    
    
    result = []
    
    orders = list(decomp.keys())
    orders.reverse()
    new = {}
    for item in orders:
        new[item] = decomp[item]
    decomp = new
    ixs = list(range(len(orders)))
    
    decomp.update({0: 0})
    orders.append(0)
    flag = True
    for ix in ixs:
        if decomp[orders[ix]] != 0 and  ((decomp[orders[ix]] * orders[ix] + \
                decomp[orders[ix+1]] * orders[ix+1]) % 9 == 0):
            temp = 'IX'
            result.insert(0, temp)
            flag = False
            continue
        
        elif decomp[orders[ix]] == 4 and flag:
            temp = 'IV'
            flag = False
            result.insert(0, temp)
            continue 
        else:
            temp = arab[orders[ix]] * decomp[orders[ix]]
            result.insert(0, temp)
        
    print(decomp)
    return ''.join(result)

print(to_roman(59))
print('result: ')

def test_to_roman():
    
    assert to_roman(9) == 'IX'
    assert to_roman(59) == 'LIX'
    assert to_roman(93) == 'XCIII'
    assert to_roman(911) == 'CMXI'
    
    assert to_roman(0) == ''
    assert to_roman(1) == 'I'
    assert to_roman(2) == 'II'
    assert to_roman(4) == 'IV'
    assert to_roman(5) == 'V'
    assert to_roman(6) == 'VI'
    assert to_roman(27) == 'XXVII'
    assert to_roman(48) == 'XLVIII'
    
    assert to_roman(141) == 'CXLI'
    assert to_roman(163) == 'CLXIII'
    assert to_roman(402) == 'CDII'
    assert to_roman(575) == 'DLXXV'
    assert to_roman(1024) == 'MXXIV'
    assert to_roman(2020) == 'MMXX'
    assert to_roman(3000) == 'MMM'


def to_arabic():
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000    
    }


def test_to_arabic():
    assert to_arabic('') == 0
    assert to_arabic('I') == 1
    assert to_arabic('II') == 2
    assert to_arabic('IV') == 4
    assert to_arabic('V') == 5
    assert to_arabic('VI') == 6
    assert to_arabic('XXVII') == 27
    assert to_arabic('XLVIII') == 48
    assert to_arabic('LIX') == 59
    assert to_arabic('XCIII') == 93
    assert to_arabic('CXLI') == 141
    assert to_arabic('CLXIII') == 163
    assert to_arabic('CDII') == 402
    assert to_arabic('DLXXV') == 575
    assert to_arabic('CMXI') == 911
    assert to_arabic('MXXIV') == 1024
    assert to_arabic('MMXX') == 2020
    assert to_arabic('MMM') == 3000


if __name__ == "__main__":
    # test_to_arabic()
    # test_to_roman()
    # test_find_where()
    # test_merged()
    # test_scrabble()
    # test_build_query_string()
    # test_to_rna()
    pass




# cd E:\WORK\python\hexletpy\collections
# c:\Users\ivan\Work\python\envs\py37\Scripts\activate




        # if key == 1:
            # if decomp[1] + decomp[5] == 5:
                # result.insert(0, 'IX')
            # elif value == 4:
                # result.insert(0, 'IV')
            # else:
                # result.insert(0, 'I' * value)
        
        # if key == 10:
            # if decomp[10] + decomp[50] == 5:
                # result.insert(0, 'IX')
            # elif value == 4:
                # result.insert(0, 'IV')
            # else:
                # result.insert(0, 'X' * value)

        # if key == 100:
            # if decomp[100] + decomp[500] == 5:
                # result.insert(0, 'IX')
            # elif value == 4:
                # result.insert(0, 'IV')
            # else:
                # result.insert(0, 'C' * value)
                # 1
        # if key == 5 and value != 0 and decomp[1] + decomp[5] != 5:
            # result.insert(0, 'V')
        
        # if key == 50 and value != 0 and decomp[10] + decomp[50] != 5:
            # result.insert(0, 'L')

        # if key == 500 and value != 0 and decomp[100] + decomp[500] != 5:
            # result.insert(0, 'D')

    # # print(decomp)
    # return ''.join(result)

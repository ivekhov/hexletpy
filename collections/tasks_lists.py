def compare_version(v01, v02):
    if [int(v01.split(".")[0]), int(v01.split(".")[1])] > [int(v02.split(".")[0]), int(v02.split(".")[1])]:
        return 1
    elif [int(v01.split(".")[0]), int(v01.split(".")[1])] < [int(v02.split(".")[0]), int(v02.split(".")[1])]:
        return -1
    return 0


def compare_version_test():
    test = [
        ('0.1', '0.2'),
        ('0.2', '0.1'),
        ('4.2', '4.2')
    ]
    for item in test:
        print('compared versions {} . result: {}'.format(item, compare_version(item[0], item[1])))


def test_compare():
    assert compare_version('0.1', '0.2') == -1
    assert compare_version('0.2', '0.1') == 1
    assert compare_version('4.2', '4.2') == 0
    assert compare_version('0.2', '0.12') == -1
    assert compare_version('3.2', '4.12') == -1
    assert compare_version('3.2', '2.12') == 1


def length_of_last_word(row):
    return len(row.strip().split(' ')[-1].strip())


def test_length_of_last_word():
    print(
        # length_of_last_word('hello, wOrLd!    ')
    )
    assert length_of_last_word('') == 0
    assert length_of_last_word(' \t\n') == 0
    assert length_of_last_word('hi') == 2
    assert length_of_last_word('  cat') == 3
    assert length_of_last_word('man in black') == 5
    assert length_of_last_word('hello, world!') == 6
    assert length_of_last_word('hello, wOrLd!    ') == 6


def is_continuous_sequence(items):
    if len(items) < 2:
        return False
    iterator = iter(items[1:])
    for item in items[:-1]:
        if (item + 1) != next(iterator):
            return False
    return True


def test_is_continuous_sequence():
    assert not is_continuous_sequence([])
    assert not is_continuous_sequence([7])
    assert not is_continuous_sequence([5, 3, 2, 8])
    assert not is_continuous_sequence([10, 11, 12, 14, 15])
    assert not is_continuous_sequence([10, 11, 11, 12])
    assert is_continuous_sequence([0, 1, 2, 3])
    assert is_continuous_sequence([-5, -4, -3])
    assert is_continuous_sequence([10, 11, 12, 13])


# Example solution
def is_continuous_sequence_x(source):
    if len(source) < 2:
        return False
    for x, y in zip(source, source[1:]):
        if (y - x) != 1:
            return False
    return True


def same_parity_filter(source):
    if not source:  # instead of len(source) == 0
        return []
    pattern = source[0] % 2
    result = [source[0]]
    for item in source[1:]:
        if item % 2 == pattern:
            result.append(item)
    return result


def test_same_parity_filter():
    assert same_parity_filter([5, 0, 1, -3, 10]) == [5, 1, -3]
    assert same_parity_filter([2, 0, 1, -3, 10, -2]) == [2, 0, 10, -2]
    assert same_parity_filter([-1, 0, 1, -3, 10, -2]) == [-1, 1, -3]
    assert same_parity_filter([10, -1.5, 1.3, -3, 25, -2]) == [10, -2]
    assert same_parity_filter([]) == []

# Реализуйте функцию chunked, которая принимает на вход число и последовательность. Число которое задает размер
# чанка (куска). Функция должна вернуть список,
# состоящий из чанков указанной размерности. При этом список должен делиться на куски-списки, строка — на строки,
# кортеж — на кортежи!
def chunked(num, source):
    a, b = source[:num], source[num:]
    result = []
    if a:
        result.append(a)
    if b:
        result.append(b)
    return result


def test_chunked_list():
    assert chunked(2, ['a', 'b', 'c', 'd']) == [['a', 'b'], ['c', 'd']]
    assert chunked(3, ['e', 'f', 'h', 'i']) == [['e', 'f', 'h'], ['i']]
    assert chunked(4, ['g', 'k', 'l', 'm']) == [['g', 'k', 'l', 'm']]
    assert chunked(4, []) == []
    assert chunked(2, ['n']) == [['n']]


def test_chunked_tuple():
    assert chunked(2, ('A', 'B', 'C', 'D')) == [('A', 'B'), ('C', 'D')]
    assert chunked(3, ('E', 'F', 'H', 'I')) == [('E', 'F', 'H'), ('I',)]
    assert chunked(4, ('G', 'K', 'L', 'M')) == [('G', 'K', 'L', 'M')]
    assert chunked(4, []) == []
    assert chunked(2, ('N',)) == [('N',)]


def test_chunked_str():
    assert chunked(2, 'abcd') == ['ab', 'cd']
    assert chunked(3, 'efhi') == ['efh', 'i']
    assert chunked(4, 'gklm') == ['gklm']
    assert chunked(4, '') == []
    assert chunked(2, 'x') == ['x']


def mirror_matrix(matrix):
    if matrix and matrix != [[()]]:
        center = int(round(len(matrix[0]) / 2))
        flag = len(matrix[0]) % 2
        for row in matrix:
            row[center::1] = row[center - 1 - flag::-1]

# -1 version
def shift_even_f(matrix, center, flag):
    for row in matrix:
        row[center::1] = row[center - 1 - flag::-1]


# -2 version
def shift_even(matrix, center):
    for row in matrix:
        row[center::1] = row[center - 1::-1]


def shift_matrix(matrix, center):
    for row in matrix:
        row[center::1] = row[center - 2::-1]


def test_mirror_matrix_return_value():
    assert mirror_matrix([[42]]) is None, (
        "Function shouldn't return anything!"
    )


def test_mirror_matrix():
    empty = []
    mirror_matrix(empty)
    assert empty == []

    empty_row = [
        [],
    ]
    mirror_matrix(empty_row)
    assert empty_row == [[]]

    single_cell = [
        [()],
    ]
    mirror_matrix(single_cell)
    assert single_cell == [[()]]

    text_sample = [
        ['aa', 'bb', 'cc'],
        ['11', '22', '33'],
    ]
    mirror_matrix(text_sample)
    assert text_sample == [
        ['aa', 'bb', 'aa'],
        ['11', '22', '11'],
    ]

    number_sample = [
        [11, 12, 13, 14, 15, 16],
        [21, 22, 23, 24, 25, 26],
        [31, 32, 33, 34, 35, 36],
        [41, 42, 43, 44, 45, 46],
        [51, 52, 53, 54, 55, 56],
        [61, 62, 63, 64, 65, 66],
    ]
    mirror_matrix(number_sample)
    assert number_sample == [
        [11, 12, 13, 13, 12, 11],
        [21, 22, 23, 23, 22, 21],
        [31, 32, 33, 33, 32, 31],
        [41, 42, 43, 43, 42, 41],
        [51, 52, 53, 53, 52, 51],
        [61, 62, 63, 63, 62, 61],
    ]


test = [
    [10, 20],
    [30, 40],
]

test2 = [
     ['d', 'o'],
     ['r', 'e'],
     ['m', 'i'],
]

resp2 = [
     ['d', 'r', 'm'],
     ['o', 'e', 'i']
]


def transposed(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transposed_matrix = []
    for col in range(0, cols):
        transposed_row = []
        for index in range(0, rows):
            transposed_row.append(matrix[index][col])
        transposed_matrix.append(transposed_row)
    return transposed_matrix


# Example
def transposed_x(matrix):
    return list(map(list, zip(*matrix)))


SAMPLES = (
    # single cell
    ([[42]], [[42]]),

    # column
    ([
        [1],
        [2],
        [3],
    ], [
        [1, 2, 3],
    ]),

    # row
    ([
        [4, 5, 6],
    ], [
        [4],
        [5],
        [6],
    ]),

    # square matrix
    ([
        [10, 20],
        [30, 40],
    ], [
        [10, 30],
        [20, 40],
    ]),

    # rectangle matrix
    ([
        ['d', 'o'],
        ['r', 'e'],
        ['m', 'i'],
    ], [
        ['d', 'r', 'm'],
        ['o', 'e', 'i'],
    ]),
)


def test_transposed():
    for matrix, result in SAMPLES:
        assert transposed(matrix) == result


def test_transposed_reversibility():
    for matrix, _ in SAMPLES:
        assert transposed(transposed(matrix)) == matrix


import operator

def rpn_calc(source):
    stack = []
    operators = ['+', '-', '/', '*']
    for item in source:
        if item not in operators:
            stack.append(item)
        else:
            if item == '+':
                stack.append(operator.add(stack.pop(), stack.pop()))
            if item == '-':
                stack.append(operator.add(-stack.pop(), stack.pop()))
            if item == '*':
                stack.append(operator.mul(stack.pop(), stack.pop()))
            if item == '/':
                stack.append(operator.delitem(stack.pop(), stack.pop()))
    return stack[0]


# def rpn_calc(source):
#     stack = []
#     for item in source:
#         if item != '+' and item != '-' and item != '*' and item != '/':

#         if item != '+' and item != '-' and item != '*' and item != '/':
#             stack.append(item)
#         else:
#             if item == '+':
#                 result = stack.pop() + stack.pop()
#                 stack.append(result)
#             elif item == '-':
#                 result = -stack.pop() + stack.pop()
#                 stack.append(result)
#             elif item == '*':
#                 result = stack.pop() * stack.pop()
#                 stack.append(result)
#             elif item == '/':
#                 result = stack.pop() / stack.pop()
#                 stack.append(result)
#     return stack[0]

# Example solution
# BEGIN
get_operator = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}.get


def rpn_calc_x(rpn):
    stack = []
    for elem in rpn:
        op = get_operator(elem)
        if op is not None:
            x = stack.pop()
            y = stack.pop()
            elem = op(y, x)
        stack.append(elem)
    return stack[0]
# END


def test_rpn_calc():
    assert rpn_calc([1, 2, '+', 4, '*', 3, '+']) == 15
    assert rpn_calc([7, 2, 3, '*', '-']) == 1
    assert rpn_calc([1, 2, '+', 2, '*']) == 6


def summary_ranges(items):
    result = []
    selected = []
    iterator = iter(items)
    flag = 0
    for item in items[1:]:
        if item == (next(iterator) + 1):
            if flag == 0:
                selected.append([])
                selected[-1].append(item - 1)
            flag = 1
            selected[-1].append(item)
        else:
            flag = 0
    for arr in selected:
        result.append(str(arr[0]) + '->' + str(arr[-1]))
    return result


# Example solution
def summary_ranges_x(numbers):
    if not numbers:
        return []

    ranges = []
    current_sequence = [numbers[0]]
    sequences = [current_sequence]

    for x, y in zip(numbers, numbers[1:]):
        if (y - x) == 1:
            current_sequence.append(y)
        else:
            current_sequence = [y]
            sequences.append(current_sequence)

    # здесь [0, 1, 2, 7, 5, 6] уже преобразован
    # в [[0, 1, 2], [7], [5, 6]]

    for sequence in sequences:
        if len(sequence) > 1:
            first, last = sequence[0], sequence[-1]
            ranges.append('{}->{}'.format(first, last))

    return ranges


def test_find_summary_ranges():
    assert summary_ranges([]) == []
    assert summary_ranges([1]) == []
    assert summary_ranges([1, 2, 3]) == ['1->3']
    assert summary_ranges([0, 1, 2, 7, 5, 6]) == ['0->2', '5->6']
    assert summary_ranges(
        [1, 1, 3, 4, 5, -6, 8, 9, 10, 12, 14, 14],
    ) == ['3->5', '8->10']
    assert summary_ranges(
        [110, 111, 112, 111, -5, -4, -2, -3, -4, -5],
    ) == ['110->112', '-5->-4']


def find_longest_length(row):
    if len(row) < 2:
        return len(row)
    chunks = []
    chunks.append([])
    for symbol in row:
        if symbol not in chunks[-1]:
            chunks[-1].append(symbol)
        else:
            chunks.append([])
            chunks[-1].append(symbol)
    reviewed = [[]]
    for first, second in zip(chunks, chunks[1:]):
        if first[-1] != second[0]:
            for item in first[1:]:
                if item not in reviewed[-1]:
                    reviewed[-1].append(item)
            for item in second:
                if item not in reviewed[-1]:
                    reviewed[-1].append(item)
        else:
            reviewed.append([])
        reviewed.append([])
    for chunk in chunks:
        reviewed.append(chunk)
    return max(list(map(len, reviewed)))
    # return chunks, reviewed

# Example solution
# BEGIN
def unique_sequence_length(string):
    unique_sequence = set()
    length = 0
    for char in string:
        if char in unique_sequence:
            break
        unique_sequence.add(char)
        length += 1
    return length


def find_longest_length_x(string):
    longest_length = 0
    for i, _ in enumerate(string):
        substring_length = unique_sequence_length(string[i:])
        if longest_length < substring_length:
            longest_length = substring_length
    return longest_length
# END


def test_find_length_length():
    assert find_longest_length('') == 0
    assert find_longest_length('a') == 1
    assert find_longest_length('jabjcdel') == 7
    assert find_longest_length('abcddef') == 4
    assert find_longest_length('abbccddeffg') == 3
    assert find_longest_length('abcd') == 4
    assert find_longest_length('1234561qweqwer') == 9


def multiply(a, b):
    if len(a[0]) == len(b):
        result = []
        for ix_row in range(len(a)):
            result.append([])
            for ix_col in range(len(b[0])):
                temp = 0
                for ix_element in range(len(a[0])):
                    temp += a[ix_row][ix_element] * b[ix_element][ix_col]
                result[-1].append(temp)
        return result
    return None


def test_multiply():
    a = [
            [1, 2, 1],  #

                [0, 1, 0],
                [2, 3, 4],
    ]
    b = [
            #1      #2
            [2,     5],
            [6,     7],
            [1,     8],
    ]

    # a = m x n
    # b = n x k
    # r = m X k
    # [
    #   [],
    #           [],
    #           []
    # ]

    assert multiply(a, b) == [
        [15, 27],
            [6, 7],
            [26, 63],
    ]



    assert multiply(
        [[2]],
        [[3]],
    ) == [[6]]

    a = [
        [1],
        [2],
    ]
    b = [
        [10, 20],
    ]
    assert multiply(a, b) == [
        [10, 20],
        [20, 40],
    ]


def show(image):
    for line in image:
        print(line)


frame = [
     '****',
     '*  *',
     '*  *',
     '****'
]


def double_symb(symb):
    return str(symb) + str(symb)


def enlarge(frame):
    if frame:
        result = []
        for row in frame:
            result.append([])
            for symb in row:
                result[-1].append(symb * 2)
            result[-1] = ''.join(result[-1])
            result.append(result[-1])
        frame = result
        return frame
    return frame


# BEGIN
def enlarge_x(image):
    output = []
    for line in image:
        row = []
        for pixel in line:
            # expand horizontally
            row.extend([pixel, pixel])
        row = ''.join(row)
        # expand verticaly
        output.extend([
            row,
            row,
        ])
    return output
# END


def test_enlarge():
    assert enlarge([]) == []
    assert enlarge(['']) == ['', '']
    assert enlarge([
        'A',
    ]) == [
        'AA',
        'AA',
    ]
    assert enlarge([
        ' *',
        '# ',
    ]) == [
        '  **',
        '  **',
        '##  ',
        '##  ',
    ]


def sum_of_intervals(intervals):
    intervals.sort()
    mins = [intervals[0][0]]
    maxs = [intervals[0][1]]
    for chunk in intervals[1:]:
        if chunk[0] < chunk[1]:
            for ix in range(len(mins)):
                if chunk[0] >= mins[ix] and chunk[1] <= maxs[ix]:
                    continue
                elif (chunk[0] >= mins[ix] and chunk[0] < maxs[ix]) and chunk[1] > maxs[ix]:
                    maxs[ix] = chunk[1]
                elif (chunk[0] < mins[ix] and chunk[1] > mins[ix]) or chunk[1] <= maxs[ix]:
                    mins[ix] = chunk[0]
                elif chunk[0] > maxs[ix] or chunk[1] < mins[ix]:
                    mins.append(chunk[0])
                    maxs.append(chunk[1])
    return sum(list(map(lambda x, y: x - y, maxs, mins)))


# Example
# BEGIN
def sum_of_intervals_x(intervals):
    values = []
    for start, end in intervals:
        for i in range(start, end):
            if i not in values:
                values.append(i)
    return len(values)
# END


def test_sum_of_intervals():
    assert sum_of_intervals([[5, 5]]) == 0
    assert sum_of_intervals([[3, 10]]) == 7

    assert sum_of_intervals([
        [1, 2],
        [11, 12],
    ]) == 2

    assert sum_of_intervals([
        [2, 7],
        [6, 6],
    ]) == 5

    assert sum_of_intervals([
        [1, 5],
        [1, 10],
    ]) == 9

    assert sum_of_intervals([
        [1, 9],
        [7, 12],
        [3, 4],
    ]) == 11

    assert sum_of_intervals([
        [7, 10],
        [1, 4],
        [2, 5],
    ]) == 7

    assert sum_of_intervals([
        [1, 5],
        [9, 19],
        [1, 7],
        [16, 19],
        [5, 11],
    ]) == 18

    assert sum_of_intervals([
        [1, 3],
        [20, 25],
    ]) == 7






MONEY = (  # noqa: WPS317
    1, 20, 2, 5, 20,
    3, 5, 2, 10, 2,
    20, 2, 20, 1, 2,
    1, 1, 2, 10, 20, 3,
)

from collections import Counter


def visualize(coins, bar_char='₽'):
    c = Counter(coins)
    temp = list(c.keys())
    temp.sort()
    new_dict = {}
    for key in temp:
        new_dict[key] = c[key]
    local_max = max(new_dict.values())
    picture_height = local_max + 3
    countdown = picture_height
    result_array = []
    visual = ''

    for row in range(picture_height+1):
        empty_cell = '  '
        rows_delim = ' '
        row4print = ''
        if countdown >= 2:
            for nominal in temp:
                if new_dict[nominal] == countdown:
                    row4print += (str(new_dict[nominal]) + rows_delim + rows_delim)
                elif new_dict[nominal] > countdown:
                    row4print += (bar_char + bar_char + rows_delim)
                else:
                    row4print += (empty_cell + rows_delim)
        elif countdown == 1:
            row4print += ('---' * len(temp))
        elif countdown == 0:
            for nominal in new_dict.keys():
                if nominal < 10:
                    row4print += (str(nominal) + rows_delim + rows_delim)
                else:
                    row4print += (str(nominal) + rows_delim)
        countdown = countdown - 1
        result_array.append(row4print[:-1])
    for row in result_array:
        visual += (row + '\n')
    return visual

# print(visualize(MONEY))


def test_visualize():
    assert visualize(MONEY) == """
   6..7..7             
   ₽₽          5 
4  ₽₽          ₽₽
₽₽ ₽₽          ₽₽
₽₽ ₽₽ 2..2  2  ₽₽
₽₽ ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
₽₽ ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
-----------------
1  2  3  5  10 20
"""[1:-1]  # noqa: W291

    assert visualize(MONEY, bar_char='$') == """
   6             
   $$          5 
4  $$          $$
$$ $$          $$
$$ $$ 2  2  2  $$
$$ $$ $$ $$ $$ $$
$$ $$ $$ $$ $$ $$
-----------------
1  2  3  5  10 20
"""[1:-1]  # noqa: W291




if __name__ == '__main__':
    print(visualize(MONEY))
    # test_visualize()
    # test_sum_of_intervals()
    # test_enlarge()
    # test_multiply()
    # test_find_length_length()
    # test_find_summary_ranges()
    # test_rpn_calc()
    # test_transposed()
    # test_transposed_reversibility()
    # test_mirror_matrix_return_value()
    # test_mirror_matrix()
    # test_chunked_list()
    # test_chunked_str()
    # test_chunked_tuple()
    # test_same_parity_filter()
    # test_is_continuous_sequence()
    # test_length_of_last_word()
    # compare_version_test()
    # test_compare()
    pass

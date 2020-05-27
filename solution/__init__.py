# BAD WAY
# from .numbers1 import mul1 as mul
# from .numbers2 import power2 as power, add2 as add, sub2 as sub
# from .numbers3 import sqrt3 as sqrt
# import numbers1, numbers2, numbers3

# import solution.numbers1
# import solution.numbers2
# import solution.numbers3

# mul = solution.numbers1.mul1
# add = solution.numbers2.add2
# sqrt = solution.numbers3.sqrt3
# power = solution.numbers2.power2

## BEST WAY OF IMPORTING
from solution.numbers1 import mul1 as mul
from solution.numbers2 import power2 as power, add2 as add, sub2 as sub
from solution.numbers3 import sqrt3 as sqrt


__all__ = [     # noqa: WPS410
'power', 'add', 'sqrt', 'mul', 'sub',
]

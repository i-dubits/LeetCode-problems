
from typing import List


class Solution:

    n = None

    def rotate(self, matrix: List[List[int]]) -> None:
        self.n = len(matrix)

        x_tr = -(self.n//2)
        y_tr = self.n // 2

        for y in range(y_tr, 0, -1):
            for x in range(x_tr, 1, 1):
                if (x == 0 or y == 0) and self.n % 2 == 0:
                    continue
                self.rotate_4_el(matrix, x, y)


        return matrix

    def rotate_4_el(self, matrix: List[List[int]], x: int, y: int):
        "x, y - transformed indices"
        def to_ord(coord: int, c_type: str = 'x') -> int:
            if c_type == 'x':
                if self.n % 2 == 0:
                    if coord < 0:
                        return coord + self.n // 2
                    else:
                        return coord + self.n // 2 - 1
                else:
                    return coord + self.n // 2
            elif c_type == 'y':
                if self.n % 2 == 0:
                    if coord > 0:
                        return -coord + self.n // 2
                    else:
                        return -coord + self.n // 2 - 1
                else:
                    return -coord + self.n // 2

        y_mx = matrix[to_ord(-x, c_type='y')][to_ord(y)]
        mx_my = matrix[to_ord(-y, c_type='y')][to_ord(-x)]
        my_x = matrix[to_ord(x, c_type='y')][to_ord(-y)]
        x_y = matrix[to_ord(y, c_type='y')][to_ord(x)]

        matrix[to_ord(y,  c_type='y')][to_ord(x)] = my_x
        matrix[to_ord(x,  c_type='y')][to_ord(-y)] = mx_my
        matrix[to_ord(-y, c_type='y')][to_ord(-x)] = y_mx
        matrix[to_ord(-x, c_type='y')][to_ord(y)] = x_y





def full_pipeline(numbers):
    sol = Solution()

    ans = sol.rotate(numbers)
    return ans



# numbers = [
#   [1,2],
#   [3,4]
# ]
# numbers = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
numbers =     [
        [5,1,9,11],
        [2,4,8,10],
        [13,3,6,7],
        [15,14,12,16]
    ]

print( full_pipeline(numbers) )


str_list = [
    [
  [1,2],
  [3,4]
    ],
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [5,1,9,11],
        [2,4,8,10],
        [13,3,6,7],
        [15,14,12,16]
    ],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )
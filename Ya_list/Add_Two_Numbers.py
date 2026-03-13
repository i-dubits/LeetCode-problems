
from typing import Optional, List

from scipy.signal import peak_widths


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values: List[int]) -> Optional[ListNode]:

    if len(values) == 0:
        return None

    root_el = ListNode(values[0])
    curr = root_el

    for i in range(1, len(values)):
        curr.next = ListNode(values[i])
        curr = curr.next

    return root_el

def print_linked_list(root_el:ListNode):
    res = []
    while root_el != None:
        res.append(str(root_el.val))
        root_el = root_el.next

    print(' '.join(res))


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        res_root = None
        prev_node = None

        add_one = False
        while l1 is not None or l2 is not None:
            first = l1.val if l1 is not None else 0
            second = l2.val if l2 is not None else 0

            res = first + second + int(add_one)
            new_node = ListNode(res%10)
            if res_root is None:
                res_root = new_node
                prev_node = new_node
            else:
                prev_node.next = new_node
                prev_node = new_node

            if res >= 10:
                add_one = True
            else:
                add_one = False

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if add_one:
            new_node = ListNode(1)
            prev_node.next = new_node

        return res_root


def full_pipeline(l1, l2):

    sol = Solution()
    l1_root = build_linked_list(l1)
    l2_root = build_linked_list(l2)
    ans = sol.addTwoNumbers(l1_root, l2_root)
    print_linked_list(ans)
    return ans

numbers = [ [2,4,3], [5,6,4] ]
full_pipeline(numbers[0], numbers[1])


str_list = [
    [ [2,4,3], [5,6,4] ],
    [ [9,9,9,9,9,9,9], [9,9,9,9] ],
]

for str_curr in str_list:
    full_pipeline(str_curr[0], str_curr[1])
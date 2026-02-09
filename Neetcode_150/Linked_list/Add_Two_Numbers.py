
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add_one = False
        start_el = ListNode(-1)
        curr = start_el

        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                val_1, val_2 = l1.val, l2.val
            elif l1 is not None and l2 is None:
                val_1, val_2 = l1.val, 0
            elif l1 is None and l2 is not None:
                val_1, val_2 = 0, l2.val

            val = val_1 + val_2
            if add_one:
                val += 1
            if val >= 10:
                add_one = True
                val = val % 10
            else:
                add_one = False

            new_node = ListNode(val)
            curr.next = new_node
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if add_one:
            new_node = ListNode(1)
            curr.next = new_node
            curr = curr.next

        return start_el.next




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

def full_pipeline_list(l1, l2):
    sol = Solution()
    l1 = build_linked_list(l1)
    l2 = build_linked_list(l2)

    ans = sol.addTwoNumbers(l1, l2)
    print_linked_list(ans)
    return ans


# list_els = [[1,2,3], [4,5,6]]
list_els = [[9], [9]]

full_pipeline_list(*list_els)


str_list = [
    [[1,2,3], [4,5,6]],
    [[9], [9]],
    [[9,9,9,9,9,9,9], [9,9,9,9]]
]

for str_curr in str_list:
    full_pipeline_list(*str_curr)



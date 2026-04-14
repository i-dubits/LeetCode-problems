
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

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

def full_pipeline_list(numbers):
    sol = Solution()
    root_el = build_linked_list(numbers)
    ans = sol.reverseList(root_el)
    # print(ans)
    print_linked_list(ans)
    return ans


# list_els = [0,1,2,3]
list_els = [1,2,3,4,5]

full_pipeline_list(list_els)


str_list = [
    [0,1,2,3],
]

for str_curr in str_list:
    full_pipeline_list(str_curr)

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr = head
        prev = None

        while curr.next != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        curr.next = prev

        return curr

def build_linked_list(values: List[int]) -> Optional[ListNode]:

    if len(values) == 0:
        return None

    root_el = ListNode(values[0])
    curr = root_el

    for v in range(1, len(values)):
        curr.next = ListNode(v)
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


list_els = [0,1,2,3]
# numbers = [1,7,2,5,12,3,500,500,7,8,4,7,3,6]
# numbers = [1,2,1]

full_pipeline_list(list_els)


str_list = [
    [0,1,2,3],
]

for str_curr in str_list:
    full_pipeline_list(str_curr)
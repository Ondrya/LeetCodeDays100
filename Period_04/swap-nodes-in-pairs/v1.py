# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # реализовать
        pass


# Вспомогательная функция для преобразования списка в связный список (для тестов)
def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Вспомогательная функция для преобразования связного списка в список (для тестов)
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def run_tests():
    solution = Solution()
    
    # Тест 1: [1,2,3,4] -> [2,1,4,3]
    head1 = list_to_linkedlist([1, 2, 3, 4])
    result1 = solution.swapPairs(head1)
    assert linkedlist_to_list(result1) == [2, 1, 4, 3], "Тест 1 провален"
    
    # Тест 2: [] -> []
    head2 = list_to_linkedlist([])
    result2 = solution.swapPairs(head2)
    assert linkedlist_to_list(result2) == [], "Тест 2 провален"
    
    # Тест 3: [1] -> [1]
    head3 = list_to_linkedlist([1])
    result3 = solution.swapPairs(head3)
    assert linkedlist_to_list(result3) == [1], "Тест 3 провален"
    
    # Тест 4: [1,2,3] -> [2,1,3]
    head4 = list_to_linkedlist([1, 2, 3])
    result4 = solution.swapPairs(head4)
    assert linkedlist_to_list(result4) == [2, 1, 3], "Тест 4 провален"
    
    print("Все тесты пройдены!")


if __name__ == "__main__":
    run_tests()
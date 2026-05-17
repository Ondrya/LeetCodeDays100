# Задача: Reverse Linked List (LeetCode 206)
# 
# Важное замечание по оптимизации:
# ================================
# Данная задача НЕ ИМЕЕТ решения за O(1) времени, так как необходимо обойти
# все N узлов списка. Теоретическая нижняя граница сложности - Ω(N).
#
# Однако есть ДВА классических подхода:
# 1. Итеративный (сложность O(N) времени, O(1) памяти) - оптимальный
# 2. Рекурсивный (сложность O(N) времени, O(N) памяти из-за стека вызовов)
#
# Итеративный подход является лучшим решением с точки зрения практики,
# так как требует минимальной дополнительной памяти.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list.
        
        Args:
            head: Head node of the linked list
            
        Returns:
            Head of the reversed linked list
            
        Time Complexity: O(N) - must visit each node once
        Space Complexity: O(1) - only use constant extra space
        """
        # TODO: Implement iterative reversal
        # Pseudo-code:
        # prev = None
        # curr = head
        # while curr is not None:
        #     next_temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_temp
        # return prev
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        return prev


# Тесты для проверки правильности реализации
def run_tests():
    """
    Test cases for reverseList function.
    
    Note: These tests assume ListNode class is defined and
    helper functions to convert between list and ListNode are available.
    """
    solution = Solution()
    
    # Helper functions for testing
    def create_linked_list(arr):
        """Convert list to linked list"""
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def linked_list_to_list(head):
        """Convert linked list to list for easy comparison"""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    # Тест 1: [1,2,3,4,5] -> [5,4,3,2,1]
    head1 = create_linked_list([1, 2, 3, 4, 5])
    reversed1 = solution.reverseList(head1)
    assert linked_list_to_list(reversed1) == [5, 4, 3, 2, 1], "Тест 1 провален"
    
    # Тест 2: [1,2] -> [2,1]
    head2 = create_linked_list([1, 2])
    reversed2 = solution.reverseList(head2)
    assert linked_list_to_list(reversed2) == [2, 1], "Тест 2 провален"
    
    # Тест 3: [] -> []
    head3 = create_linked_list([])
    reversed3 = solution.reverseList(head3)
    assert linked_list_to_list(reversed3) == [], "Тест 3 провален"
    
    # Тест 4: [1] -> [1] (один элемент)
    head4 = create_linked_list([1])
    reversed4 = solution.reverseList(head4)
    assert linked_list_to_list(reversed4) == [1], "Тест 4 провален"
    
    # Тест 5: [-5000, 0, 5000] -> [5000, 0, -5000] (граничные значения)
    head5 = create_linked_list([-5000, 0, 5000])
    reversed5 = solution.reverseList(head5)
    assert linked_list_to_list(reversed5) == [5000, 0, -5000], "Тест 5 провален"
    
    print("Все тесты пройдены!")


if __name__ == "__main__":
    run_tests()
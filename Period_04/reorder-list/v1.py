"""
Задача: Reorder List (LeetCode 143)

Переупорядочить односвязный список из вида:
L0 → L1 → … → Ln-1 → Ln
в вид:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

Ограничения: нельзя изменять значения узлов, только ссылки.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # реализовать
        pass





def create_linked_list(values):
    """Вспомогательная функция для создания списка из значений."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Вспомогательная функция для преобразования списка в Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def run_tests():
    solution = Solution()
    
    # Тест 1: Чётное количество узлов [1,2,3,4] → [1,4,2,3]
    head1 = create_linked_list([1, 2, 3, 4])
    solution.reorderList(head1)
    assert linked_list_to_list(head1) == [1, 4, 2, 3], "Тест 1 провален"
    
    # Тест 2: Нечётное количество узлов [1,2,3,4,5] → [1,5,2,4,3]
    head2 = create_linked_list([1, 2, 3, 4, 5])
    solution.reorderList(head2)
    assert linked_list_to_list(head2) == [1, 5, 2, 4, 3], "Тест 2 провален"
    
    # Тест 3: Один узел [1] → [1]
    head3 = create_linked_list([1])
    solution.reorderList(head3)
    assert linked_list_to_list(head3) == [1], "Тест 3 провален"
    
    # Тест 4: Два узла [1,2] → [1,2]
    head4 = create_linked_list([1, 2])
    solution.reorderList(head4)
    assert linked_list_to_list(head4) == [1, 2], "Тест 4 провален"
    
    # Тест 5: [1,2,3,4,5,6] → [1,6,2,5,3,4]
    head5 = create_linked_list([1, 2, 3, 4, 5, 6])
    solution.reorderList(head5)
    assert linked_list_to_list(head5) == [1, 6, 2, 5, 3, 4], "Тест 5 провален"
    
    print("Все тесты пройдены!")


if __name__ == "__main__":
    run_tests()
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
        """
        Изменяет список на месте, ничего не возвращает.
        Преобразует L0 → L1 → ... → Ln в L0 → Ln → L1 → Ln-1 → L2 → ...
        """
        # Если список пуст или состоит из одного узла - ничего не делаем
        if not head or not head.next:
            return
        
        # Шаг 1: Находим середину списка (медленный и быстрый указатели)
        slow = head  # медленный указатель
        fast = head  # быстрый указатель
        
        # Быстрый движется в 2 раза быстрее медленного
        # Когда быстрый достигает конца, медленный оказывается в середине
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Шаг 2: Разворачиваем вторую половину списка
        prev = None           # предыдущий узел (станет новым хвостом)
        curr = slow.next      # текущий узел (начало второй половины)
        slow.next = None      # разрываем связь между половинами
        
        # Стандартный алгоритм разворота связного списка
        while curr:
            next_temp = curr.next  # сохраняем следующий узел
            curr.next = prev       # разворачиваем ссылку
            prev = curr            # сдвигаем prev
            curr = next_temp       # переходим к следующему узлу
        
        # Шаг 3: Сливаем две половины в требуемом порядке
        first = head    # начало первой половины
        second = prev   # начало развернутой второй половины
        
        # Чередуем узлы из первой и второй половин
        while second:
            next_first = first.next   # сохраняем следующий узел первой половины
            next_second = second.next # сохраняем следующий узел второй половины
            
            first.next = second       # первый указывает на второй
            second.next = next_first  # второй указывает на следующий первого
            
            first = next_first        # перемещаемся к следующей паре
            second = next_second      # перемещаемся к следующему узлу второй половины




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
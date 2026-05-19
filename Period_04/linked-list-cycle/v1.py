# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True


# Тесты для задачи определения цикла в связном списке
def run_tests():
    solution = Solution()
    
    # Вспомогательная функция для создания списка с циклом
    def create_linked_list_with_cycle(arr, pos):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        cycle_node = None
        if pos == 0:
            cycle_node = head
        
        for i in range(1, len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
            if i == pos:
                cycle_node = current
        
        if pos != -1 and cycle_node:
            current.next = cycle_node
        
        return head
    
    # Тест 1: Список с циклом (пример из задачи)
    head1 = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    assert solution.hasCycle(head1) == True, "Тест 1 провален"
    
    # Тест 2: Список с циклом из двух элементов
    head2 = create_linked_list_with_cycle([1, 2], 0)
    assert solution.hasCycle(head2) == True, "Тест 2 провален"
    
    # Тест 3: Список без цикла (один элемент)
    head3 = create_linked_list_with_cycle([1], -1)
    assert solution.hasCycle(head3) == False, "Тест 3 провален"
    
    # Тест 4: Пустой список
    head4 = None
    assert solution.hasCycle(head4) == False, "Тест 4 провален"
    
    # Тест 5: Список без цикла из нескольких элементов
    head5 = create_linked_list_with_cycle([1, 2, 3, 4, 5], -1)
    assert solution.hasCycle(head5) == False, "Тест 5 провален"
    
    # Тест 6: Список, где цикл на первом элементе
    head6 = create_linked_list_with_cycle([1, 2, 3, 4], 0)
    assert solution.hasCycle(head6) == True, "Тест 6 провален"
    
    # Тест 7: Список с циклом, где pos - последний элемент
    head7 = create_linked_list_with_cycle([1, 2, 3, 4], 3)
    assert solution.hasCycle(head7) == True, "Тест 7 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()
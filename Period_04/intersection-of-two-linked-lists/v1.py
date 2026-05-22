"""
Задача: Find Intersection of Two Linked Lists (160. Intersection of Two Linked Lists)

Решение: Используем двухпоинтерный подход (алгоритм с выравниванием длин)
или более элегантный алгоритм с обменом списками.

ОПТИМАЛЬНОЕ РЕШЕНИЕ СЛОЖНОСТЬЮ O(1) ПАМЯТИ:
================================================================================
Существует элегантное решение с использованием двух указателей (т.н. "алгоритм Floyd'a" или "алгоритм с обменом списками"):

1. Инициализируем два указателя pA и pB на headA и headB соответственно
2. Пока pA != pB:
   - Если pA достиг конца списка A, перенаправляем его на headB
   - Иначе перемещаем pA на следующий узел
   - Если pB достиг конца списка B, перенаправляем его на headA
   - Иначе перемещаем pB на следующий узел
3. Возвращаем pA (который будет либо узлом пересечения, либо null)

Почему это работает:
- Если списки пересекаются, указатели пройдут одинаковое расстояние до встречи в точке пересечения
- Если не пересекаются, оба указателя пройдут m+n узлов и встретятся на null

Сложность:
- Время: O(m + n), где m и n - длины списков
- Память: O(1) - только два указателя

Хотя временная сложность O(m+n), это оптимально, так как в любом случае 
нужно просмотреть оба списка. Но память - O(1) - это лучший возможный результат.
================================================================================
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Находит узел пересечения двух односвязных списков.
        
        Args:
            headA: Головной узел первого списка
            headB: Головной узел второго списка
            
        Returns:
            Узел пересечения или None, если списки не пересекаются
            
        Time: O(m + n), где m и n - длины списков
        Memory: O(1) - константная память
        """
        
        if not headA or not headB:
            return None
        
        # Инициализируем два указателя
        pA = headA
        pB = headB
        
        # Идем до тех пор, пока указатели не встретятся
        while pA != pB:
            # Если pA достиг конца, перенаправляем на headB
            # Иначе идем дальше по списку A
            pA = pA.next if pA else headB
            
            # Если pB достиг конца, перенаправляем на headA
            # Иначе идем дальше по списку B
            pB = pB.next if pB else headA
        
        # pA и pB либо указывают на узел пересечения, либо оба равны None
        return pA


# Тесты для проверки решения
def run_tests():
    """
    Тесты для проверки корректности решения.
    ВАЖНО: Тесты написаны в предположении, что у нас есть доступ к узлам.
    В реальной среде тестирования списки создаются автоматически.
    """
    
    def create_linked_list(values):
        """Вспомогательная функция для создания связного списка"""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def get_list_values(head):
        """Вспомогательная функция для получения значений списка"""
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values
    
    solution = Solution()
    
    # Тест 1: Пример с пересечением
    # Создаем общую часть: 8 -> 4 -> 5
    common = ListNode(8)
    common.next = ListNode(4)
    common.next.next = ListNode(5)
    
    # Создаем список A: 4 -> 1 -> common
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = common
    
    # Создаем список B: 5 -> 6 -> 1 -> common
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = common
    
    result = solution.getIntersectionNode(headA, headB)
    assert result == common, f"Тест 1 провален: ожидался узел с значением 8"
    print("Тест 1 пройден!")
    
    # Тест 2: Пример с пересечением (другая структура)
    # Создаем общую часть: 2 -> 4
    common2 = ListNode(2)
    common2.next = ListNode(4)
    
    # Создаем список A: 1 -> 9 -> 1 -> common2
    headA2 = ListNode(1)
    headA2.next = ListNode(9)
    headA2.next.next = ListNode(1)
    headA2.next.next.next = common2
    
    # Создаем список B: 3 -> common2
    headB2 = ListNode(3)
    headB2.next = common2
    
    result2 = solution.getIntersectionNode(headA2, headB2)
    assert result2 == common2, f"Тест 2 провален: ожидался узел с значением 2"
    print("Тест 2 пройден!")
    
    # Тест 3: Без пересечения
    headA3 = create_linked_list([2, 6, 4])
    headB3 = create_linked_list([1, 5])
    
    result3 = solution.getIntersectionNode(headA3, headB3)
    assert result3 is None, f"Тест 3 провален: ожидался None"
    print("Тест 3 пройден!")
    
    # Тест 4: Один список пуст
    result4 = solution.getIntersectionNode(None, headB3)
    assert result4 is None, f"Тест 4 провален: ожидался None"
    print("Тест 4 пройден!")
    
    # Тест 5: Оба списка пусты
    result5 = solution.getIntersectionNode(None, None)
    assert result5 is None, f"Тест 5 провален: ожидался None"
    print("Тест 5 пройден!")
    
    # Тест 6: Полное совпадение списков (пересекаются с начала)
    headA6 = create_linked_list([1, 2, 3, 4, 5])
    result6 = solution.getIntersectionNode(headA6, headA6)
    assert result6 == headA6, f"Тест 6 провален: ожидался первый узел"
    print("Тест 6 пройден!")
    
    print("\n🎉 Все тесты пройдены успешно!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Сложение двух чисел, представленных в виде связных списков,
        где старший разряд находится в начале списка.
        
        Алгоритмическая заметка:
        Существует элегантное решение через стеки (O(n) по времени и памяти)
        или через рекурсию. Однако математически это задача сложения чисел
        с обратным порядком разрядов.
        
        Альтернативный подход O(1) по памяти:
        Если бы числа были представлены в обратном порядке (как в классической
        задаче LeetCode 2), можно было бы выполнять сложение за один проход
        без доп. памяти. В данной формулировке (MSB first) без стека или
        реверса списков обойтись нельзя.
        
        Для решения за O(n) времени и O(n) памяти:
        1. Использовать стеки для хранения цифр обоих чисел
        2. Последовательно извлекать цифры и складывать с переносом
        3. Формировать результирующий список от младших разрядов к старшим
        
        Именованные алгоритмы: "Сложение чисел с прямым порядком разрядов"
        сводится к классическому сложению через реверс или стеки.
        """
        pass


# Тесты для проверки решения
def run_tests():
    solution = Solution()
    
    # Вспомогательная функция для создания списка из массива
    def create_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    # Вспомогательная функция для преобразования списка в массив
    def linked_list_to_array(head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    # Тест 1: Пример из условия [7,2,4,3] + [5,6,4] = [7,8,0,7]
    l1 = create_linked_list([7, 2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [7, 8, 0, 7], "Тест 1 провален"
    
    # Тест 2: [2,4,3] + [5,6,4] = [8,0,7]
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [8, 0, 7], "Тест 2 провален"
    
    # Тест 3: [0] + [0] = [0]
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [0], "Тест 3 провален"
    
    # Тест 4: Разная длина с переносом в старший разряд
    l1 = create_linked_list([9, 9, 9])
    l2 = create_linked_list([1])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [1, 0, 0, 0], "Тест 4 провален"
    
    # Тест 5: Один из списков больше другого
    l1 = create_linked_list([1, 2, 3, 4, 5])
    l2 = create_linked_list([5, 6, 7])
    result = solution.addTwoNumbers(l1, l2)
    assert linked_list_to_array(result) == [1, 8, 0, 1, 2], "Тест 5 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()
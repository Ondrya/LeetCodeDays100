from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Словарь для отображения исходных узлов на их копии
        old_to_new = {}
        
        # Первый проход: создаём все новые узлы и сохраняем соответствие
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next
        
        # Второй проход: устанавливаем next и random связи для новых узлов
        current = head
        while current:
            new_node = old_to_new[current]
            # Устанавливаем next
            if current.next:
                new_node.next = old_to_new[current.next]
            # Устанавливаем random
            if current.random:
                new_node.random = old_to_new[current.random]
            current = current.next
        
        # Возвращаем голову скопированного списка
        return old_to_new[head]


# Вспомогательная функция для создания списка из списка пар [val, random_index]
def create_linked_list(arr):
    """Создаёт связный список из представления [[val, random_index], ...]"""
    if not arr:
        return None
    
    # Создаём все узлы
    nodes = [Node(x[0]) for x in arr]
    
    # Устанавливаем next связи
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Устанавливаем random связи
    for i, (_, random_idx) in enumerate(arr):
        if random_idx is not None:
            nodes[i].random = nodes[random_idx]
    
    return nodes[0] if nodes else None


def list_to_representation(head):
    """Преобразует связный список обратно в представление [[val, random_index], ...]"""
    if not head:
        return []
    
    # Сначала собираем все узлы в список
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next
    
    # Создаём словарь для поиска индекса узла
    node_to_index = {node: i for i, node in enumerate(nodes)}
    
    # Формируем результат
    result = []
    for node in nodes:
        random_index = node_to_index[node.random] if node.random else None
        result.append([node.val, random_index])
    
    return result


# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1
    arr1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head1 = create_linked_list(arr1)
    copied1 = solution.copyRandomList(head1)
    result1 = list_to_representation(copied1)
    assert result1 == arr1, f"Тест 1 провален: {result1} != {arr1}"
    print("Тест 1 пройден!")
    
    # Тест 2
    arr2 = [[1, 1], [2, 1]]
    head2 = create_linked_list(arr2)
    copied2 = solution.copyRandomList(head2)
    result2 = list_to_representation(copied2)
    assert result2 == arr2, f"Тест 2 провален: {result2} != {arr2}"
    print("Тест 2 пройден!")
    
    # Тест 3
    arr3 = [[3, None], [3, 0], [3, None]]
    head3 = create_linked_list(arr3)
    copied3 = solution.copyRandomList(head3)
    result3 = list_to_representation(copied3)
    assert result3 == arr3, f"Тест 3 провален: {result3} != {arr3}"
    print("Тест 3 пройден!")
    
    # Тест 4: пустой список
    head4 = None
    copied4 = solution.copyRandomList(head4)
    assert copied4 is None, "Тест 4 провален: пустой список"
    print("Тест 4 пройден!")
    
    # Тест 5: один узел
    arr5 = [[42, None]]
    head5 = create_linked_list(arr5)
    copied5 = solution.copyRandomList(head5)
    result5 = list_to_representation(copied5)
    assert result5 == arr5, f"Тест 5 провален: {result5} != {arr5}"
    print("Тест 5 пройден!")
    
    print("\nВсе тесты пройдены!")


if __name__ == "__main__":
    run_tests()
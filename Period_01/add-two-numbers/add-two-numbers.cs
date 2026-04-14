/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        // Создаем фиктивный головной узел для упрощения кода (вернем dummyHead.next)
        ListNode dummyHead = new ListNode(0);
        ListNode current = dummyHead;
        int carry = 0; // перенос в следующий разряд
        
        // Проходим по обоим связным спискам, пока не обработаем все узлы и перенос не станет 0
        // Пример: l1 = [2,4,3] (число 342), l2 = [5,6,4] (число 465)
        while (l1 != null || l2 != null || carry != 0)
        {
            // Получаем текущие значения (0 если узел отсутствует)
            // Итерация 1: val1 = 2, val2 = 5
            // Итерация 2: val1 = 4, val2 = 6
            // Итерация 3: val1 = 3, val2 = 4
            int val1 = (l1 != null) ? l1.val : 0;
            int val2 = (l2 != null) ? l2.val : 0;
            
            // Вычисляем сумму с учетом переноса
            // Итерация 1: sum = 2 + 5 + 0 = 7
            // Итерация 2: sum = 4 + 6 + 0 = 10
            // Итерация 3: sum = 3 + 4 + 1 = 8
            int sum = val1 + val2 + carry;
            
            // Текущая цифра = sum % 10, новый перенос = sum / 10
            // Итерация 1: digit = 7, carry = 0
            // Итерация 2: digit = 0, carry = 1
            // Итерация 3: digit = 8, carry = 0
            int digit = sum % 10;
            carry = sum / 10;
            
            // Создаем новый узел с полученной цифрой и добавляем в результирующий список
            // Результат после каждой итерации: [7] -> [7,0] -> [7,0,8]
            current.next = new ListNode(digit);
            current = current.next;
            
            // Переходим к следующим узлам, если они существуют
            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
        }
        
        // Возвращаем фактический результат (пропускаем фиктивный головной узел)
        // Конечный результат: [7,0,8] что представляет число 807 (342 + 465)
        return dummyHead.next;
    }
}
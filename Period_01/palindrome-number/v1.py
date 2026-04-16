# https://leetcode.com/problems/palindrome-number/submissions/1979763909/

'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        return str(x) == str(x)[::-1]


# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: Положительное число-палиндром
    assert solution.isPalindrome(121) == True, "Тест 1 провален"
    
    # Тест 2: Положительное число-не палиндром
    assert solution.isPalindrome(123) == False, "Тест 2 провален"
    
    # Тест 3: Отрицательное число (не может быть палиндромом из-за знака минус)
    assert solution.isPalindrome(-121) == False, "Тест 3 провален"
    
    # Тест 4: Ноль (палиндром)
    assert solution.isPalindrome(0) == True, "Тест 4 провален"
    
    # Тест 5: Однозначное число (все однозначные числа - палиндромы)
    assert solution.isPalindrome(5) == True, "Тест 5 провален"
    
    # Тест 6: Число с одинаковыми цифрами
    assert solution.isPalindrome(11) == True, "Тест 6 провален"
    
    # Тест 7: Четное количество цифр - палиндром
    assert solution.isPalindrome(1221) == True, "Тест 7 провален"
    
    # Тест 8: Четное количество цифр - не палиндром
    assert solution.isPalindrome(1234) == False, "Тест 8 провален"
    
    # Тест 9: Большое число-палиндром
    assert solution.isPalindrome(123454321) == True, "Тест 9 провален"
    
    # Тест 10: Число, заканчивающееся на 0 (кроме самого 0)
    assert solution.isPalindrome(10) == False, "Тест 10 провален"
    
    print("Все тесты пройдены успешно!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()
from typing import List

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Базовый случай
        if n == 0:
            return 1.0
        
        # Обработка отрицательной степени
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        
        # Простое линейное умножение n раз
        for _ in range(n):
            result *= x
        
        return result


# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: положительная степень
    assert abs(solution.myPow(2.00000, 10) - 1024.00000) < 1e-5, "Тест 1 провален"
    
    # Тест 2: дробное основание
    assert abs(solution.myPow(2.10000, 3) - 9.26100) < 1e-5, "Тест 2 провален"
    
    # Тест 3: отрицательная степень
    assert abs(solution.myPow(2.00000, -2) - 0.25000) < 1e-5, "Тест 3 провален"
    
    # Тест 4: n = 0
    assert abs(solution.myPow(5.00000, 0) - 1.00000) < 1e-5, "Тест 4 провален"
    
    # Тест 5: x = 0
    assert abs(solution.myPow(0.00000, 5) - 0.00000) < 1e-5, "Тест 5 провален"
    
    # Тест 6: отрицательное основание
    assert abs(solution.myPow(-2.00000, 3) - (-8.00000)) < 1e-5, "Тест 6 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()
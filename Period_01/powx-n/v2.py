from typing import List

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # БИНАРНОЕ РЕШЕНИЕ (оптимальное)
        if n == 0:
            return 1.0
        
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        current_product = x
        
        while n > 0:
            if n & 1:
                result *= current_product
            current_product *= current_product
            n >>= 1
        
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

    # ТЕСТ 7: ПРОВАЛЬНЫЙ ТЕСТ ДЛЯ ЛИНЕЙНОГО РЕШЕНИЯ
    # Очень маленькое x и максимальное n
    # Линейное решение будет выполнять 2,147,483,647 итераций
    # Это гарантированно вызовет Time Limit Exceeded UPD - не вызвало
    result = solution.myPow(0.00001, 2147483647)
    # Ожидаемый результат: очень маленькое положительное число (стремится к 0)
    assert result >= 0, "Тест 7 провален"

    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()
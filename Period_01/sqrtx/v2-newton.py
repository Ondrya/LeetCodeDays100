from typing import List

# ПО АЛГОРИТМУ НЬЮТОНА
class Solution:
    def mySqrt(self, x: int) -> int:
        
        # краеаое условие
        if x < 2:
            return x
        
        # Метод Ньютона (метод касательных)
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        
        return r

# Тесты
def run_tests():
    solution = Solution()
    
    # Тест 1: x = 4 (полный квадрат)
    assert solution.mySqrt(4) == 2, "Тест 1 провален"
    
    # Тест 2: x = 8 (не полный квадрат)
    assert solution.mySqrt(8) == 2, "Тест 2 провален"
    
    # Тест 3: x = 0
    assert solution.mySqrt(0) == 0, "Тест 3 провален"
    
    # Тест 4: x = 1
    assert solution.mySqrt(1) == 1, "Тест 4 провален"
    
    # Тест 5: x = 16 (полный квадрат)
    assert solution.mySqrt(16) == 4, "Тест 5 провален"
    
    # Тест 6: x = 9 (полный квадрат)
    assert solution.mySqrt(9) == 3, "Тест 6 провален"
    
    # Тест 7: x = 15 (ближайший меньший квадрат)
    assert solution.mySqrt(15) == 3, "Тест 7 провален"
    
    # Тест 8: x = 2
    assert solution.mySqrt(2) == 1, "Тест 8 провален"
    
    # Тест 9: x = 2147395600 (максимальное значение)
    assert solution.mySqrt(2147395600) == 46340, "Тест 9 провален"
    
    print("Все тесты пройдены!")


# Запуск тестов
if __name__ == "__main__":
    run_tests()
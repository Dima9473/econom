from calculator import (
    SumCalculator,
    square_function,
    cube_function,
    inverse_square_function,
    quadratic_linear_function,
)

print("Hello,2 World!")

# Создаем экземпляр калькулятора для диапазона от 1 до 3
calculator = SumCalculator(start_value=1, end_value=3)

# Вычисляем сумму квадратов, передавая функцию square_function
result = calculator.calculate_sum(square_function)

# Выводим результат суммы квадратов
print(f"\nИтоговая сумма k^2 для k от 1 до 3: {result}")

# Пример с функцией 1/k^2
print("\nПример с функцией 1/k^2:")
calculator_inverse = SumCalculator(start_value=1, end_value=5)
result_inverse = calculator_inverse.calculate_sum(inverse_square_function)
print(f"Итоговая сумма 1/k^2 для k от 1 до 5: {result_inverse:.6f}")

# Пример с функцией (2k + k^2)
print("\nПример с функцией (2k + k^2):")
calculator_quadratic = SumCalculator(start_value=1, end_value=4)
result_quadratic = calculator_quadratic.calculate_sum(quadratic_linear_function)
print(f"Итоговая сумма (2k + k^2) для k от 1 до 4: {result_quadratic}")

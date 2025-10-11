"""
Класс для расчета суммы с настраиваемыми параметрами и функциями
"""


class SumCalculator:
    """
    Класс для расчета суммы значений функции на заданном диапазоне
    """

    def __init__(self, start_value: int, end_value: int):
        """
        Инициализация калькулятора

        Args:
            start_value (int): Начальное значение диапазона
            end_value (int): Конечное значение диапазона (включительно)
        """
        self.start_value = start_value
        self.end_value = end_value
        self.result = 0

    def calculate_sum(self, calculation_function):
        """
        Вычисляет сумму значений функции на заданном диапазоне

        Args:
            calculation_function: Функция, которая принимает один аргумент и возвращает значение

        Returns:
            float: Сумма всех значений функции на диапазоне
        """
        self.result = 0

        for k in range(self.start_value, self.end_value + 1):
            value = calculation_function(k)
            self.result += value

        return self.result

    def get_result(self):
        """
        Возвращает последний вычисленный результат

        Returns:
            float: Результат последнего вычисления
        """
        return self.result

    def reset(self):
        """Сбрасывает результат в ноль"""
        self.result = 0


# Примеры функций для использования с калькулятором
def square_function(x):
    """Функция для вычисления квадрата числа"""
    return x**2


def cube_function(x):
    """Функция для вычисления куба числа"""
    return x**3


def linear_function(x):
    """Линейная функция"""
    return 2 * x + 1


def inverse_square_function(x):
    """Функция для вычисления 1/k^2"""
    if x == 0:
        raise ValueError("Деление на ноль: k не может быть равно 0")
    return 1 / (x**2)


def quadratic_linear_function(x):
    """Функция для вычисления (2k + k^2)"""
    return 2 * x + x**2

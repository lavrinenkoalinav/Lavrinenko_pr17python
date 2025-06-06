from calendar_tools import UkrainianCalendar
from math_utils import Calculator
from text_analysis import TextStats
from datetime import datetime

def show_calendar_module():
    cal = UkrainianCalendar()
    print("Свята:", cal.get_holiday_list())
    today = datetime.now().date()
    print(f"Сьогодні ({today}) — робочий день?:", cal.is_working_day(today))

def calculator_menu():
    calc = Calculator()
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    print("Операції: add, subtract, multiply, divide")
    op = input("Оберіть операцію: ")

    operations = {
        "add": calc.add,
        "subtract": calc.subtract,
        "multiply": calc.multiply,
        "divide": calc.divide
    }

    if op in operations:
        result = operations[op](a, b)
        print("Результат:", result)
    else:
        print("Невідома операція")

def text_analysis():
    text = input("Введіть текст: ")
    stats = TextStats(text)
    print("Кількість слів:", stats.count_words())
    letter, count = stats.most_common_letter()
    print(f"Найчастіша літера: '{letter}' з кількістю {count}")

# Демонстрація всіх модулів
print("=== Модуль календаря ===")
show_calendar_module()

print("\n=== Модуль калькулятора ===")
calculator_menu()

print("\n=== Модуль аналізу тексту ===")
text_analysis()

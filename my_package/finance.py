"""Модуль для финансовых расчетов."""

from decimal import Decimal, getcontext


def deposit_calculator():
    """Рассчитывает итоговую сумму вклада с капитализацией.
    
    Returns:
        tuple: (итоговая сумма, прибыль)
    """
    print("\n=== Задание 6 ===")
    
    getcontext().prec = 10
    
    print("Введите параметры вклада:")
    initial_amount = Decimal(input("Начальная сумма вклада (руб.): "))
    interest_rate = Decimal(input("Годовая процентная ставка (%): "))
    years = Decimal(input("Срок вклада (лет): "))
    
    monthly_rate = interest_rate / (12 * 100)
    months = years * 12
    final_amount = initial_amount * (1 + monthly_rate) ** months
    
    final_amount = final_amount.quantize(Decimal('0.01'))
    profit = final_amount - initial_amount
    
    print("\nРезультаты расчета:")
    print(f"Начальная сумма: {initial_amount} руб.")
    print(f"Процентная ставка: {interest_rate}% годовых")
    print(f"Срок вклада: {years} лет")
    print(f"Итоговая сумма: {final_amount} руб.")
    print(f"Общая прибыль: {profit} руб.")
    
    return final_amount, profit


def task6():
    """Пример расчета вклада с предустановленными значениями.
    
    Returns:
        tuple: (итоговая сумма, прибыль)
    """
    print("Пример расчета вклада:")

    initial_amount = Decimal('200000.50')  
    interest_rate = Decimal('7.5')         
    years = Decimal('3')                   
    
    getcontext().prec = 10
    monthly_rate = interest_rate / (12 * 100)
    months = years * 12
    final_amount = initial_amount * (1 + monthly_rate) ** months
    final_amount = final_amount.quantize(Decimal('0.01'))
    profit = final_amount - initial_amount
    
    print(f"Начальная сумма: {initial_amount} руб.")
    print(f"Процентная ставка: {interest_rate}% годовых")
    print(f"Срок вклада: {years} лет")
    print(f"Итоговая сумма: {final_amount} руб.")
    print(f"Общая прибыль: {profit} руб.")
    
    return final_amount, profit
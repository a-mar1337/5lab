"""Модуль с различными задачами для работы с данными."""

from datetime import datetime, date


def task1():
    """Генерирует список квадратов чисел от 1 до 10.
    
    Returns:
        list: Список квадратов чисел
    """
    squares = [x**2 for x in range(1, 11)]
    print("Квадраты чисел от 1 до 10:", squares)
    return squares


def task2():
    """Генерирует список четных чисел от 1 до 19.
    
    Returns:
        list: Список четных чисел
    """
    even_numbers = [x for x in range(1, 20) if x % 2 == 0]
    print("Четные числа от 1 до 19:", even_numbers)
    return even_numbers


def task3():
    """Фильтрует слова длиннее 3 символов и переводит в верхний регистр.
    
    Returns:
        list: Отфильтрованный список слов
    """
    words = ["python", "Java", "c++", "Rust", "go"]
    filtered_words = [word.upper() for word in words if len(word) > 3]
    print("Исходный список:", words)
    print("Слова в верхнем регистре длиннее 3 символов:", filtered_words)
    return filtered_words


class Countdown:
    """Класс для обратного отсчета."""
    
    def __init__(self, n):
        """Инициализирует отсчет с числа n.
        
        Args:
            n (int): Начальное число отсчета
        """
        self.n = n
        self.current = n
    
    def __iter__(self):
        """Возвращает итератор."""
        return self
    
    def __next__(self):
        """Возвращает следующее число в отсчете.
        
        Returns:
            int: Следующее число
            
        Raises:
            StopIteration: Когда отсчет завершен
        """
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


def task4():
    """Демонстрирует обратный отсчет от 6 до 1."""
    print("Обратный отсчет от 5:")
    for x in Countdown(6):
        print(x, end=" ")
    print()


def fibonacci(n):
    """Генерирует последовательность Фибоначчи.
    
    Args:
        n (int): Количество чисел для генерации
        
    Yields:
        int: Следующее число Фибоначчи
    """
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def task5():
    """Выводит первые 5 чисел последовательности Фибоначчи."""
    print("Первые 5 чисел Фибоначчи:")
    for num in fibonacci(5):
        print(num, end=" ")
    print()


def task7():
    """Демонстрирует операции с дробями."""
    from fractions import Fraction
    
    frac1 = Fraction(3, 4)
    frac2 = Fraction(5, 6)
    
    print(f"Дробь 1: {frac1}")
    print(f"Дробь 2: {frac2}")
    
    addition = frac1 + frac2
    subtraction = frac1 - frac2
    multiplication = frac1 * frac2
    division = frac1 / frac2
    
    print("\nРезультаты операций:")
    print(f"Сложение: {frac1} + {frac2} = {addition}")
    print(f"Вычитание: {frac1} - {frac2} = {subtraction}")
    print(f"Умножение: {frac1} * {frac2} = {multiplication}")
    print(f"Деление: {frac1} / {frac2} = {division}")


def task8():
    """Выводит текущую дату и время в различных форматах.
    
    Returns:
        datetime: Текущая дата и время
    """
    t = datetime.now()
    
    print("Текущая дата и время:")
    print(f"Полная дата и время: {t}")
    print(f"Только дата: {t.date()}")
    print(f"Только время: {t.time()}")
    
    print("\nАльтернативные форматы:")
    print(f"Дата (ISO формат): {t.date().isoformat()}")
    print(f"Время (ISO формат): {t.time().isoformat('seconds')}")
    
    return t


def task9():
    """Рассчитывает дни с рождения и до следующего дня рождения.
    
    Returns:
        tuple: (дней прошло, дней до следующего дня рождения)
    """
    birth_date = date(2005, 6, 17) 
    
    today = date.today()
    
    days_passed = (today - birth_date).days
    
    next_birthday = date(today.year, birth_date.month, birth_date.day)
    
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)

    days_to_birthday = (next_birthday - today).days

    print(f"Дата рождения: {birth_date}")
    print(f"Сегодняшняя дата: {today}")
    print(f"Дней прошло с рождения: {days_passed} дней")
    print(f"Следующий день рождения: {next_birthday}")
    print(f"Дней до следующего дня рождения: {days_to_birthday} дней")
    return days_passed, days_to_birthday


def format_datetime(dt):
    """Форматирует дату и время в читаемый вид.
    
    Args:
        dt (datetime): Дата и время для форматирования
        
    Returns:
        str: Отформатированная строка
    """
    months = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля",
        5: "мая", 6: "июня", 7: "июля", 8: "августа",
        9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    }
    
    time_str = dt.strftime("%H:%M")
    
    return f"Сегодня {dt.day} {months[dt.month]} {dt.year} года, время: {time_str}"


def task10():
    """Выводит текущую дату и время в читаемом формате.
    
    Returns:
        str: Отформатированная строка с датой и временем
    """
    now = datetime.now()
    formatted = format_datetime(now)
    print("Текущая дата и время:")
    print(formatted)
    return formatted
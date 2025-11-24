Примеры использования
=====================

Запуск через командную строку
-----------------------------

.. code-block:: bash

   # Квадраты чисел от 1 до 10
   python main.py 1

   # Четные числа от 1 до 19
   python main.py 2

   # Фильтрация слов
   python main.py 3

   # Обратный отсчет
   python main.py 4

   # Числа Фибоначчи
   python main.py 5

   # Расчет вклада
   python main.py 6

   # Операции с дробями
   python main.py 7

   # Текущая дата и время
   python main.py 8

   # Расчет дней до дня рождения
   python main.py 9

   # Форматированная дата
   python main.py 10

Примеры кода
------------

Генерация списков
~~~~~~~~~~~~~~~~~

.. code-block:: python

   from my_package.tasks import task1, task2, task3

   # Квадраты чисел
   squares = task1()

   # Четные числа
   even_numbers = task2()

   # Фильтрация слов
   words = task3()

Работа с последовательностями
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from my_package.tasks import Countdown, fibonacci

   # Обратный отсчет
   for number in Countdown(5):
       print(number)

   # Числа Фибоначчи
   for fib_num in fibonacci(10):
       print(fib_num)

Финансовые расчеты
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from my_package.finance import task6, deposit_calculator

   # Пример расчета
   final_amount, profit = task6()

   # Интерактивный расчет
   # final_amount, profit = deposit_calculator()

Работа с датами
~~~~~~~~~~~~~~~

.. code-block:: python

   from my_package.tasks import task8, task9, task10

   # Текущая дата
   current_time = task8()

   # Дни до дня рождения
   days_passed, days_left = task9()

   # Форматированная дата
   formatted_date = task10()

Проверка документации
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Просмотр докстрингов
   from my_package.tasks import task1
   help(task1)

   from my_package.tasks import Countdown
   help(Countdown)
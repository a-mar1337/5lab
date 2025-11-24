"""Основной модуль приложения.

Предоставляет консольный интерфейс для запуска различных задач.
"""

import argparse
from my_package import tasks
from my_package import finance


def main():
    """Основная функция приложения."""
    parser = argparse.ArgumentParser(description="Запуск различных задач")
    
    parser.add_argument('task', type=int, choices=range(1, 11), 
                       help='Номер задачи от 1 до 10')
    
    args = parser.parse_args()
    
    task_functions = {
        1: tasks.task1,
        2: tasks.task2,
        3: tasks.task3,
        4: tasks.task4,
        5: tasks.task5,
        6: finance.task6,
        7: tasks.task7,
        8: tasks.task8,
        9: tasks.task9,
        10: tasks.task10
    }
    
    if args.task in task_functions:
        print(f"\n=== Задача {args.task} ===")
        task_functions[args.task]()
    else:
        print("Задача не найдена")


if __name__ == "__main__":
    main()
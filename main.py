import argparse
from my_project.data_loader import load_data, save_data
from my_project.calculator import Calculator, calculate_average


def main():
    parser = argparse.ArgumentParser(description="Обработка данных и вычисления")
    
    subparsers = parser.add_subparsers(dest='command')
    
    load_parser = subparsers.add_parser('load')
    load_parser.add_argument('filename')
    
    calc_parser = subparsers.add_parser('calc')
    calc_parser.add_argument('--numbers', nargs='+', type=float)
    
    args = parser.parse_args()
    
    if args.command == 'load':
        try:
            data = load_data(args.filename)
            print(f"Загружено {len(data)} записей")
        except Exception as e:
            print(f"Ошибка: {e}")
    
    elif args.command == 'calc':
        if args.numbers:
            try:
                avg = calculate_average(args.numbers)
                print(f"Среднее: {avg}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        else:
            calc = Calculator()
            result = calc.add(10, 5)
            print(f"10 + 5 = {result}")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
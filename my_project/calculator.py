class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a: float, b: float) -> float:
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def get_history(self) -> list:
        return self.history.copy()


def calculate_average(numbers: list) -> float:
    if not numbers:
        raise ValueError("Список чисел не может быть пустым")
    return sum(numbers) / len(numbers)
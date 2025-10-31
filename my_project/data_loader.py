import json
from typing import List, Dict, Any


def load_data(filename: str) -> List[Dict[str, Any]]:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {filename} не найден")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Ошибка декодирования JSON: {e}", e.doc, e.pos)


def save_data(data: List[Dict[str, Any]], filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
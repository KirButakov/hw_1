import json
import os

from custom_logger import logger


def load_transactions_from_json():
    """
    Загружает данные о финансовых транзакциях из JSON-файла.

    Returns:
        list: Список словарей с данными о финансовых транзакциях.
              Возвращает пустой список, если файл не найден, пустой, содержит не список
              или не удалось корректно загрузить данные из файла.
    """
    file_path = "data/operations.json"  # Путь к файлу в директории data

    # Проверяем существование файла
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return []

    try:
        # Открываем файл и пытаемся загрузить данные
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                # Проверяем тип данных и их структуру
                if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                    # Проверяем, что список данных не пустой
                    if len(data) > 0:
                        return data
                    else:
                        print(f"File is empty: {file_path}")
                        return []
                else:
                    print(f"File does not contain a list of dictionaries: {file_path}")
                    return []
            except json.JSONDecodeError:
                print(f"Error decoding JSON from file: {file_path}")
                return []
    except IOError:
        print(f"Error reading file: {file_path}")
        return []


def read_csv_file(file_path):
    logger.info(f"Reading CSV file from {file_path}")

    return []

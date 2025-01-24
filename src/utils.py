import json
import os

from custom_logger import logger


def load_transactions_from_json(file_path):
    """
    Загружает данные о финансовых транзакциях из JSON-файла.

    Args:
        file_path (str): Путь к JSON-файлу.

    Returns:
        list: Список словарей с данными о финансовых транзакциях.
              Возвращает пустой список, если файл не найден, пустой, содержит не список
              или не удалось корректно загрузить данные из файла.
    """
    # Проверяем существование файла
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
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
                        logger.info(f"Successfully loaded transactions from {file_path}")
                        return data
                    else:
                        logger.warning(f"File is empty: {file_path}")
                        return []
                else:
                    logger.error(f"File does not contain a list of dictionaries: {file_path}")
                    return []
            except json.JSONDecodeError:
                logger.error(f"Error decoding JSON from file: {file_path}")
                return []
    except IOError:
        logger.error(f"Error reading file: {file_path}")
        return []


def read_csv_file(file_path):
    """
    Читает данные из CSV-файла.

    Args:
        file_path (str): Путь к CSV-файлу.

    Returns:
        list: Список данных, прочитанных из CSV-файла.
    """
    logger.info(f"Reading CSV file from {file_path}")

    # Тут должна быть логика чтения CSV-файла

    logger.info(f"Successfully read CSV file from {file_path}")
    return []

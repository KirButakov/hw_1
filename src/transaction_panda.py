import logging
import os

import pandas as pd

# Убедимся, что директория для логов существует
log_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Настройка логирования
log_file = os.path.join(log_directory, "utils.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_file, mode="w"), logging.StreamHandler()],  # Перезапись файла при каждом запуске
)

logger = logging.getLogger(__name__)


def read_csv_file(file_path, delimiter=";"):
    """
    Читает CSV файл и возвращает список словарей с данными.

    Parameters:
    file_path (str): Путь к CSV файлу.
    delimiter (str): Разделитель, используемый в CSV файле.

    Returns:
    list: Список словарей с данными из CSV файла.
    """
    logger.info(f"Reading CSV file from {file_path} with delimiter '{delimiter}'")
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        transactions = df.to_dict(orient="records")
        logger.info(f"Successfully read {len(transactions)} transactions from CSV file")
        return transactions
    except Exception as e:
        logger.error(f"Error reading CSV file: {e}")
        return None

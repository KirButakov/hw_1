import os
import sys

# Добавление пути к src в sys.path для корректных импортов
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import time

from custom_logger import logger
from src.masks import example_function
from src.utils import read_csv_file

if __name__ == "__main__":
    logger.info("Script started")

    # Путь к папке data относительно текущего файла
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))
    csv_file_path = os.path.join(base_path, "transactions.csv")
    xlsx_file_path = os.path.join(base_path, "transactions_excel.xlsx")
    sheet_name = "Transactions"

    # Чтение данных из CSV файла
    transactions_csv = read_csv_file(csv_file_path)

    # Пример вызова функции из masks
    example_function()

    logger.info("Script finished")

    # Принудительная запись логов
    logger.handlers[0].flush()

    # Задержка, чтобы увидеть логи
    time.sleep(1)

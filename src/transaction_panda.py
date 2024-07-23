import os

import pandas as pd


def read_csv_file(file_path, delimiter=";"):
    """
    Читает CSV файл и возвращает список словарей с данными.

    Parameters:
    file_path (str): Путь к CSV файлу.
    delimiter (str): Разделитель, используемый в CSV файле.

    Returns:
    list: Список словарей с данными из CSV файла.
    """
    try:
        df = pd.read_csv(file_path, delimiter=delimiter)
        transactions = df.to_dict(orient="records")
        print("CSV File Data:")
        print(transactions[:5])
        return transactions
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None


def read_excel_file(file_path, sheet_name, delimiter=";"):
    """
    Читает Excel файл и возвращает список словарей с данными.

    Parameters:
    file_path (str): Путь к Excel файлу.
    sheet_name (str): Название листа, откуда будут читаться данные.
    delimiter (str): Разделитель, используемый в данных листа.

    Returns:
    list: Список словарей с данными из Excel файла.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        df = df.iloc[:, 0].str.split(delimiter, expand=True)
        df.columns = ["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"]
        transactions = df.to_dict(orient="records")
        print("Excel File Data:")
        print(transactions[:5])
        return transactions
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None


if __name__ == "__main__":
    """
    Главная функция, которая выполняется при запуске скрипта.

    Читает данные из файлов CSV и XLSX и выводит первые 5 записей.
    """
    # Путь к папке data относительно текущего файла
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
    csv_file_path = os.path.join(base_path, "transactions.csv")
    xlsx_file_path = os.path.join(base_path, "transactions_excel.xlsx")
    sheet_name = "Transactions"

    # Чтение данных из CSV файла
    transactions_csv = read_csv_file(csv_file_path)

    # Чтение данных из Excel файла
    transactions_excel = read_excel_file(xlsx_file_path, sheet_name)

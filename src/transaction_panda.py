import os

import pandas as pd


def read_csv_file(file_path):
    """
    Читает CSV файл и возвращает DataFrame.

    Parameters:
    file_path (str): Путь к CSV файлу.

    Returns:
    pd.DataFrame: DataFrame с данными из CSV файла.
    """
    try:
        df = pd.read_csv(file_path)
        print("CSV File Data:")
        print(df.head())
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None


def write_to_excel(df, excel_file_path, sheet_name):
    """
    Записывает DataFrame в Excel файл.

    Parameters:
    df (pd.DataFrame): DataFrame с данными для записи.
    excel_file_path (str): Путь к Excel файлу.
    sheet_name (str): Название листа, куда будут записаны данные.
    """
    try:
        with pd.ExcelWriter(excel_file_path, engine="openpyxl", mode="a") as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        print(f"Data written to {sheet_name} in {excel_file_path}")
    except Exception as e:
        print(f"Error writing to Excel file: {e}")


if __name__ == "__main__":
    """
    Главная функция, которая выполняется при запуске скрипта.

    Читает данные из файла CSV и записывает их в файл XLSX.
    """
    # Путь к папке data относительно текущего файла
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
    csv_file_path = os.path.join(base_path, "transactions.csv")
    xlsx_file_path = os.path.join(base_path, "transactions_excel.xlsx")
    sheet_name = "Transactions"

    # Чтение данных из CSV файла
    df_csv = read_csv_file(csv_file_path)

    if df_csv is not None:
        # Запись данных в Excel файл
        write_to_excel(df_csv, xlsx_file_path, sheet_name)

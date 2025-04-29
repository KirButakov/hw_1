import json
import os
from collections import Counter
from processing import sort_by_date
from homework_13_2 import filter_transactions_by_description, filter_transactions_by_status

def count_transactions_by_type(transactions, transaction_type):
    """
    Функция для подсчета количества банковских операций определенного типа.
    """
    counter = Counter(
        transaction["type"] for transaction in transactions if transaction.get("type") == transaction_type
    )
    return dict(counter)

def load_transactions_from_json(file_path):
    """Загрузка транзакций из JSON-файла"""
    with open(file_path, "r") as file:
        return json.load(file)

def read_csv_file(file_path):
    """Чтение транзакций из CSV-файла"""
    import pandas as pd
    return pd.read_csv(file_path).to_dict(orient='records')

def get_transactions_from_xlsx(file_path):
    """Чтение транзакций из XLSX-файла"""
    import pandas as pd
    return pd.read_excel(file_path).to_dict(orient='records')

def main():
    """
    Основная функция программы для работы с банковскими транзакциями.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("\nПользователь: ")

    # Выбор типа файла и загрузка данных
    if choice == "1":
        file_path = os.path.join("data", "operations.json")
        transactions = load_transactions_from_json(file_path)
    elif choice == "2":
        file_path = os.path.join("data", "operations.csv")
        transactions = read_csv_file(file_path)
    elif choice == "3":
        file_path = os.path.join("data", "operations.xlsx")
        transactions = get_transactions_from_xlsx(file_path)
    else:
        print("Некорректный выбор.")
        return

    if not transactions:
        print("Не удалось загрузить транзакции.")
        return

    # Выбор статуса
    statuses = ["EXECUTED", "CANCELED", "PENDING"]
    status = input(
        "\nВведите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтрации статусы: EXECUTED, CANCELED, PENDING\nПользователь: "
    ).upper()

    while status not in statuses:
        print(f'Статус операции "{status}" недоступен.')
        status = input("Введите корректный статус: ").upper()

    filtered_transactions = filter_transactions_by_status(transactions, status)
    print(f'Операции отфильтрованы по статусу "{status}"')

    # Сортировка
    print("\nПрограмма: Отсортировать операции по дате? Да/Нет")
    sort_by_date_flag = input("Пользователь: ").lower() == "да"

    if sort_by_date_flag:
        print("Программа: Отсортировать по возрастанию или по убыванию?")
        sort_order = input("Пользователь: ").lower()
        if sort_order == "по возрастанию":
            filtered_transactions = sort_by_date(filtered_transactions, ascending=True)
        elif sort_order == "по убыванию":
            filtered_transactions = sort_by_date(filtered_transactions, ascending=False)
        else:
            print("Некорректный выбор сортировки.")

    # Фильтрация по валюте
    print("\nПрограмма: Выводить только рублевые транзакции? Да/Нет")
    filter_rub = input("Пользователь: ").lower() == "да"

    if filter_rub:
        filtered_transactions = [t for t in filtered_transactions if t.get("currency") == "RUB"]

    # Фильтрация по описанию
    print("\nПрограмма: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    filter_description = input("Пользователь: ").lower() == "да"

    if filter_description:
        keyword = input("Введите ключевое слово для фильтрации по описанию: ")
        filtered_transactions = filter_transactions_by_description(filtered_transactions, keyword)

    # Вывод результатов
    if filtered_transactions:
        print("\nПрограмма: Распечатываю итоговый список транзакций...")
        for transaction in filtered_transactions:
            print(transaction)
        print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}")
    else:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

if __name__ == "__main__":
    main()

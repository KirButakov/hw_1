import csv
import json
from collections import Counter

import openpyxl

from processing import filter_by_state


def get_transactions_from_json():
    """
    Функция для обработки JSON-файла с транзакциями.
    """
    with open("transactions.json", "r") as file:
        transactions = json.load(file)
    print("Для обработки выбран JSON-файл.")
    return transactions


def get_transactions_from_csv():
    """
    Функция для обработки CSV-файла с транзакциями.
    """
    transactions = []
    with open("transactions.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    print("Для обработки выбран CSV-файл.")
    return transactions


def get_transactions_from_xlsx():
    """
    Функция для обработки XLSX-файла с транзакциями.
    """
    workbook = openpyxl.load_workbook("transactions.xlsx")
    sheet = workbook.active
    transactions = []

    headers = [cell.value for cell in sheet[1]]

    for row in sheet.iter_rows(min_row=2, values_only=True):
        transaction = {headers[i]: row[i] for i in range(len(headers))}
        transactions.append(transaction)
    print("Для обработки выбран XLSX-файл.")
    return transactions


def count_transactions_by_type(transactions, transaction_type):
    """
    Функция для подсчета количества банковских операций определенного типа.
    """
    counter = Counter(
        transaction["type"] for transaction in transactions if transaction.get("type") == transaction_type
    )
    return dict(counter)


def main():
    """
    Основная функция программы для работы с банковскими транзакциями.
    Программа приветствует пользователя, предлагает выбрать тип файла для обработки
    и выполняет последующую фильтрацию и сортировку транзакций по заданным параметрам.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("\nПользователь: ")

    if choice == "1":
        transactions = get_transactions_from_json()
    elif choice == "2":
        transactions = get_transactions_from_csv()
    elif choice == "3":
        transactions = get_transactions_from_xlsx()
    else:
        print("Некорректный выбор.")
        return

    statuses = ["EXECUTED", "CANCELED", "PENDING"]
    status = input(
        "\nВведите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь: "
    ).upper()

    while status not in statuses:
        print(f'Статус операции "{status}" недоступен.')
        status = input("Введите корректный статус: ").upper()

    filtered_transactions = filter_by_state(transactions, status)
    print(f'Операции отфильтрованы по статусу "{status}"')

    print("\nПрограмма: Отсортировать операции по дате? Да/Нет")
    sort_by_date = input("Пользователь: ").lower() == "да"

    if sort_by_date:
        print("Программа: Отсортировать по возрастанию или по убыванию?")
        sort_order = input("Пользователь: ").lower()
        if sort_order == "по возрастанию":
            filtered_transactions.sort(key=lambda x: x["date"])
        elif sort_order == "по убыванию":
            filtered_transactions.sort(key=lambda x: x["date"], reverse=True)
        else:
            print("Некорректный выбор сортировки.")

    print("\nПрограмма: Выводить только рублевые транзакции? Да/Нет")
    filter_rub = input("Пользователь: ").lower() == "да"

    if filter_rub:
        filtered_transactions = [t for t in filtered_transactions if t.get("currency") == "RUB"]

    print("\nПрограмма: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    filter_description = input("Пользователь: ").lower() == "да"

    if filter_description:
        keyword = input("Введите ключевое слово для фильтрации по описанию: ")
        filtered_transactions = [t for t in filtered_transactions if keyword in t.get("description", "")]

    if filtered_transactions:
        print("\nПрограмма: Распечатываю итоговый список транзакций...")
        for transaction in filtered_transactions:
            print(transaction)
        print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}")
    else:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()

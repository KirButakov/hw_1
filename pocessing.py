from datetime import datetime
from typing import List, Dict


# Первая функция.
def sort_key(entry: Dict[str, str]) -> str:
    """
    Функция для извлечения ключа 'date' из словаря.
    """
    return entry["date"]


def sort_by_date(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Сортирует список словарей по дате.


    data (List[Dict[str, str]]): Список словарей, которые нужно отсортировать.


    List[Dict[str, str]]: Отсортированный список словарей по дате.
    """
    return sorted(data, key=sort_key)


# Вторая функция.
def sort_transactions_by_date(
    transactions: List[Dict[str, str]], reverse_order: bool = True
) -> List[Dict[str, str]]:
    """
    Сортирует по дате.


    transactions (List[Dict[str, str]]): Список словарей.
    reverse_order (bool, ...): Порядок сортировки. Сортировка происходит по убыванию даты.


    List[Dict[str, str]]: Отсортированный список операций по дате.


    """

    # Функция для извлечения даты из словаря операции
    def get_date(transaction: Dict[str, str]) -> datetime:
        return datetime.fromisoformat(transaction["date"])

    # Сортировка по дате с использованием  функции
    sorted_transactions = sorted(transactions, key=get_date, reverse=reverse_order)

    return sorted_transactions

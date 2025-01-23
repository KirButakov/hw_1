import re
from collections import Counter

# Функция для фильтрации транзакций по описанию
def filter_transactions_by_description(transactions, search_string):
    """
    Функция фильтрует список словарей с данными о банковских операциях по заданной строке поиска в описании.

    transactions (list of dict): Список словарей с данными о банковских операциях. Каждый словарь должен содержать ключ 'description'.
    search_string (str): Строка для поиска в описаниях операций.

    list of dict: Список словарей операций, у которых в описании присутствует search_string.
    """
    filtered_transactions = []
    for transaction in transactions:
        if "description" in transaction:
            description = transaction["description"]
            if re.search(search_string, description, re.IGNORECASE):
                filtered_transactions.append(transaction)
    return filtered_transactions

# Функция для фильтрации транзакций по статусу
def filter_transactions_by_status(transactions, status):
    """
    Функция фильтрует список словарей с данными о банковских операциях по заданному статусу.

    transactions (list of dict): Список словарей с данными о банковских операциях. Каждый словарь должен содержать ключ 'state'.
    status (str): Статус для фильтрации. Статус будет приведен к верхнему регистру для сопоставления.

    list of dict: Список словарей операций, у которых статус совпадает с заданным.
    """
    status = status.upper()
    filtered_transactions = [transaction for transaction in transactions if transaction.get("state", "").upper() == status]
    return filtered_transactions

# Функция для подсчета операций по категориям
def count_operations_by_category(transactions, categories):
    """
    Подсчитывает количество операций в каждой категории на основе описаний транзакций.

    transactions (list of dict): Список словарей с данными о банковских операциях. Каждый словарь должен содержать ключ 'description'.
    categories (list of str): Список категорий, для которых нужно подсчитать операции. Каждая категория рассматривается как регулярное выражение.

    dict: Словарь с количеством операций для каждой категории.
    """
    # Создаем пустой Counter для подсчета категорий
    category_counts = Counter()

    for transaction in transactions:
        description = transaction.get("description", "")
        for category in categories:
            pattern = re.compile(category, re.IGNORECASE)
            if re.search(pattern, description):
                category_counts[category] += 1

    return dict(category_counts)

import re


# Первое задание
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


# Второе задание
def count_operations_by_category(transactions, categories):
    """
    Подсчитывает количество операций в каждой категории на основе описаний транзакций.


    - transactions (список словарей): Список словарей с данными о банковских операциях.
                                       Каждый словарь должен содержать поле 'description'.
    - categories (список строк): Список категорий, для которых нужно подсчитать операции.
                                 Каждая категория рассматривается как регулярное выражение.


    """

    category_counts = {category: 0 for category in categories}

    for transaction in transactions:
        description = transaction.get("description", "")
        for category in categories:
            pattern = re.compile(category, re.IGNORECASE)
            if re.search(pattern, description):
                category_counts[category] += 1

    return category_counts

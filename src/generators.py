def filter_by_currency(transactions, currency):
    """
    Фильтрует список транзакций по указанной валюте.

    Args:
        transactions (list of dict): Список транзакций, каждая транзакция представлена словарем.
        currency (str): Валюта, по которой нужно отфильтровать транзакции.

    Yields:
        dict: Транзакция, соответствующая указанной валюте.
    """
    for transaction in transactions:
        if transaction.get("currency") == currency:
            yield transaction


def transaction_descriptions(transactions):
    """
    Генерирует описания транзакций из списка транзакций.

    Args:
        transactions (list of dict): Список транзакций, каждая транзакция представлена словарем.

    Yields:
        str: Описание транзакции или "Нет описания", если описание отсутствует.
    """
    for transaction in transactions:
        yield transaction.get("description", "Нет описания")


def card_number_generator(start, end):
    """
    Генерирует номера банковских карт в заданном диапазоне.

    Args:
        start (int): Начальный номер диапазона.
        end (int): Конечный номер диапазона.

    Yields:
        str: Сформатированный номер банковской карты в виде строки.
    """
    for number in range(start, end + 1):
        card_number = f"{number:016d}"
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number

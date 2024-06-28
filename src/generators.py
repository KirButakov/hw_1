# Функция, которая принимает список словарей
def filter_by_currency(transactions, currency):
    for transaction in transactions:
        if transaction.get("currency") == currency:
            yield transaction


# Генератор, который принимает список словарей
def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction.get("description", "Нет описания")


# Генератор номеров банковских карт
def card_number_generator(start, end):
    for number in range(start, end + 1):
        card_number = f"{number:016d}"
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number

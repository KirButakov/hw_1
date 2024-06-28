from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_transaction_descriptions():
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
        {"amount": 1000},  # транзакция без описания
    ]

    descriptions = transaction_descriptions(transactions)

    for _ in range(5):
        print(next(descriptions))


def test_filter_by_currency():
    # Создаем объект-генератор, который будет выдавать транзакции
    def transaction_generator():
        yield {"number": 939719570, "amount": 100}
        yield {"number": 142264268, "amount": 200}
        yield {"number": 939719570, "amount": 150}
        yield {"amount": 500}  # транзакция без указания числа

    # Используем объект-генератор в качестве входных данных
    number = 939719570
    transactions_with_number = filter_by_currency(transaction_generator(), number)

    # Выводим первые несколько транзакций с заданным числом
    for _ in range(5):
        try:
            print(next(transactions_with_number))
        except StopIteration:
            print("Конец списка транзакций")


def test_card_number_generator(transactions_fixture):
    # Выводим номера карт, созданные с помощью генератора
    for card_number in card_number_generator(1, 5):
        print(card_number)

    # Проверяем наличие всех полей в транзакциях
    for transaction in transactions_fixture:
        assert "id" in transaction
        assert "state" in transaction
        assert "date" in transaction
        assert "operationAmount" in transaction
        assert "description" in transaction
        assert "from" in transaction
        assert "to" in transaction

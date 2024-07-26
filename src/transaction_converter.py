import os

from dotenv import load_dotenv

from src.external_api import fetch_exchange_rate

# Загрузка переменных окружения из .env файла
load_dotenv()


def convert_transaction_amount(transaction):
    """
    Конвертирует сумму транзакции в рубли.

    Если транзакция в валюте USD или EUR, конвертирует сумму в рубли
    по текущему обменному курсу, используя внешнее API.

    Args:
        transaction (dict): Словарь с ключами 'transaction'.
            'transaction' (dict): Словарь с ключами 'amount' и 'currency'.
                'amount' (float): Сумма транзакции.
                'currency' (str): Валюта транзакции ('USD', 'EUR', 'RUB').

    Returns:
        float: Сумма транзакции в рублях.

    Raises:
        ValueError: Если валюта не поддерживается или ключ API не установлен.
    """
    amount = transaction["transaction"]["amount"]
    currency = transaction["transaction"]["currency"]

    if currency == "RUB":
        return float(amount)
    elif currency == "USD" or currency == "EUR":
        # Получение курса валют из внешнего API
        api_key = os.getenv("API_ACCESS_KEY")
        if not api_key:
            raise ValueError("API access key is not set")

        exchange_rate = fetch_exchange_rate(api_key, currency)
        if currency == "USD":
            converted_amount = float(amount) * exchange_rate["USD_RUB"]
        else:  # currency == 'EUR'
            converted_amount = float(amount) * exchange_rate["EUR_RUB"]

        return converted_amount
    else:
        raise ValueError(f"Unsupported currency: {currency}")

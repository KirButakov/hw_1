import requests


def fetch_exchange_rate(api_key, base_currency):
    """
    Запрашивает текущие курсы валют для конвертации в рубли.

    Args:
        api_key (str): Ключ доступа к API.
        base_currency (str): Базовая валюта ('USD' или 'EUR').

    Returns:
        dict: Словарь с курсами обмена {'USD_RUB': float, 'EUR_RUB': float}.
            Значение курса для базовой валюты будет равно None, если не запрошено.

    Raises:
        requests.exceptions.RequestException: Если произошла ошибка при запросе.
    """
    endpoint = "https://api.apilayer.com/exchangerates_data/latest"
    headers = {"apikey": api_key}
    url = f"{endpoint}?base={base_currency}&symbols=RUB"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Выбрасывает исключение для кода ответа, указывающего на ошибку

        data = response.json()
        return {
            "USD_RUB": data["rates"]["RUB"] if base_currency == "USD" else None,
            "EUR_RUB": data["rates"]["RUB"] if base_currency == "EUR" else None,
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        raise

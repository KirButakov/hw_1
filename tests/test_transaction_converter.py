import unittest
from unittest.mock import patch

from src.transaction_converter import convert_transaction_amount


class TestConvertTransactionAmount(unittest.TestCase):
    """
    Тесты для функции convert_transaction_amount.
    """

    @patch("src.transaction_converter.fetch_exchange_rate")
    @patch("os.getenv")
    def test_convert_usd_to_rub(self, mock_getenv, mock_fetch_exchange_rate):
        """
        Проверяет конвертацию суммы из USD в RUB.
        """
        mock_getenv.return_value = "test_api_key"
        mock_fetch_exchange_rate.return_value = {"USD_RUB": 75.0}

        transaction = {"amount": 100, "currency": "USD"}
        converted_amount = convert_transaction_amount(transaction)

        self.assertEqual(converted_amount, 7500.0)

    @patch("src.transaction_converter.fetch_exchange_rate")
    @patch("os.getenv")
    def test_convert_eur_to_rub(self, mock_getenv, mock_fetch_exchange_rate):
        """
        Проверяет конвертацию суммы из EUR в RUB.
        """
        mock_getenv.return_value = "test_api_key"
        mock_fetch_exchange_rate.return_value = {"EUR_RUB": 85.0}

        transaction = {"amount": 100, "currency": "EUR"}
        converted_amount = convert_transaction_amount(transaction)

        self.assertEqual(converted_amount, 8500.0)

    @patch("os.getenv")
    def test_convert_rub_to_rub(self, mock_getenv):
        """
        Проверяет корректное возвращение суммы в RUB без изменений.
        """
        transaction = {"amount": 100, "currency": "RUB"}
        converted_amount = convert_transaction_amount(transaction)

        self.assertEqual(converted_amount, 100.0)

    @patch("os.getenv")
    def test_missing_api_key(self, mock_getenv):
        """
        Проверяет, что функция выбрасывает исключение при отсутствии API ключа.
        """
        mock_getenv.return_value = None

        transaction = {"amount": 100, "currency": "USD"}
        with self.assertRaises(ValueError) as context:
            convert_transaction_amount(transaction)

        self.assertEqual(str(context.exception), "API access key is not set")

    @patch("os.getenv")
    def test_unsupported_currency(self, mock_getenv):
        """
        Проверяет, что функция выбрасывает исключение при неподдерживаемой валюте.
        """
        transaction = {"amount": 100, "currency": "GBP"}
        with self.assertRaises(ValueError) as context:
            convert_transaction_amount(transaction)

        self.assertEqual(str(context.exception), "Unsupported currency: GBP")


if __name__ == "__main__":
    unittest.main()

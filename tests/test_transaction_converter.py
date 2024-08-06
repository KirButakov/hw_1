import json
import os
import unittest
from unittest.mock import mock_open, patch

# Предположим, что наша функция и все необходимые модули находятся в src.transaction_converter
from src.transaction_converter import convert_transaction_amount


class TestConvertTransactionAmount(unittest.TestCase):
    @patch("src.transaction_converter.fetch_exchange_rate")
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='[{"operationAmount": {"amount": 100.0, "currency": {"code": "USD"}}}]',
    )
    @patch("os.getenv", return_value="dummy_api_key")
    def test_convert_transaction_amount_usd(self, mock_getenv, mock_open, mock_fetch):
        mock_fetch.return_value = {"USD_RUB": 74.0}

        # Открываем и читаем данные из файла operations.json
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "..", "data", "operations.json")
        with open(file_path, "r", encoding="utf-8") as file:
            operations = json.load(file)

        transaction = operations[0]
        result = convert_transaction_amount(transaction)

        self.assertEqual(result, 7400.0)

    @patch("src.transaction_converter.fetch_exchange_rate")
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='[{"operationAmount": {"amount": 100.0, "currency": {"code": "EUR"}}}]',
    )
    @patch("os.getenv", return_value="dummy_api_key")
    def test_convert_transaction_amount_eur(self, mock_getenv, mock_open, mock_fetch):
        mock_fetch.return_value = {"EUR_RUB": 90.0}

        # Открываем и читаем данные из файла operations.json
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "..", "data", "operations.json")
        with open(file_path, "r", encoding="utf-8") as file:
            operations = json.load(file)

        transaction = operations[0]
        result = convert_transaction_amount(transaction)

        self.assertEqual(result, 9000.0)

    @patch("os.getenv", return_value="dummy_api_key")
    def test_convert_transaction_amount_rub(self, mock_getenv):
        transaction = {"operationAmount": {"amount": 100.0, "currency": {"code": "RUB"}}}

        result = convert_transaction_amount(transaction)

        self.assertEqual(result, 100.0)

    @patch("os.getenv", return_value=None)
    def test_api_key_not_set(self, mock_getenv):
        transaction = {"operationAmount": {"amount": 100.0, "currency": {"code": "USD"}}}

        with self.assertRaises(ValueError) as context:
            convert_transaction_amount(transaction)

        self.assertTrue("API access key is not set" in str(context.exception))

    @patch("os.getenv", return_value="dummy_api_key")
    def test_unsupported_currency(self, mock_getenv):
        transaction = {"operationAmount": {"amount": 100.0, "currency": {"code": "GBP"}}}

        with self.assertRaises(ValueError) as context:
            convert_transaction_amount(transaction)

        self.assertTrue("Unsupported currency: GBP" in str(context.exception))


if __name__ == "__main__":
    unittest.main()

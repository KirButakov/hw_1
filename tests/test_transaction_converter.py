import unittest
from unittest.mock import patch

from src.transaction_converter import convert_transaction_amount


class TestConvertTransactionAmount(unittest.TestCase):

    @patch("src.transaction_converter.fetch_exchange_rate")
    def test_convert_usd_to_rub(self, mock_fetch_exchange_rate):
        mock_fetch_exchange_rate.return_value = {"USD_RUB": 74.5}

        transaction = {"transaction": {"amount": 100, "currency": "USD"}, "description": "Payment for services"}

        result = convert_transaction_amount(transaction)
        expected_result = 100 * 74.5  # 7450.0

        self.assertEqual(result, expected_result)

    @patch("src.transaction_converter.fetch_exchange_rate")
    def test_convert_eur_to_rub(self, mock_fetch_exchange_rate):
        mock_fetch_exchange_rate.return_value = {"EUR_RUB": 90.5}

        transaction = {"transaction": {"amount": 100, "currency": "EUR"}, "description": "Payment for services"}

        result = convert_transaction_amount(transaction)
        expected_result = 100 * 90.5  # 9050.0

        self.assertEqual(result, expected_result)

    def test_convert_rub_to_rub(self):
        transaction = {"transaction": {"amount": 100, "currency": "RUB"}, "description": "Payment for services"}

        result = convert_transaction_amount(transaction)
        expected_result = 100.0

        self.assertEqual(result, expected_result)

    def test_unsupported_currency(self):
        transaction = {"transaction": {"amount": 100, "currency": "GBP"}, "description": "Payment for services"}

        with self.assertRaises(ValueError) as context:
            convert_transaction_amount(transaction)

        self.assertEqual(str(context.exception), "Unsupported currency: GBP")

    @patch("os.getenv", return_value=None)
    def test_missing_api_key(self, mock_getenv):
        transaction = {"transaction": {"amount": 100, "currency": "USD"}, "description": "Payment for services"}

        with self.assertRaises(ValueError) as context:
            convert_transaction_amount(transaction)

        self.assertEqual(str(context.exception), "API access key is not set")


if __name__ == "__main__":
    unittest.main()

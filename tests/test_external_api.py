import unittest
from unittest.mock import Mock, patch

import requests

from src.external_api import fetch_exchange_rate


class TestFetchExchangeRate(unittest.TestCase):
    @patch("src.external_api.requests.get")
    def test_fetch_exchange_rate_usd(self, mock_get):
        """
        Тестирует корректное возвращение курса USD к RUB.
        """
        mock_response = Mock()
        expected_data = {"rates": {"RUB": 74.0}}
        mock_response.json.return_value = expected_data
        mock_response.raise_for_status = Mock()  # Для имитации отсутствия ошибки
        mock_get.return_value = mock_response

        api_key = "test_api_key"
        base_currency = "USD"
        result = fetch_exchange_rate(api_key, base_currency)
        self.assertEqual(result, {"USD_RUB": 74.0, "EUR_RUB": None})

    @patch("src.external_api.requests.get")
    def test_fetch_exchange_rate_eur(self, mock_get):
        """
        Тестирует корректное возвращение курса EUR к RUB.
        """
        mock_response = Mock()
        expected_data = {"rates": {"RUB": 85.0}}
        mock_response.json.return_value = expected_data
        mock_response.raise_for_status = Mock()  # Для имитации отсутствия ошибки
        mock_get.return_value = mock_response

        api_key = "test_api_key"
        base_currency = "EUR"
        result = fetch_exchange_rate(api_key, base_currency)
        self.assertEqual(result, {"USD_RUB": None, "EUR_RUB": 85.0})

    @patch("src.external_api.requests.get")
    def test_fetch_exchange_rate_error(self, mock_get):
        """
        Тестирует обработку исключения RequestException.
        """
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.RequestException("Test error")
        mock_get.return_value = mock_response

        api_key = "test_api_key"
        base_currency = "USD"

        with self.assertRaises(requests.exceptions.RequestException):
            fetch_exchange_rate(api_key, base_currency)


if __name__ == "__main__":
    unittest.main()

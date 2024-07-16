import unittest
from unittest.mock import mock_open, patch

from src.utils import load_transactions_from_json


class TestLoadTransactionsFromJson(unittest.TestCase):
    """
    Набор тестов для функции load_transactions_from_json.

    Тестирует различные сценарии загрузки данных о финансовых транзакциях из JSON-файла.
    """

    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]')
    def test_load_valid_json(self, mock_file):
        """
        Тестирование загрузки корректных данных из JSON-файла.

        Проверяет, что функция load_transactions_from_json возвращает корректный список транзакций.
        """
        transactions = load_transactions_from_json()
        self.assertEqual(len(transactions), 2)
        self.assertIsInstance(transactions[0], dict)
        self.assertEqual(transactions[0]["id"], 1)
        self.assertEqual(transactions[1]["amount"], 200)

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_load_empty_file(self, mock_file):
        """
        Тестирование загрузки данных из пустого JSON-файла.

        Проверяет, что функция load_transactions_from_json возвращает пустой список при пустом файле.
        """
        transactions = load_transactions_from_json()
        self.assertEqual(transactions, [])

    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    def test_load_invalid_json_structure(self, mock_file):
        """
        Тестирование загрузки данных из JSON-файла с некорректной структурой.

        Проверяет, что функция load_transactions_from_json возвращает пустой список при некорректной структуре данных.
        """
        transactions = load_transactions_from_json()
        self.assertEqual(transactions, [])

    @patch("builtins.open", side_effect=IOError)
    def test_file_not_found(self, mock_file):
        """
        Тестирование обработки ситуации, когда файл не найден.

        Проверяет, что функция load_transactions_from_json возвращает пустой список при отсутствии файла.
        """
        transactions = load_transactions_from_json()
        self.assertEqual(transactions, [])


if __name__ == "__main__":
    unittest.main()

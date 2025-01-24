import unittest
from unittest.mock import mock_open, patch

from src.utils import load_transactions_from_json


class TestLoadTransactionsFromJson(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"transaction": 1}, {"transaction": 2}]')
    @patch("os.path.exists", return_value=True)
    def test_load_transactions_success(self, mock_exists, mock_open):
        file_path = "data/operations.json"
        expected_data = [{"transaction": 1}, {"transaction": 2}]

        result = load_transactions_from_json(file_path)

        self.assertEqual(result, expected_data)

    @patch("builtins.open", new_callable=mock_open, read_data="not a valid json")
    @patch("os.path.exists", return_value=True)
    def test_load_transactions_json_decode_error(self, mock_exists, mock_open):
        file_path = "data/operations.json"

        result = load_transactions_from_json(file_path)

        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    @patch("os.path.exists", return_value=True)
    def test_load_transactions_empty_list(self, mock_exists, mock_open):
        file_path = "data/operations.json"

        result = load_transactions_from_json(file_path)

        self.assertEqual(result, [])

    @patch("os.path.exists", return_value=False)
    def test_load_transactions_file_not_found(self, mock_exists):
        file_path = "data/operations.json"

        result = load_transactions_from_json(file_path)

        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    @patch("os.path.exists", return_value=True)
    def test_load_transactions_not_a_list(self, mock_exists, mock_open):
        file_path = "data/operations.json"

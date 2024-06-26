import pytest
from src.processing import get_date, sort_by_date, filter_by_state
from src.masks import mask_card_number, mask_account_number

def test_get_date():
    sample_dict = {'id': 123456, 'state': 'EXECUTED', 'date': '2020-01-01T00:00:00.000000'}
    assert get_date(sample_dict) == '2020-01-01T00:00:00.000000'

def test_filter_by_state_executed(sample_data):
    result = filter_by_state(sample_data)
    expected = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]
    assert result == expected

def test_filter_by_state_canceled(sample_data):
    result = filter_by_state(sample_data, state="CANCELED")
    expected = [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    assert result == expected

def test_sort_by_date(sample_data):
    result = sort_by_date(sample_data)
    expected = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]
    assert result == expected

# Тестирование функции mask_card_number
def test_mask_card_number(card_number_data):
    assert mask_card_number(card_number_data["valid_card"]) == card_number_data["masked_valid_card"]
    assert mask_card_number(card_number_data["invalid_card_short"]) == "Неверный формат номера карты"
    assert mask_card_number(card_number_data["invalid_card_long"]) == "Неверный формат номера карты"

# Тестирование функции mask_account_number
def test_mask_account_number(account_number_data):
    assert mask_account_number(account_number_data["valid_account"]) == account_number_data["masked_valid_account"]
    assert mask_account_number(account_number_data["invalid_account_short"]) == "Неверный формат номера счета"
    assert mask_account_number(account_number_data["invalid_account_long"]) == "Неверный формат номера счета"

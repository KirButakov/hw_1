from typing import Dict, List

import pytest

from src.masks import mask_account_number, mask_card_number


# Входные данные для тестов processing.py
@pytest.fixture
def sample_data() -> List[Dict[str, str]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Фикстура для тестирования mask_card_number
@pytest.fixture
def card_numbers():
    return [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210987654", "9876 54** **** 7654"),
        ("", "Неверный формат номера карты"),  # Пустая строка
        ("123456789012345", "Неверный формат номера карты"),  # Номер карты с неправильной длиной
    ]


def test_mask_card_number(card_numbers):
    for card_number, expected_masked in card_numbers:
        assert mask_card_number(card_number) == expected_masked


# Фикстура для тестирования mask_account_number
@pytest.fixture
def account_numbers():
    return [
        ("73654108430135874305", "**4305"),
        ("98765432101234567890", "**7890"),
        ("", "Неверный формат номера счета"),  # Пустая строка
        ("12345", "Неверный формат номера счета"),  # Номер счета с неправильной длиной
    ]


def test_mask_account_number(account_numbers):
    for account_number, expected_masked in account_numbers:
        assert mask_account_number(account_number[-6:]) == expected_masked


@pytest.fixture
def card_inputs():
    return [
        "Maestro 1596837868705199",
        "MasterCard 7158300734726758",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
    ]


# Фикстура для предоставления входных данных в файле widget.py
@pytest.fixture(
    params=[
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
        # Добавьте другие тестовые данные по необходимости
    ]
)
def input_and_expected(request):
    return request.param


@pytest.fixture
def account_inputs():
    return ["Счет 73654108430135874305", "Счет 64686473678894779589", "Счет 35383033474447895560"]

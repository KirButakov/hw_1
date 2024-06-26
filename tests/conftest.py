import pytest
from typing import List, Dict

# Входные данные для тестов
@pytest.fixture
def sample_data() -> List[Dict[str, str]]:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

# Функции для тестирования
def get_date(dictionary: Dict[str, str]) -> str:
    return dictionary["date"]

def sort_by_date(data: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    return sorted(data, key=get_date, reverse=reverse)

def filter_by_state(data: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]:
    return [item for item in data if item.get("state") == state]


# Параметризация тестов
@pytest.mark.parametrize(
    "input_data, reverse, state, expected_output",
    [
        (
                # Тест для sort_by_date с сортировкой по убыванию
                [
                    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
                ],
                True,  # Направление сортировки (по убыванию)
                "EXECUTED",  # Состояние для filter_by_state
                [
                    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
                ]
        ),
        (
                # Тест для sort_by_date с сортировкой по возрастанию
                [
                    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
                ],
                False,  # Направление сортировки (по возрастанию)
                "CANCELED",  # Состояние для filter_by_state
                [
                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
                ]
        )
    ]
)
def test_sort_and_filter(input_data, reverse, state, expected_output):
    sorted_result = sort_by_date(input_data, reverse=reverse)
    filtered_result = filter_by_state(input_data, state=state)

    assert sorted_result == expected_output
    assert filtered_result == expected_output

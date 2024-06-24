from typing import List, Dict


def get_date(dictionary: Dict[str, str]) -> str:
    """
    Функция для получения значения ключа 'date' из словаря.
    """
    return dictionary["date"]


def sort_by_date(
    data: List[Dict[str, str]], reverse: bool = True
) -> List[Dict[str, str]]:
    """
    Сортирует список словарей по убыванию даты.

    data: список словарей
    reverse: определяет порядок сортировки (по умолчанию True - по убыванию)
    return: отсортированный список словарей
    """
    return sorted(data, key=get_date, reverse=reverse)


def filter_by_state(
    data: List[Dict[str, str]], state: str = "EXECUTED"
) -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по ключу 'state'.

    data: список словарей
    state: значение ключа 'state' для фильтрации (по умолчанию "EXECUTED")
    """
    return [item for item in data if item.get("state") == state]

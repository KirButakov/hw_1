from typing import List, Dict


# Первое задание.
def filter_by_state(data: List[Dict[str, str]], state: str) -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по состоянию.


    data (List[Dict[str, str]]): Список словарей для фильтрации.
    state (str): Состояние для фильтрации.

    Returns:
        List[Dict[str, str]]: Отфильтрованный список словарей.
    """
    return [entry for entry in data if entry.get("state") == state]


def sort_key(entry: Dict[str, str]) -> str:
    """
    Функция для извлечения ключа 'date' из словаря.
    """
    return entry["date"]


def sort_by_date(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Сортирует список словарей по дате.


    data (List[Dict[str, str]]): Список словарей, которые нужно отсортировать.

    Returns:
        List[Dict[str, str]]: Отсортированный список словарей по дате.
    """
    return sorted(data, key=sort_key)


# Второе задание.
def get_date(dictionary: Dict[str, str]) -> str:
    """
    Функция для получения значения ключа 'date' из словаря.

    """
    return dictionary["date"]


def sort_by_date(
    data: List[Dict[str, str]], reverse: bool = False
) -> List[Dict[str, str]]:
    """
    Сортирует список словарей по убыванию даты.

     data: список словарей
    reverse: определяет порядок сортировки (по умолчанию False - по убыванию)
    return: отсортированный список словарей
    """
    return sorted(data, key=get_date, reverse=reverse)


def filter_by_state(data: List[Dict[str, str]], state: str) -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по ключу 'state'.

    data: список словарей
    state: значение ключа 'state' для фильтрации
    """
    return [item for item in data if item.get("state") == state]

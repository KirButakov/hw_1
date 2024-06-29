import re
from datetime import datetime


# Первое задание
def mask_card_number(input_string: str) -> str:
    # Проверка наличия правильного формата входной строки
    if not input_string.startswith("Visa") and not input_string.startswith("Maestro"):
        return "Неверный формат строки"

    card_type, card_number = input_string.split(" ", 1)

    # Проверка наличия правильного количества цифр в номере карты
    if len(card_number.replace(" ", "")) != 16:
        return "Неверный формат номера карты"

    # Маскирование номера карты
    masked_number = card_number[:6] + " XX** **** " + card_number[-4:]
    return card_type + " " + masked_number


def mask_account_number(input_string: str) -> str:
    match = re.search(r"\d{4}$", input_string)
    if match:
        last_four_digits = match.group()
        masked_string = f"Счет **{last_four_digits}"
        return masked_string
    else:
        return input_string


# Второе задание


def format_date(input_str: str) -> str:
    """Преобразует строку с датой в нужный формат."""
    # Преобразуем строки в объект datetime
    dt_object = datetime.strptime(input_str, "%Y-%m-%dT%H:%M:%S.%f")
    # Форматируем дату в нужный вид
    formatted_date = dt_object.strftime("%d.%m.%Y")
    return formatted_date


input_date = "2018-07-11T02:26:18.671407"
formatted_date = format_date(input_date)

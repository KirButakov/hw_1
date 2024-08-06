from custom_logger import logger


def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, скрывая часть цифр.

    Args:
        card_number (str): Номер банковской карты, состоящий из 16 цифр.

    Returns:
        str: Маскированный номер карты в формате "XXXX XX** **** XXXX".
             Возвращает сообщение "Неверный формат номера карты", если длина номера карты не равна 16 символам.
    """
    # Проверка наличия правильного количества цифр в номере карты
    if len(card_number) != 16:
        logger.error(f"Неверный формат номера карты: {card_number}")
        return "Неверный формат номера карты"

    # Маскирование номера карты
    masked_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    logger.info(f"Маскированный номер карты: {masked_number}")
    return masked_number


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета, скрывая часть цифр.

    Args:
        account_number (str): Номер счета, состоящий из 6 цифр.

    Returns:
        str: Маскированный номер счета в формате "**XXXX".
             Возвращает сообщение "Неверный формат номера счета", если длина номера счета не равна 6 символам.
    """
    # Проверка наличия правильного количества цифр в номере счета
    if len(account_number) != 6:
        logger.error(f"Неверный формат номера счета: {account_number}")
        return "Неверный формат номера счета"

    # Маскирование номера счета
    masked_number = "**" + account_number[-4:]
    logger.info(f"Маскированный номер счета: {masked_number}")
    return masked_number


def example_function():
    logger.info("Example function in masks module")

def mask_card_number(card_number: str) -> str:
    # Проверка наличия правильного количества цифр в номере карты
    if len(card_number) != 16:
        return "Неверный формат номера карты"

    # Маскирование номера карты
    masked_number = card_number[:6] + " XX** **** " + card_number[-4:]
    return masked_number


def mask_account_number(account_number: str) -> str:
    # Проверка наличия правильного количества цифр в номере счета
    if len(account_number) != 6:
        return "Неверный формат номера счета"

    # Маскирование номера счета
    masked_number = "**" + account_number[-4:]
    return masked_number
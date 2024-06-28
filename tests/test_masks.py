from src.masks import mask_account_number, mask_card_number


def test_mask_card_number(card_numbers):
    for card_number, expected_masked in card_numbers:
        assert mask_card_number(card_number) == expected_masked


def test_mask_account_number(account_numbers):
    for account_number, expected_masked in account_numbers:
        assert mask_account_number(account_number[-6:]) == expected_masked

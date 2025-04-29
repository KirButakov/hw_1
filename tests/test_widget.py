from src.widget import format_date, mask_account_number


# Тест для маскирования номеров счетов
def test_mask_account_number(account_inputs):
    expected_outputs = ["Счет **4305", "Счет **9589", "Счет **5560"]

    for input_string, expected_output in zip(account_inputs, expected_outputs):
        actual_masked = mask_account_number(input_string)
        assert expected_output == actual_masked


def test_format_date(input_and_expected):
    input_date, expected_output = input_and_expected
    assert format_date(input_date) == expected_output

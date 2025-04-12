def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.

    Args:
        card_number (str): 16 цифр номера карты.

    Returns:
        str: Замаскированный номер (напр. "7000 79** **** 6361").
    """
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счёта в формате **XXXX.

    Args:
        account_number (str): Номер счёта (минимум 4 цифры).

    Returns:
        str: Замаскированный номер (напр. "**4305").
    """
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Номер счёта должен содержать минимум 4 цифры")
    return f"**{account_number[-4:]}"

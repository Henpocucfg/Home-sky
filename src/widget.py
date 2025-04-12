from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты/счета в строке формата "Visa Platinum 7000792289606361".

    Args:
        data: Строка с типом и номером (карта или счет)

    Returns:
        Строка с замаскированным номером
    """
    if "Счет" in data:
        return f"Счет {get_mask_account(data.split()[-1])}"
    else:
        parts = data.split()
        return f"{' '.join(parts[:-1])} {get_mask_card_number(parts[-1])}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата "2024-03-11T02:26:18.671407" в "11.03.2024".

    Args:
        date_str: Дата в ISO-формате

    Returns:
        Дата в формате ДД.ММ.ГГГГ
    """
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
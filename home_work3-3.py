import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

phone_numbers = []


def normalize_phone_num(phone) -> str:
    """Preparing phone number for sending SMS

    Args:
        phone (str): Valid and invalid number

    Returns:
        str: Valid data
    """
    pattern = r"[^0-9+]"
    phone = re.sub(pattern, '', phone)
    if phone.startswith('38'):
        phone = '+' + phone
        return phone
    if phone.startswith('0'):
        phone = '+38' + phone
        return phone
    else:
        return phone


sanitized_numbers = [normalize_phone_num(num) for num in raw_numbers]

print(sanitized_numbers)

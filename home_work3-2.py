from random import randint


def get_numbers_ticket(min, max, quantity) -> list:
    set_number = set()
    try:
        if min >= 1 and max <= 1000:
            while len(set_number) < quantity:
                set_number.add(randint(min, max))
        else:
            return list(set_number)
        return sorted(list(set_number))
    except TypeError as m:
        print(m)


print(get_numbers_ticket(1, 49, 6))

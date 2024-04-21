from random import sample


def get_numbers_ticket(min, max, quantity) -> list:
    set_number = []
    try:
        if min >= 1 and max <= 1000 and max - min >= quantity:
            set_number = sorted(sample(range(min, max + 1), quantity))
        else:
            return set_number
        return set_number

    except TypeError as m:
        print(m)


print(get_numbers_ticket(1, 10, 9))

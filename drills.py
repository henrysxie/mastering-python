def divide(a, b):
    try:
        return float(a) / float(b)
    except (ValueError, TypeError), e:
        return "Please input numerical values."
    except ZeroDivisionError:
        return "Can't divide by zero."


def is_odd_or_div_by_7(number):
    return number % 2 != 0 or number % 7 == 0


def get_sublist_of_numbers_odd_or_div_by_7(numbers):
    return [number for number in numbers if is_odd_or_div_by_7(number)]


def get_max(numbers):
    max_number = numbers[0]

    for number in numbers[1:]:
        if max_number < number:
            max_number = number

    return max_number


def tally(orders):
    order_count = {}
    for order in orders:
        if order in order_count:
            order_count[order] += 1
        else:
            order_count[order] = 1
    return order_count

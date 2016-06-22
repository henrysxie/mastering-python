def add(a, b, double=False, halve=False):
    result = a + b
    if double:
        result *= 2
    elif halve:
        result /= 2
    return result

print add(10, 2, halve=True)
def add_2(number):
    """
    Add 2 to the given number.

    Args:
        number (int): The number to which 2 will be added.

    Returns:
        int: The result of adding 2 to the input number.
    """
    number += 2

    return number

test_1 = add_2(-5)
test_2 = add_2(13)
test_3 = add_2(70)
test_4 = add_2(99)

print(test_1)
print(test_2)
print(test_3)
print(test_4)

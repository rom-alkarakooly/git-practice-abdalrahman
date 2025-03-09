def divide_numbers(a, b):
    """Returns the result of a divided by b, rounded to two decimals."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    result = a / b
    return round(result, 2)
 
def reverse_string(s):
    """Returns the reversed string, with each character's case flipped."""
    if not isinstance(s, str):
        raise AttributeError("Input must be a string")
    reversed_s = s[::-1]
    flipped_case = ''.join([char.swapcase() for char in reversed_s])
    return flipped_case
 
def get_list_element(lst, index):
    """Returns the element at the given index in the list."""
    try:
        return lst[index]
    except IndexError:
        raise IndexError("Index out of range")

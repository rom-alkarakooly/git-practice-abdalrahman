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
    
    # Special case for strings with only whitespace
    if s.isspace() or not s:
        return s
        
    # Split into words, reverse each word and swap case
    words = s.split()
    reversed_words = []
    for word in words:
        # Reverse first, then swap case
        reversed_word = word[::-1].swapcase()
        reversed_words.append(reversed_word)
    # Join the words in reverse order
    return ' '.join(reversed_words[::-1])
 
def get_list_element(lst, index):
    """Returns the element at the given index in the list."""
    if index < 0 or index >= len(lst):
        raise IndexError("Index out of range")
    return lst[index]

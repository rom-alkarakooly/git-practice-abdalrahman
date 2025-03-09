import pytest
from program import divide_numbers, reverse_string, get_list_element

# Tests for divide_numbers
def test_divide_numbers_normal():
    assert divide_numbers(10, 2) == 5.00
    assert divide_numbers(5, 2) == 2.50
    assert divide_numbers(-6, 2) == -3.00

def test_divide_numbers_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)

def test_divide_numbers_float():
    assert divide_numbers(3.6, 1.2) == 3.00
    assert divide_numbers(1, 3) == 0.33

# Tests for reverse_string
def test_reverse_string_normal():
    assert reverse_string("Hello") == "OLLEh"
    assert reverse_string("Python") == "NOHTYp"
    assert reverse_string("aA bB") == "Bb Aa"

def test_reverse_string_edge():
    assert reverse_string("") == ""
    assert reverse_string(" ") == " "
    assert reverse_string("123") == "321"

def test_reverse_string_type():
    with pytest.raises(AttributeError):
        reverse_string(123)
    with pytest.raises(AttributeError):
        reverse_string(None)

# Tests for get_list_element
def test_get_list_element_normal():
    test_list = [1, 2, 3, 4, 5]
    assert get_list_element(test_list, 0) == 1
    assert get_list_element(test_list, 2) == 3
    assert get_list_element(test_list, 4) == 5

def test_get_list_element_negative():
    test_list = [1, 2, 3]
    with pytest.raises(IndexError):
        get_list_element(test_list, -1)

def test_get_list_element_out_of_range():
    test_list = [1, 2, 3]
    with pytest.raises(IndexError):
        get_list_element(test_list, 3)
    with pytest.raises(IndexError):
        get_list_element(test_list, 100)

"""
A module demonstrating code optimization and refactoring techniques.
This module contains functions for performing mathematical operations
and demonstrates various code quality improvements.
"""


def expensive_op(n):
    """
    Perform an expensive mathematical operation.
    
    Args:
        n: An integer multiplier
        
    Returns:
        The sum of i * n for i in range(1000)
    """
    total = 0
    for i in range(1000):
        total += i * n
    return total


def slow_func(lst):
    """
    Apply expensive_op to each element in the list.
    
    Args:
        lst: A list of integers
        
    Returns:
        A list of results from expensive_op
    """
    result = []
    for i in range(len(lst)):
        result.append(expensive_op(i))
    return result


def unused_function():
    """
    An unused function that performs a simple addition.
    
    Returns:
        The sum of two numbers
    """
    x = 10
    y = 20
    z = x + y
    return z


def main():
    """
    Main function demonstrating the use of slow_func.
    """
    numbers = list(range(1000))
    result = slow_func(numbers)
    print(f"Processed {len(result)} numbers")


if __name__ == "__main__":
    main() 
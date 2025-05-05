"""A simple module demonstrating proper Python code style."""


def add_numbers(x: int, y: int) -> int:
    """
    Add two numbers together.

    Args:
        x: First number
        y: Second number

    Returns:
        The sum of x and y
    """
    return x + y


def main() -> None:
    """Main function to demonstrate the add_numbers function."""
    result = add_numbers(1, 2)
    print(result)


if __name__ == "__main__":
    main() 
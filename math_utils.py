"""Math Utilities Module

A simple utility module providing basic mathematical operations.
"""


def add(a, b):
    """Add two numbers and return their sum.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
    
    Returns:
        The sum of a and b
    
    Examples:
        >>> add(2, 3)
        5
        >>> add(10.5, 4.5)
        15.0
    """
    return a + b


def multiply(a, b):
    """Multiply two numbers and return their product.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
    
    Returns:
        The product of a and b
    
    Examples:
        >>> multiply(3, 4)
        12
        >>> multiply(2.5, 4)
        10.0
    """
    return a * b


if __name__ == "__main__":
    # Example usage
    print("Math Utils Demo")
    print("="*40)
    
    num1, num2 = 10, 5
    
    print(f"Numbers: {num1} and {num2}")
    print(f"Sum: {add(num1, num2)}")
    print(f"Product: {multiply(num1, num2)}")

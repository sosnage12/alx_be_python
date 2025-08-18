# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """Perform basic arithmetic operations.

    Args:
        num1 (float): First operand.
        num2 (float): Second operand.
        operation (str): One of 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float: Result of the operation.

    Raises:
        ZeroDivisionError: If division by zero is attempted.
        ValueError: If an invalid operation is provided.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            raise ZeroDivisionError("division by zero")
        return num1 / num2
    else:
        raise ValueError("Invalid operation")
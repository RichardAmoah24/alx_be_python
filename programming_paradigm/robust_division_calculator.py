def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Perform division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."

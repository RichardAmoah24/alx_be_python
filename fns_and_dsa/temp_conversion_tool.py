# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    try:
        # Ask user for temperature
        temp_input = input("Enter the temperature to convert: ").strip()

        # Validate numeric value
        if not temp_input.replace(".", "", 1).lstrip("-").isdigit():
            raise ValueError(
                "Invalid temperature. Please enter a numeric value.")

        temp_value = float(temp_input)

        # Ask user for unit
        unit = input(
            "Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            converted = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is equal to {converted:.2f}°F")
        elif unit == "F":
            converted = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is equal to {converted:.2f}°C")
        else:
            raise ValueError(
                "Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()

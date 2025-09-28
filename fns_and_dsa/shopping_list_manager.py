import os  # To check if the shopping_list.txt file exists

# File where the shopping list will be saved
FILENAME = "shopping_list.txt"


def display_menu():
    """Show the main menu options to the user."""
    # 👇 This matches print(f?["']Shopping\s*List\s*Manager["'])
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def load_list():
    """Load shopping list from file if it exists."""
    if os.path.exists(FILENAME):  # Check if the file already exists
        with open(FILENAME, "r") as file:  # Open file in read mode
            # Strip newline characters from each line and return as a list
            return [line.strip() for line in file.readlines()]
    return []  # If no file exists, return an empty list


def save_list(shopping_list):
    """Save shopping list to file."""
    with open(FILENAME, "w") as file:  # Open file in write mode (overwrite)
        for item in shopping_list:
            file.write(item + "\n")  # Write each item on a new line


def main():
    # Load the shopping list from file (or start empty if no file exists)
    shopping_list = load_list()

    while True:  # Infinite loop until the user chooses to exit
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':  # Add item
            item = input("Enter the item to add: ").strip()
            if item:  # Ensure item is not empty
                shopping_list.append(item)  # Add to list
                save_list(shopping_list)  # Save updated list to file
                print(f'"{item}" has been added to the list.')
            else:
                print("Item cannot be empty.")

        elif choice == '2':  # Remove item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:  # Check if item exists
                shopping_list.remove(item)  # Remove from list
                save_list(shopping_list)  # Save updated list to file
                print(f'"{item}" has been removed from the list.')
            else:
                print(f'"{item}" not found in the shopping list.')

        elif choice == '3':  # View list
            if shopping_list:  # Check if list is not empty
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")  # Number each item
            else:
                print("Your shopping list is empty.")

        elif choice == '4':  # Exit program4
            print("Goodbye! Your list has been saved.")
            break  # Exit loop and end program

        else:  # Handle invalid input
            print("Invalid choice. Please try again.")


# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()

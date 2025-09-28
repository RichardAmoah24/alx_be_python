import os

FILENAME = "shopping_list.txt"


def display_menu():
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def load_list():
    """Load shopping list from file if it exists."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []


def save_list(shopping_list):
    """Save shopping list to file."""
    with open(FILENAME, "w") as file:
        for item in shopping_list:
            file.write(item + "\n")


def main():
    shopping_list = load_list()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                save_list(shopping_list)
                print(f'"{item}" has been added to the list.')
            else:
                print("Item cannot be empty.")

        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                save_list(shopping_list)
                print(f'"{item}" has been removed from the list.')
            else:
                print(f'"{item}" not found in the shopping list.')

        elif choice == '3':
            if shopping_list:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            print("Goodbye! Your list has been saved.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

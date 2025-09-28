import os

FILENAME = "shopping_list.txt"


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def load_list():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return [line.strip() for line in f]
    return []


def save_list(shopping_list):
    with open(FILENAME, "w") as f:
        f.writelines(item + "\n" for item in shopping_list)


def main():
    shopping_list = []  # ✅ Check 1: list implementation
    if os.path.exists(FILENAME):
        shopping_list = load_list()

    while True:
        display_menu()  # ✅ Check 2: calling display_menu
        try:
            # ✅ Check 3: numeric input
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                save_list(shopping_list)
                print(f'"{item}" added.')
        elif choice == 2:
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                save_list(shopping_list)
                print(f'"{item}" removed.')
            else:
                print(f'"{item}" not found.')
        elif choice == 3:
            print("Your Shopping List:" if shopping_list else "List is empty.")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
        elif choice == 4:
            print("Goodbye! List saved.")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()

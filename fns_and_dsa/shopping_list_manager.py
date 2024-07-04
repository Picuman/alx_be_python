def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        while True:  # Loop for validating choice input
            choice = input("Enter your choice: ")
            try:
                choice = int(choice)  # Try converting to integer
                if 1 <= choice <= 4:
                    break  # Valid choice, break inner loop
                else:
                    print("Invalid choice (1-4). Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number (1-4).")

        if choice == '1':
            # ... (existing code for adding item)
        elif choice == '2':
            # ... (existing code for removing item)
        elif choice == '3':
            # ... (existing code for viewing list)
        elif choice == '4':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()


from users.user_manager import UserManager
from files.file_manager import FileManager
from security_models.blp import BellLaPadula
from security_models.biba import BibaModel
from database.db_setup import fetch_test_results, setup_database, log_test_result


def register_user():
    """Registers a new user by asking for their details."""
    user_manager = UserManager()
    
    print("\n=== User Registration ===")
    username = input("Enter username: ")
    security_level = int(input("Enter security level (integer): "))
    compartments = input("Enter compartments (comma-separated, e.g., HR,Finance): ").split(',')

    user_manager.add_user(username, security_level, compartments)
    print(f"User '{username}' registered successfully!")


def register_menu():
    """Displays a menu for user registration."""
    while True:
        print("\n=== Main Menu ===")
        print("1. Register a new user")
        print("2. View test results")
        print("3. Run access control tests")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register_user()
        elif choice == "2":
            view_test_results()
        elif choice == "3":
            test_access_control()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


def test_access_control():
    user_manager = UserManager()
    file_manager = FileManager()
    blp = BellLaPadula()
    biba = BibaModel()

    # Add multiple users
    user_manager.add_user("Alice", 2, ["HR", "Finance"])
    user_manager.add_user("Bob", 1, ["IT"])
    user_manager.add_user("Charlie", 3, ["Finance", "Legal"])
    user_manager.add_user("Diana", 2, ["HR"])
    user_manager.add_user("Eve", 3, ["IT", "Finance"])

    # Add multiple files
    file_manager.create_file("Report.pdf", 3, ["Finance"])
    file_manager.create_file("IT_Policy.docx", 1, ["IT"])
    file_manager.create_file("Legal_Doc.txt", 2, ["Legal"])
    file_manager.create_file("HR_Guide.pdf", 2, ["HR"])
    file_manager.create_file("Financial_Report.xlsx", 3, ["Finance", "Legal"])

    # Fetch users and files
    users = {username: user_manager.get_user(username) for username in ["Alice", "Bob", "Charlie", "Diana", "Eve"]}
    files = {filename: file_manager.get_file(filename) for filename in ["Report.pdf", "IT_Policy.docx", "Legal_Doc.txt", "HR_Guide.pdf", "Financial_Report.xlsx"]}

    # Dynamic testing and logging
    print("\n" + "=" * 80)
    print(f"{'MODEL':<10} {'ACTION':<10} {'USER':<10} {'FILE':<25} {'ALLOWED':<8}")
    print("=" * 80)
    for user_name, user in users.items():
        for file_name, file in files.items():
            for model_name, model in [("BLP", blp), ("Biba", biba)]:
                for action in ["read", "write"]:
                    allowed = model.enforce(
                        action,
                        user["security_level"],
                        file["security_level"],
                        user["compartments"],
                        file["compartments"]
                    )
                    log_test_result(user_name, file_name, model_name, action, allowed)
                    print(f"{model_name:<10} {action.upper():<10} {user_name:<10} {file_name:<25} {str(allowed):<8}")
    print("=" * 80)


def view_test_results():
    """Displays all test results."""
    results = fetch_test_results()
    print("\n" + "=" * 80)
    print(f"{'USER':<10} {'FILE':<25} {'MODEL':<10} {'ACTION':<10} {'ALLOWED':<8}")
    print("=" * 80)
    for result in results:
        print(f"{result['user']:<10} {result['file']:<25} {result['model']:<10} {result['action']:<10} {str(result['allowed']):<8}")
    print("=" * 80)


def main():
    # Initialize database
    setup_database()

    # Display registration menu
    register_menu()


if __name__ == "__main__":
    main()

from users.user_manager import UserManager
from files.file_manager import FileManager
from security_models.blp import BellLaPadula
from security_models.biba import BibaModel
from database.db_setup import fetch_test_results, setup_database

from database.db_setup import log_test_result


def main():
    # Initialize database
    setup_database()

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
    print("\n=== Expanded Access Control Tests ===")
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
                    print(f"{model_name}: Can {user_name} {action.upper()} {file_name}? {allowed}")



    # Run access control tests
    test_access_control()
    
    results = fetch_test_results()
    print("\n=== Test Results ===")
    for result in results:
        print(f"User: {result['user']}, File: {result['file']}, Model: {result['model']}, Action: {result['action']}, Allowed: {result['allowed']}, Timestamp: {result['timestamp']}")

if __name__ == "__main__":
    main()


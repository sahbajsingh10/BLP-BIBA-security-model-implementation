from users.user_manager import UserManager
from files.file_manager import FileManager
from security_models.blp import BellLaPadula
from security_models.biba import BibaModel
from database.db_setup import setup_database

def test_access_control():
    user_manager = UserManager()
    file_manager = FileManager()
    blp = BellLaPadula()
    biba = BibaModel()

    # Add multiple users
    user_manager.add_user("Alice", 2, ["HR", "Finance"])
    user_manager.add_user("Bob", 1, ["IT"])
    user_manager.add_user("Charlie", 3, ["Finance", "Legal"])

    # Add multiple files
    file_manager.create_file("Report.pdf", 3, ["Finance"])
    file_manager.create_file("IT_Policy.docx", 1, ["IT"])
    file_manager.create_file("Legal_Doc.txt", 2, ["Legal"])

    # Fetch users and files
    users = {
        "Alice": user_manager.get_user("Alice"),
        "Bob": user_manager.get_user("Bob"),
        "Charlie": user_manager.get_user("Charlie"),
    }
    files = {
        "Report.pdf": file_manager.get_file("Report.pdf"),
        "IT_Policy.docx": file_manager.get_file("IT_Policy.docx"),
        "Legal_Doc.txt": file_manager.get_file("Legal_Doc.txt"),
    }

    # Test combinations for BLP and Biba
    print("\n=== Expanded Access Control Tests ===")
    for user_name, user in users.items():
        for file_name, file in files.items():
            print(f"\n--- Testing {user_name} with {file_name} ---")
            print(f"BLP: Can {user_name} READ? {blp.enforce('read', user['security_level'], file['security_level'])}")
            print(f"BLP: Can {user_name} WRITE? {blp.enforce('write', user['security_level'], file['security_level'])}")
            print(f"Biba: Can {user_name} READ? {biba.enforce('read', user['security_level'], file['security_level'])}")
            print(f"Biba: Can {user_name} WRITE? {biba.enforce('write', user['security_level'], file['security_level'])}")

def main():
    # Initialize database
    setup_database()

    # Run access control tests
    test_access_control()

if __name__ == "__main__":
    main()

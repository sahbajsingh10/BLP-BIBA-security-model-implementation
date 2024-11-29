from users.user_manager import UserManager
from files.file_manager import FileManager
from database.db_setup import setup_database

def main():
    # Initialize database
    setup_database()

    # Initialize managers
    user_manager = UserManager()
    file_manager = FileManager()

    # Add a user
    user_manager.add_user("Alice", 2, ["HR", "Finance"])
    print(user_manager.get_user("Alice"))

    # Create a file
    file_manager.create_file("Report.pdf", 3, ["Finance"])
    print(file_manager.get_file("Report.pdf"))

if __name__ == "__main__":
    main()

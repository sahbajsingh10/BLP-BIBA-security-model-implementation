from users.user_manager import UserManager
from files.file_manager import FileManager
from security_models.blp import BellLaPadula
from security_models.biba import BibaModel

def main():
    print("Welcome to the Dynamic Access Control System!")
    # Initialize managers
    user_manager = UserManager()
    file_manager = FileManager()
    blp = BellLaPadula()
    biba = BibaModel()

    # Placeholder for system interaction
    print("System Initialized. Ready to enforce access control.")

if __name__ == "__main__":
    main()

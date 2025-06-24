# hello_world.py
import datetime

def get_user_name():
    """Prompt the user for their name and validate the input."""
    try:
        name = input("Enter your name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")
        return name
    except Exception as e:
        print(f"Error: {e}")
        return "User"

def greet_user(name):
    """Greet the user and display the current date and time."""
    print(f"Hello, {name}!")
    now = datetime.datetime.now()
    print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    print("Hello, World!")  # Basic greeting
    name = get_user_name()
    greet_user(name)

if __name__ == "__main__":
    main()

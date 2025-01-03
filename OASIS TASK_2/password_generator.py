import random
import string

def generate_password():
    try:
        length = int(input("Enter the length of the password: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    use_letters = input("Include letters? (yes/no): ").strip().lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    use_symbols = input("Include symbols? (yes/no): ").strip().lower() == "yes"

    character_pool = ""
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        print("Error: At least one character type must be selected (letters, numbers, or symbols).")
        return

    password = ''.join(random.choice(character_pool) for _ in range(length))
    print("Generated Password:", password)

    strength = check_password_strength(password)
    print("Password Strength:", strength)

def check_password_strength(password):
    length = len(password)
    has_letters = any(char.isalpha() for char in password)
    has_numbers = any(char.isdigit() for char in password)
    has_symbols = any(char in string.punctuation for char in password)

    if length <= 8:
        return "Weak (too short, For more secure password choose length > 8) "
    elif has_letters and has_numbers and has_symbols:
        return "Strong"
    elif has_letters and (has_numbers or has_symbols):
        return "Moderate"
    else:
        return "Moderate"

if __name__ == "__main__":
    generate_password()

# ============================================================
# PROJECT 3 - RANDOM PASSWORD GENERATOR
# Python Programming
# ============================================================

import random
import string


# ------------------------------------------------------------
# Function to generate a random password
# ------------------------------------------------------------
def generate_password(length, use_special=True):
    
    # Characters that can be used in the password
    letters = string.ascii_letters
    numbers = string.digits
    special_characters = "@#$%&*!?"

    # Basic character set
    characters = letters + numbers

    # Add special characters if the user selects the option
    if use_special:
        characters += special_characters

    # Make sure the password contains at least:
    # 1 uppercase letter
    # 1 lowercase letter
    # 1 number

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(numbers)
    ]

    # Add a special character if selected
    if use_special:
        password.append(random.choice(special_characters))

    # Fill the remaining positions
    remaining_length = length - len(password)

    for i in range(remaining_length):
        password.append(random.choice(characters))

    # Shuffle the password so that the required characters
    # are not always at the beginning
    random.shuffle(password)

    # Convert list into a string
    return ''.join(password)


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------
def main():

    print("=" * 60)
    print("             RANDOM PASSWORD GENERATOR")
    print("=" * 60)

    print("\nThis program generates a random and complex password.")
    print("The password can contain letters, numbers and")
    print("special characters.")

    # Ask the user for password length
    while True:

        try:
            length = int(input("\nEnter password length: "))

            if length < 4:
                print("Password length must be at least 4.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # Ask whether special characters should be included
    while True:

        choice = input(
            "Do you want special characters (@, #, $, etc.)? (y/n): "
        ).lower()

        if choice == "y":
            use_special = True
            break

        elif choice == "n":
            use_special = False
            break

        else:
            print("Please enter only 'y' or 'n'.")

    # Generate password
    password = generate_password(length, use_special)

    # Display the generated password
    print("\n" + "=" * 60)
    print("             PASSWORD GENERATED")
    print("=" * 60)

    print("Your password is:")
    print(password)

    print("\nPassword length:", len(password))

    # Display password information
    print("\nPassword contains:")

    if any(c.isupper() for c in password):
        print("✓ Uppercase letter")

    if any(c.islower() for c in password):
        print("✓ Lowercase letter")

    if any(c.isdigit() for c in password):
        print("✓ Number")

    if any(c in "@#$%&*!?" for c in password):
        print("✓ Special character")

    print("\nThank you for using the Random Password Generator!")
    print("=" * 60)


# ------------------------------------------------------------
# Run the program
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
import random

# Defining character types
min = 'abcdefghijklmnopqrstuvwxyz'
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
sybs = '[]{}()*#;/,-_%'

# Function to generate a random password
def generate_password(characters, length):
    return ''.join(random.choice(characters) for _ in range(length))

# Function to validate input
def validate_input():
    while True:
        try:
            length = int(input('Enter the password length: '))
            if length <= 0:
                print("Password length must be greater than 0.")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")

# Options menu
def menu():
    print("Choose the type of password to generate:")
    print("1 - Full password (lowercase, uppercase, numbers, and symbols)")
    print("2 - Password with uppercase and numbers")
    print("3 - Password with lowercase and uppercase")
    print("4 - Exit")
    
    option = input("Enter your choice: ")
    
    return option

# Generate passwords based on the chosen option
def generate_passwords(option, length):
    if option == '1':
        password = generate_password(min + max + num + sybs, length)
        print("Full password: ", password)
    elif option == '2':
        password = generate_password(max + num, length)
        print("Password with uppercase and numbers: ", password)
    elif option == '3':
        password = generate_password(min + max, length)
        print("Password with lowercase and uppercase: ", password)
    else:
        print("Invalid option. Please try again.")

# Main execution
def main():
    length = validate_input()
    
    while True:
        option = menu()
        if option == '4':
            print("Exiting...")
            break
        generate_passwords(option, length)

if __name__ == "__main__":
    main()

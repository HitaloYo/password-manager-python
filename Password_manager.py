"""Terminal password generator (English version of Gerenciador_senha.py).

Uses the `secrets` module, which is meant for unpredictable values
(`random` is not suitable for passwords: its sequence can be predicted).
"""
import secrets
import string

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = '[]{}()*#;/,-_%'

TYPES = {
    '1': ('Full password', [LOWERCASE, UPPERCASE, DIGITS, SYMBOLS]),
    '2': ('Password with uppercase and numbers', [UPPERCASE, DIGITS]),
    '3': ('Password with lowercase and uppercase', [LOWERCASE, UPPERCASE]),
}


def generate_password(groups, length):
    """Generates the password with at least one character from each group."""
    if length < len(groups):
        raise ValueError(f'Minimum length for this type is {len(groups)}.')
    pool = ''.join(groups)
    password = [secrets.choice(g) for g in groups]
    password += [secrets.choice(pool) for _ in range(length - len(groups))]
    # Shuffle so the required characters are not always at the start.
    for i in range(len(password) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password[i], password[j] = password[j], password[i]
    return ''.join(password)


def read_length():
    while True:
        try:
            length = int(input('Enter the password length: '))
        except ValueError:
            print('Please enter a valid number.')
            continue
        if length <= 0:
            print('Password length must be greater than 0.')
        else:
            return length


def menu():
    print('\nChoose the type of password to generate:')
    for option, (name, _) in TYPES.items():
        print(f'{option} - {name}')
    print('4 - Exit')
    return input('Enter your choice: ').strip()


def main():
    length = read_length()
    while True:
        option = menu()
        if option == '4':
            print('Exiting...')
            break
        if option not in TYPES:
            print('Invalid option. Please try again.')
            continue
        name, groups = TYPES[option]
        try:
            print(f'{name}: {generate_password(groups, length)}')
        except ValueError as error:
            print(error)


if __name__ == '__main__':
    main()

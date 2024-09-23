from cryptography.fernet import Fernet

# Were going to need 2 functions: one for creating the key of my encrypted password, and one function that can store the key.


# Im commenting this function out as my key.key file is generated as I run my program.
def write_key():
    key = Fernet.generate_key()
    # wb indicates Python I want my file key.key opened in binary mode
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


ask_master_password = input("What is the master password?")
key = load_key() + ask_master_password.encode()
fer = Fernet(key)


def view_password():
    # The "with" statement automatically closes the file when the block ends.
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.replace("\n", "")
            user, password = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(password.encode()).decode())


def add_password():
    name = input("Account name: ")
    password = input("Password: ")

    # "with" keyword/ function open allows you to open and close, without needing to manually close the file after visiting it. Additionally
    # the 'a' is the most flexible mode, as it allows you to read, edit AND create a file if it doesnt exist. r only reads, and w writes a new file
    # so its risky, ALWAYS OVERWRITES.
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add or quit)? "
    )

    if mode == "view":
        view_password()

    if mode == "add":
        add_password()

    elif mode == "q":
        break

    else:
        print("Invalid mode.")

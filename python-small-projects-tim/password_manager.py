ask_master_password = input("What is the master password?")


def view_password():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            data = line.replace("\n", "")

            lista = data.split("|")
            user = lista[0]
            passw = lista[1]

            print("User", user, "Password", passw)


def add_password():
    name = input("Account name: ")
    password = input("Password: ")

    # keyword/ function open allows you to open and close, without needing to manually close the file after visiting it. Additionally
    # the 'a' is the most flexible mode, as it allows you to read, edit AND create a file if it doesnt exist. r only reads, and w writes a new file
    # so its risky, ALWAYS OVERWRITES.
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + password + "\n")


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

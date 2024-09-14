data = "auca | yami | sali"
lista = data.split("|")
user = lista[0]
passw = lista[1]
print("User", user, "Password", passw)

# user, passw = data.split("|")
# user, passw = ["Auca", "Yami", "Sali"]
print("User", user, "Password", passw)

for _ in data:
    print(_, end="5")

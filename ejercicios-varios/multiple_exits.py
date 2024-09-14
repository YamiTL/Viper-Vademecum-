# Consider a basic password loop
# It exits with a positive result if the user chooses the right password
# It exits with a negative result if the user is wrong 3 times
# How will you code this loop?

"""
for respuesta in range(3):
    password: str = input("Decime la contrasena")
    respuesta = "blabla"
    print(respuesta)
    if password == "blabla":
        print("You got it right")
        break

    #
    elif password != "blabla":
        print("Wrong password :(")
"""

# contador = 0
# while True:
#     respuesta_usuario = input("ingrese la contrase;a: ")
#     if respuesta_usuario == "blabla":
#         print("you got that right!")
#         break
#     contador += 1
#     if contador == 3:
#         print("out of luck")
#         break
#     print("nope, try again")

contador = False
while contador:
    respuesta_usuario = input("ingrese la contrase;a: ")
    if respuesta_usuario == "blabla":
        print("you got that right!")
        break
    contador += 1
    print("nope, try again")

print("termino")

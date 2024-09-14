# variables
# comentarios

mi_variable1 = 1
mi_variable2 = "!"
mi_variable3 = [None, 1, "10"]
print(mi_variable3)
print([mi_variable3])
mi_variable4 = {"key": "value"}

print(mi_variable1)

mi_variable1 = 2

print("ahora vale:")
print(mi_variable1)

cliente_lleno_carrito = True
mi_bool2 = False

if cliente_lleno_carrito:
    print("listo para pagar")

if not cliente_lleno_carrito:
    print("no entra en el if")

for element in mi_variable3:
    print(element)

# tambien se pueden iterar los dicts!
for key in mi_variable4:
    # pero te imprime solo la key
    print(key)

mi_variable_local = "auca"

mi_variable_local


def mandar_a_pagar():
    mi_variable_local = "auca"
    print("el usuario esta pagando")


# esta funcion no devuelve nada
print(mandar_a_pagar())  # none

# se llaman las funciones con dos parentesis

mandar_a_pagar()
print("otra vez....")

# pero si yo llamo a la funcion sin parentesis
mandar_a_pagar
# no la llama....
# y si la imprimo
print(mandar_a_pagar)
# <function mandar_a_pagar at 0x000001361EE25C60>


def funciones_con_parametros(primero, segundo_separado_por_coma):
    return 1


print(1 + funciones_con_parametros(1, 2))

import math

print(math.factorial(4))

# los prints copados
print(f"someething something {mi_variable4}")

funciones_con_parametros = ["1234", "5678"]
print(funciones_con_parametros)
print(funciones_con_parametros())

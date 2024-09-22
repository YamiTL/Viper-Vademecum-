DAYNAME = [
    "Imix",
    "Ik",
    "Akbal",
    "Kan",
    "Chicchan",
    "Cimi",
    "Manik",
    "Lamat",
    "Muluc",
    "Oc",
    "Chuwen",
    "Eb'",
    "B'en",
    "Ix",
    "Men",
    "K'ib",
    "Kab'an",
    "Etz'nab'",
    "Kawak",
    "Ajaw",
]

DAYNUMBER = range(0, 14)


# Quiero ahora construir un metodo que sea next_day que me devuelva el proximo dia sobre el TzolkinDay
# Los metodos no se pueden escribir sueltos como si fueran funciones, no son tan modulares. Deben ser escritas
# dentro de clases.
class TzolkinDay:
    def next_day(self) -> "TzolkinDay":
        next_day_name = indicar_siguiente_Tzolkin_dayname(self.day_name)
        next_day_number = iterar_numeros_1_al_13(self.day_number)
        return TzolkinDay(next_day_name, next_day_number)

    def __init__(self, day_name: str, day_number: int):
        if day_number > 13:
            raise Exception("Day number is above permitted")
        if day_name not in DAYNAME:
            raise Exception("Day name is not correct")
        self.day_name = day_name
        self.day_number = day_number

    def __str__(self):
        return f"El dia es {self.day_name}, en {self.day_number}"


DAYNAME_LAST_ITEM = len(DAYNAME) - 1


def indicar_siguiente_Tzolkin_dayname(Tzolkin_dayname: str) -> str:  # type: ignore
    # primero chequear si el string esta en la lista de str DAYNAME
    if Tzolkin_dayname in DAYNAME:
        Tzolkin_index = DAYNAME.index(Tzolkin_dayname)
        if Tzolkin_index < DAYNAME_LAST_ITEM:
            nextTzolkin_index = Tzolkin_index + 1
            return DAYNAME[nextTzolkin_index]
        elif Tzolkin_index == DAYNAME_LAST_ITEM:
            return DAYNAME[0]
    else:
        raise Exception("Por favor ingresa un nombre de dia valido")


def iterar_numeros_1_al_13(numero_iterado: int) -> int:  # type: ignore
    if numero_iterado <= 0 or numero_iterado > 13:
        raise Exception("Tenes que ingresar un numero positivo, del 1 al 13")
    elif numero_iterado == 13:
        return 1
    elif numero_iterado <= 12:
        return numero_iterado + 1


# print(iterar_numeros_1_al_13(numero_iterado=2))
# # Es correcto que el programa estalle cuando le ingreso 0, un num menor = a 0, o un num mayor a 13
# # print(iterar_numeros_1_al_13(numero_iterado=0))
# print(iterar_numeros_1_al_13(13))
# # print(iterar_numeros_1_al_13(-2))
# # print(iterar_numeros_1_al_13(15))


today = TzolkinDay("Ajaw", 12)
tomorrow = TzolkinDay(day_name="Kawak", day_number=8)
print(today.day_number)
print(tomorrow.day_name)
myTzolkinDay = today.next_day()
print(myTzolkinDay)

# indicar_siguiente_Tzolkin_dayname("Oc")

# I need a program that transforms seconds into whole hours, whole minutes and the remainder in seconds.
# Yo quiero transformar mis segundos en horas. Para eso, puedo partir de la base de que se que 1h tiene 60min, y 60min son 3600 segundos.


def seconds_into_hours_yami():
    seconds = 14926
    minutes = seconds // 60
    hours = minutes // 60
    final_seconds = int(seconds % minutes % hours)
    print(f"{seconds} seconds is the same as")
    print(f"{hours} hours, {minutes} minutes, and {final_seconds} seconds")


seconds_into_hours_yami()


def same_operation_brilliant():
    seconds = 14926
    hours = seconds // 3600
    # Se enfoca en 2 aspectos de la misma ecuacion
    leftover_seconds = seconds % 3600  # Se enfoca en 2 aspectos de la misma ecuacion
    # Abajo esta convirtiendo el remanente de la operacion de arriba a minutos
    minutes = leftover_seconds // 60
    final_seconds = leftover_seconds % 60
    print(f"{seconds} seconds is the same as")
    print(f"{hours} hours, {minutes} minutes, and {final_seconds} seconds")


same_operation_brilliant()

# def remainder_seconds():
#     seconds = 14926
#     remainder = seconds % 60
#     print(remainder)
# remainder_seconds()

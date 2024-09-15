def calcular_sueldo(nombre, costohora, cantidadhoras):
    sueldo = costohora * cantidadhoras
    print(nombre, "trabajó", cantidadhoras, "horas y cobra un sueldo de", sueldo)


# Bloque principal

calcular_sueldo("juan", 10, 120)  # Argumentos posicionales
calcular_sueldo(costohora=12, cantidadhoras=40, nombre="ana")  # Argumentos nombrados
calcular_sueldo(cantidadhoras=90, nombre="luis", costohora=7)  # Argumentos nombrados en diferente orden

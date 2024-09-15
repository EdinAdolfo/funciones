def mostrar_mayor(v1, v2, v3):
    if v1 > v2 and v1 > v3:
        print("El valor mayor de los tres números es:", v1)
    elif v2 > v3:
        print("El valor mayor de los tres números es:", v2)
    else:
        print("El valor mayor de los tres números es:", v3)

def cargar():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    valor3 = int(input("Ingrese el tercer valor: "))
    mostrar_mayor(valor1, valor2, valor3)

# Programa principal
cargar()

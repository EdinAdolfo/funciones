def cargar():
    lista = []
    for x in range(10):
        valor = int(input("Ingrese valor: "))
        lista.append(valor)
    return lista


def imprimir(lista):
    for x in range(len(lista)):
        if x == len(lista) - 1:
            print(lista[x])  # Evita la coma al final
        else:
            print(lista[x], end=", ")


# Bloque principal

lista = cargar()
imprimir(lista)

def mayormenor(lista):
    may = lista[0]
    men = lista[0]
    for x in range(1, len(lista)):
        if lista[x] > may:
            may = lista[x]
        elif lista[x] < men:
            men = lista[x]
    print("El valor mayor de la lista es", may)
    print("El valor menor de la lista es", men)

# Bloque principal

lista = []
for x in range(5):
    valor = int(input("Ingrese valor: "))
    lista.append(valor)

mayormenor(lista)

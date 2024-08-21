lista = list (["hola", "Jovanna", 1977, 21, 12, True])
# Nos devuelve la longitud de la listas (cantidad de caracteres)
cadena ="hola"
resultado = len(lista)
#Agregando un elemento a la lista
lista.append(4)#Agregué el #4
#Agregando un elemento a una posicion especifica
lista.insert(2, False)
#Agregando varios elementos en la lista
lista.extend([1980])# Elimine me gusta bailar
#Eliminando un elemento de la lista
print(len(lista))
lista.pop(0)
print(len(lista))
print(lista)
lista.pop(-1)
#Eliminando un elemento de la lista por su valor
#lista.remove("Sagitario")
#lista.sort()
print(lista)
#lista.sort(reverse=True)
#Verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(14)
print(elemento_encontrado)
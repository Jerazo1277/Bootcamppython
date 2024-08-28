#Ejemplo de como funcionan los iteradores
#Crear una lista con algunos números
my_list = [1, 2, 3, 4]
#Obtener el iteador de la lista
#Uni iterador es un objeto que nos permite recorrer una colección (como una lista) uno por uno
my_iter = iter(my_list)
#Usar el iterador para acceder a los elementos de la lista
#la función next() nos da el siguiente elemento en la colección cada vez que se llama
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#print(next(my_iter))
text = "Hola mundo"
#crear un iterador
#Un iterador nos permite recorrer cada caracter de una cadena uno por uno
iter_text = iter(text)
#Iterar sobre cada caracter de la cadena usando un bucle for
for char in iter_text:
    print(char)
#Crear un iterador de una lista
#range(1, limit+1, 2) genera números comenzando en 1, con saltos de 2, hasta llegar a 9 (el límite no se incluye)
odd_iter = iter(range(1, 10, 2))
#usar el iterador para recorrer y mostrar cada número impar generado
for num in odd_iter:
    print(num)
#Definir un iterador con un generador
def my_generator():
    #La palabra clave yield nos permite retornar un valor en cada llamada
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
#Crear un iterador a partir de un generador
for value in my_generator():
    print(value)
    #Fibonacci
    #La serie de Fibonacci es una secuencia de números en la que el siguiente siempre es la suma de los dos anteriores
    #los dos anteriores de la serie son [0 1 1 2 3 5 8 13 . . .]
    #La función next() nos permite obtener el siguiente número de la serie
        #usar un bucle for para iterar sobre los valores generados
for value in my_generator():
    print(value)
#Fibonacci
#La serie de Fibonacci hace referencia a que vamos a obtener un valor sumando 
#los dos anteriores [0 1 1 2 3 5 8 13 ...]
def fibonacci(limit):
    #inicializar los dos primero números de la secuencia de Fibonacci
    a, b = 0, 1.
    #Continuar generando números mientras 'a' sea menor que el límte
    while a < limit:
        yield a #Devolver el valor actual de 'a' y pausar la ejecución de la función
        a, b = b, a + b 
for num in fibonacci(10):
    print(num)
        

#La l�gica de orden superior en inteligencia artificial se refiere a la capacidad de tratar funciones como ciudadanos de primera clase. Esto significa que 
#puedes pasar funciones como argumentos a otras funciones, devolver funciones desde funciones, y almacenar funciones en variables. Esto es una caracter�stica 
#fundamental en muchos lenguajes de programaci�n, incluido Python, y es especialmente �til en la programaci�n funcional y en la construcci�n de algoritmos m�s 
#flexibles y gen�ricos.
#Un ejemplo sencillo de l�gica de orden superior en Python es el uso de funciones lambda (funciones an�nimas) y funciones de orden superior como map() y filter(). 
#Estas funciones pueden tomar otras funciones como argumentos.


#Ejemplo 1: Usando map() con una funci�n de orden superior en Python:
# Funci�n de orden superior
#En este ejemplo, la funci�n cuadrado es una funci�n de orden superior porque puede aplicarse a una lista de n�meros utilizando map().


def cuadrado(x):
    return x ** 2

# Lista de n�meros
numeros = [1, 2, 3, 4, 5]

# Aplicar la funci�n de orden superior a cada elemento de la lista usando map()
resultados = list(map(cuadrado, numeros))

print(resultados)


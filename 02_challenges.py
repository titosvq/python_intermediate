### Retos de programación ###

# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

def fizzbuzz():

    my_range = range(1, 101)

    for i in my_range:
        if i %3 == 0 and i %5 == 0:
            print("fizzbuzz")

        elif i %3 == 0:
            print("fizz")

        elif i %5 == 0:
            print("buzz")

        else:
            print(i)

fizzbuzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def anagrama(palabra1, palabra2):
    if palabra1.lower() == palabra2.lower():
        return False
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

print(anagrama("amor", "amor"))

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    
    init = 0
    next = 1
    
    for index in range(0, 50):
        print(init)
        fib = init + next
        init = next
        next = fib

fibonacci()

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def es_primo():

    for num in range(1, 101):

        if num >= 2:
            
            is_divisible = False
        
            for index in range(2, num):
                if num % index == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(num)

es_primo()

def comp_primo(numero):

    if numero < 2:
        return False    

    for index in range(2, numero):
        if numero % index == 0:
            return False
        
    print(f'El número {numero} es primo')
    
comp_primo(7)

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse(text):
    
    text_len = len(text)
    reversed_text = ""
    for i in range(0, text_len):
        reversed_text += text[text_len - i - 1]
    
    return reversed_text

print(reverse("Chiquillo"))
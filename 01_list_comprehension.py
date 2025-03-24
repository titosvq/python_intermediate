### Compresión de Listas ###

# Una forma de crear listas de forma rápida o en base a listas que ya tenemos

my_original_list = [36, 36, 37, 6, 3, 63, 61]

my_list = [i for i in my_original_list]
print(my_list)

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_list = [i for i in range(8)] # Creamos rápidamente una lista del 0 al 7
print(my_list)

my_range = range(50)
print(list(my_range))
print(range(10))

my_list = [i + 3 for i in range(8)]
print(my_list)

my_list = [i * 3 for i in range(8)]
print(my_list)

my_list = [i * i for i in range(8)]
print(my_list)

def sum_five(num):
    return num + 5

my_list = [sum_five(i) for i in range(10)]
print(my_list)
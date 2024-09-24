# Tuplas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.66, "Andres", "Cebrian")
my_other_tuple = (30, 50, 43, 62, 12)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[3])
print(my_tuple[-2])
#print(my_tuple[6]) Out of range

print(my_tuple.count(35)) # Imprime numero de veces que aparece el elemento
print(my_tuple.index("Andres")) # Situa posición

# my_tuple[1] = 1.9 # No funciona porque las tuplas son cerradas una vez declaradas
# print(my_tuple)

print(my_tuple + my_other_tuple) # Concatena tuplas
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[1:3]) # Escribimos solo el intervalo de la tupla

del my_tuple # Te cargas la variable
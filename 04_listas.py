# Listas (esto ya empieza a molar)

my_list = list() # Solo admite un argumento, y lo divide por caracteres
my_other_list = []

print(len(my_list))

my_list = [1,2,5,8, 43, 2 , 67]

print(my_list) # Imprimo toda la lista
print(my_list[3]) # Imprimo el elemento en posición 3 de la lista
print(my_list[-1])
print(my_list[-3])
# print(my_list[12]) Esto sí da error (Fuera de rango)
# print(my_list[-10]) Tb se sale de rango

my_other_list = [42, 1.90, "Andres", "Cebrian"] # Una lista NO tiene que tener todas las variables del mismo tipo
print(type(my_other_list)) # El tipo es lista
print(type(my_other_list[2])) # El tipo es string

print(my_other_list.count("Andres")) # Cuenta numero de veces que aparece en la lista el argumento

edad, altura, nombre, apellidos = my_other_list # Extraes valores de la lista a variables sencillas
print(edad)
print(nombre)

altura, edad, apellidos, nombre = my_other_list[1], my_other_list[0], my_other_list[3], my_other_list[2]
print(edad)
print(nombre)

my_final_list = my_list + my_other_list
print(my_final_list) # Concatenas listas
print(len(my_final_list))

# Añadir y quitar elementos
my_other_list.append("Utrillas") # Añades elemento
print(my_other_list)

my_other_list.insert(1, "Azul") # Añade elemento en la posición que queramos
print(my_other_list)

my_other_list[1] = "Verde" # Cambio el elemento en la posición dentro de la lista
print(my_other_list)

my_other_list.remove("Verde") # Elimino elemento que coincida
del my_other_list[2] # Elimino elemento por posición
# my_list.remove("Azul") # Dará error al no encontrar dicho elemento
print(my_other_list)

my_list.pop() # Elimino el último elemento
my_list.pop(2) # Elimino el elemento en posicion 2, y dice el elemento
my_pop_element = my_list.pop(2) # Lo borra, pero dice el elemento, por lo que podemos guardarlo
print(my_list)
print(my_pop_element)

my_new_list = my_list.copy() # Copia y desvincula
my_newer_list = my_list # Clona y referencia
print(my_new_list)
print(my_newer_list)
print(my_list)

my_list.clear() # Vacio la lista
print(my_new_list) # Como es copia, no afecta el clear
print(my_newer_list) # Como es clon, afecta el clear
print(my_list)


# Cosas chapuceras
my_list = "Hola caracola" # Deja de ser una lista
print(my_list)
print(type(my_list))

my_list = list("Hola caracola") # Vuelve a ser una lista donde cada letra es un elemento
print(my_list)
print(type(my_list))

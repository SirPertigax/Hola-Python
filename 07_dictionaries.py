# Diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Andres", "Apellido":"Cebrian", "Edad":35, 1:"Python"} # Creamos pares clave/valor

my_dict = {
    "Nombre":"Andres", 
    "Apellido":"Cebrian", 
    "Edad":35, 
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict)) # La longitud es el numero de claves, no de registros
print(len(my_dict))

print(my_other_dict["Nombre"])
print(my_dict["Lenguajes"]) # No pones el index, pones la clave, y arroja el valor

my_dict["Nombre"] = "Maria Luisa" # Cambias el valor
print(my_dict["Nombre"])

my_dict["Ciudad"]= "Utrillas" # Añadimos campo al diccionario
print(my_dict)

del my_dict["Ciudad"] # Eliminamos campo
print(my_dict)

print("Apellido" in my_dict) # Nos dice si está el elemento
print(my_dict["Apellido"])
print("Ciudad" in my_dict)

print(my_dict.items()) # Te da campo y valor emparejados
print(my_dict.keys()) # Te da los campos en forma de LISTA
print(my_dict.values()) # Te da los valores en forma de LISTA

my_third_dict = my_dict.fromkeys(("Nombre", 1)) # Creamos un nuevo diccionario con los campos extraidos de un diccionario anterior
print(my_third_dict)

my_list = ["Nombre", "Apellido", "Ciudad", "Lenguaje"] 
my_other_dict = dict.fromkeys(my_list) # Puedo utilizar una lista para abrir los campos
print(my_other_dict)

my_third_dict = my_dict.copy() # Copio diccionario
print(my_third_dict)

my_third_dict = dict.fromkeys(my_dict) # Copio diccionario, pero con los campos vacios
print(my_third_dict)

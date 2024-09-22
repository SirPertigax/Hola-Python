# Variables

my_string_variable = "Utrillas"
print(my_string_variable)

my_int_variable = 3
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables dentro de una cadena
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:" , my_bool_variable)

# Extensión de la variable
print(len(my_string_variable))

# Declarar variables en una sola linea ¡Cuidado con abusar!
name, surname, alias, edad = "Andres", "Cebrian", "Turilly", 42
print("Me llamo", name, surname,". Mi edad es", edad, "y mi alias es:", alias)

# Inputs en consola
"""
first_name = input("Cual es tu nombre?")
edad_usuario = input("Cual es tu edad?")

print("Hola", first_name)
print("Tu edad es ", edad_usuario)
print(type(edad_usuario)) # El tipo de variable de un input es string
int_edad_usuario = int(edad_usuario) # Puedes convertir una string a int
print(type(int_edad_usuario)) # Saldrá int

"""

# Cambiamos tipos
name = 42
age = "Andres"
print(type(name))
print(type(age))

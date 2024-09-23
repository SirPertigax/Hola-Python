# Strings

my_string = "Mi cadena"
my_other_string = "Mi otra cadena"

print(len(my_string)) # Longitud de la cadena

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\nEsta es la otra parte" # Hacemos salto de linea

print(my_new_line_string)
print(my_string +"\n" + my_other_string)

my_tab_string = "\tEste es un string con tabulación" # Meter tabulación a la cadena
print(my_tab_string)

# Formateo cadenas

name = "Andrés"
surname = "Cebrián"
edad = 42

print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(edad)) # No recomendado
print("Mi nombre es {} {} y mi edad es {}". format(name, surname, edad)) # Esta es la más fácil
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, edad)) # Esta se asegura que las variables son del tipo deseado
print(f"Mi nombre es {name} {surname} y mi edad es {edad}") # Esta es la que vamos a usar


# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(d)

# División
language_slice = language[1:3] # Imprime posiciones 1 y 2
print(language_slice)

language_slice = language[1:] # Imprime posiciones del 1 hasta el final
print(language_slice)

language_slice = language[:3] # Imprime posiciones del 2 al principio
print(language_slice)

language_slice = language[0:6:2] # Imprime el rango, contando según el tercer número
print(language_slice)

# Reverse
reversed_language = language[::-1] # Le das la vuelta a la cadena
print(reversed_language)

# Funciones del sistema
print(len(language)) # Longitud de la cadena
print(language.capitalize()) # Pone en mayuscula el primer carácter
print(language.upper()) # Pone todo en mayusculas
print(language.count("t")) # Cuantos caracteres tiene del mismo tipo que ponemos como argumento
print(language.upper().islower())
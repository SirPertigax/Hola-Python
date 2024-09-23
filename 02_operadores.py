# Operadores aritméticos
print("Operadores aritméticos")
print(3+4) # Suma
print(3-4) # Resta
print(3*4) # Multiplo
print(3/4) # Divisor
print(3//4) # Divide, pero solo da el entero, redondeado hacia abajo
print(10%3) # Resto
print(2**3) # Potencias
print(2**3 + (3 - 7) / 1 //4)

print("Hola" + "Python" + " ¿Qué tal? ") # Concatena cadenas de texto
    # print("Hola" - "Python") # No se pueden restar cadenas de texto
    # print("Hola" + 5) # No se puede trabajar con variables distintas
print("hola" + str(5)) # Transformamos variable int a str
print("hola" * 5) # Se repite la cadena
    # print("hola" * 5.2) # No se puede repetir con float

my_float= 2.5 * 2 # Multiplicar float por int, resulta un float
print("hola" * int(my_float)) 

# Operadores comparativos
print("Operadores comparativos")
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

print("Hola" > "Python") # Compara por ordenación alfabética
print("Hola" < "Python")
print("aaaa" >= "baaa") 
print(len("aaaa") >= len("baaa")) # Compara por longitud
print("Hola" <= "Python")
print("Hola" == "Hala") 
print("Hola" != "Python")

# Operadores lógicos
print("Operadores lógicos")
print (3 < 4 and "Hola" > "Python") 
print (3 < 4 and "Hola" < "Python")
print (3 < 4 or "Hola" > "Python")
print (3 > 4 or "Hola" > "Python")
print (3 < 4 or "Hola" > "Python" and 4 == 4)
print (3 > 4 or "Hola" > "Python" and 4 == 4)
print (3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4)) # Hace la inversa de la condición. La niega
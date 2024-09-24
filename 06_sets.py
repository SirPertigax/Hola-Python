 # Sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Andres", "Cebrian", 23, 3} # Lo transformas en un set
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Utrillas")
print(my_other_set) # No está ordenado, te va cambiando los elementos de orden

my_other_set.add("Utrillas")
print(my_other_set) # No admite repetidos, por lo que no añade elemento

print("Utrollas" in my_other_set) # Nos dice si está o no el elemenjto

my_other_set.remove("Utrillas")
print(my_other_set)

my_other_set.clear() # Vacias el set
print(my_other_set)

# del my_other_set # Te cargas la variable, no la vacias

my_other_set = {"C#", "Python", "HTML"}
my_set = {"Zbrush", "Blender", "Fusion"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)

my_new_set = my_new_set.union({"Photoshop", "Illustrator"})
print(my_new_set)

print(my_new_set.difference(my_set))

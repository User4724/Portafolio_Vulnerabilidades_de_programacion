#Como crear un array
#Se puede crear vacio
cars = []
#Se puede crear con elementos o strings como se muetra abajo
cars = [3, 5, 0, "Hola"]

print(cars)

#Obtener una longitud 
longitud_array = len(cars)
print(longitud_array)

#Eliminar una posicion
cars.pop(1) #Elemento 1 era el numero 5 ahora solo queda 3, 0, "Hola"
print(cars)

#Eliminar un elemnto
cars.remove("Hola")
print(cars)
#Ahora se ha eliminado la palabra Hola

#Añadir un elemento al final
cars.append("Adios")
print(cars)

#Modificar un elemento en una posicion especifica
cars[0] = "Hola" #Va a quitar lo que hani en esa posicion y agregara la palabra Hola
print(cars)
#El resultado es Hola, 0, Adios


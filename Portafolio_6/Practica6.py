#Diccionarios
#Iniciar
mi_diccionario = {
    "clave1" : "ValorA",
    "clave2" : "ValorB",
    "clave3" : "ValorC",
    "claveX" : [1,2,3]
}
diccionario = dict([("clave1", "valor1"), ("clave2", "valor2")])

print(mi_diccionario)

#Añadir / Modificar

mi_diccionario["claveY"] = "hola"
mi_diccionario.update({"clave1": "valorAAA"})
print(mi_diccionario)

#Eliminar
mi_diccionario.pop("clave2", "error") #Sino existe clave2 arrojara "error"
mi_diccionario.popitem()

print(mi_diccionario)
print(mi_diccionario.items())
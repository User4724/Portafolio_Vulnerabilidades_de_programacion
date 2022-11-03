#Variables=Las variables son apartados donde se guarda informacion
#texto = "repaso de python"
#nombre = "Omar"
#altura = "174"
#year = "2022"

#Concatenacion es la forma de unir  e imprimir todo de un golpe
#vamos a concatenar pero como existen numeros tendremos que gragar un string
#para que no arroje ningun error 
#print(f"(texto) - (nombre) - (altura) - (str(year)")
#print(texto + " - " + nombre + " - " + altura + " - " + str(year))
#Se puede concatener con el simbolo mas como se presenta en el texto anterior

#Se puede concatenar dentro de una variable su sitio web
#Tambien llamado ENTRADA DE DATOS el cual esperara una respuesta
#Ejemplo:

#sitioweb = input("¿Cual es tu pagina web?: ")

#Se ha guardado la inforacion dentro de la funcion la cual 
#podremos visualizar al realizar una impresion de sitioweb

#print("El sitio web del usuario es: " + sitioweb)

#Condicionales permiten elegir entre ejecuciones por ejemplo si(hace frio) entonces pone una chamarra
#variable

#altura = int(input ("¿Cual es tu altura?"))

#if altura >= 174:
#    print("Eres una persona promedio")
#else: 
#    print("Eres bajito")



#Funciones 
#Se puede agregar una salida (que siempre es lo mejor para que no se quede dentro la informacion) en este caso sera un return

#def mostraraltura():
 #   altura = int(input("¿Cual es tu altura?: "))

  #  if altura >= 174:
       # 174print("Eres una persona promedio")
#    else: 
      #  print("Eres bajito")

#mostraraltura()

# 
# Creacion de Listas
#Para seleccionar a una persona lo haremos de la siguiente manera
#Aqui se muestran 3 variables dentro de una misma
#Ingresaremos el bucle for para imprimir como lista, asi repetir la serie de instrucciones hasta que se cumpla la condicion

personas = ["Omar", "Laura", "Andy"]

print(personas[0]) 

for personas in personas:
    print(personas)


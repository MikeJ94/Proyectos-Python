
#Proyecto #1 

#Declaracion de una Variable tipo Cadena
organizacion = "DevLoops" 

# 3 Maneras para Concatenar una Cadena de Caracteres:
#1 Usando el Simbolo +
#print ("Aprender a programar con " + organizacion)
#2 Usando la palabra reservada format
#print ("Aprende a programar con {}".format(organizacion))
#3 Usando f-string (EL MAS USADO)
#print (f"Aprende a programar con {organizacion}")

#Comienzo del Proyecto Mad Libs

#Paso 1. Pedir los Atributos al Usuario
adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo (Plural): ")

#Paso 2. Concatenamos los Valores digitados por el usuario a una Cadena guardada en una variable.
madlib = f"¡Programar es {adj}! Siempre me emociona porque me encanta {verbo1} problemas. \
    ¡Aprende a {verbo2} con DevLoops y alcanza tus {sustantivo_plural}!"

#Paso 3. Mandamos a Imprimir en Pantalla
print(madlib)
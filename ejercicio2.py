'''
Ejercicio 2

Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos... Transforma este texto:
un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro
En este otro:
Un día que el viento soplaba con fuerza...
- Mira como se mueve aquella banderola -dijo un monje.
- Lo que se mueve es el viento -respondió otro monje.
- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.

Lo único prohibido es modificar directamente el texto.

'''
# Función auxiliar para formatear las tres últimas frases del texto.
def aux_formatear_texto(texto_mayuscula, i): 
    #print(len(texto_mayuscula))
    if i == len(texto_mayuscula) -1:
        return "- " + texto_mayuscula[i] + ".\n"  
    else:
        return "- " + texto_mayuscula[i] + ".\n" + aux_formatear_texto(texto_mayuscula, i+1)

# Función principal para formatear el texto.
def formatear_texto(texto):   
    # Método split para convertir una cadena en uns lista, utilizando un separador en este caso #. 
    texto_separado = texto.split("#") 
    # Método capitalize() nos permite tranformar la primera letra en mayúscula.
    texto_mayuscula = [i.capitalize() for i in texto_separado] 
    # A la primera frase que se encuentra en la posición 0 de nuestro texto le añadimos tres puntos.
    texto_mayuscula[0] += "...\n"
    # Nos devuelve la primera frase del texto (con letra mayúscula y tres puntos al final) + el resto del texto ya formateado con la función auxiliar.
    return texto_mayuscula[0] + aux_formatear_texto(texto_mayuscula,1)

texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella bandolera -dijo un monje#lo que es el viento -respondió otro monje#ni las bandoleras ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

# Imprimimos por pantalla el texto formateado.
print(formatear_texto(texto))    
    

#t = ["-" + i for i in texto_separado[1:]]
#print(t, end = "\n")

# Poner primera letra de cada frase en mayúscula.
#mayuscula = [i.capitalize() for i in texto_separado]
#print(mayuscula, end = "\n")

# Forma 1 eliminar #:

# caracter_eliminar = "#"
#texto = "".join(x for x in texto if x not in caracter_eliminar)
#print(texto)

# Forma 2 eliminar #:

#for x in range(len(caracter_eliminar)):
    #texto = texto.replace(caracter_eliminar[x], "")
#print(texto)


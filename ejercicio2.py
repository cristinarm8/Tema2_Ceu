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

texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella bandolera -dijo un monje#lo que es el viento -respondió otro monje#ni las bandoleras ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

# Forma 1 eliminar #:

caracter_eliminar = "#"
texto = "".join(x for x in texto if x not in caracter_eliminar)
print(texto)

# Forma 2 eliminar #:

for x in range(len(caracter_eliminar)):
    texto = texto.replace(caracter_eliminar[x], "")
print(texto)

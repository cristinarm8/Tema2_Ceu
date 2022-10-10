'''
Ejercicio 3

Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:
Borrar los elementos duplicados.
Ordenar la lista de mayor a menor.
Eliminar todos los números impares.
Realizar una suma de todos los números que quedan.
Añadir como primer elemento de la lista la suma realizada.
Devolver la lista modificada.

Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:
nueva_lista = modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )
True

Recordatorio
La función sum(lista) devuelve una suma de los elementos de una lista.

'''

lista = [2,5,1,12,7,8,3,8,6,4,2,5,3,12]

def modificar(lista:list):

    # Borrar elmentos duplicados
    lista_nueva = list(set(lista))
    #return print(lista_nueva)

    # Ordenar la lista de mayor a menor
    lista_nueva = sorted(lista_nueva, reverse = True)
    print(f"Lista ordenada de mayor a menor: {lista_nueva}")

    # Eliminar todos los números impares
    lista_ordenada_pares = []

    for i in lista_nueva:
        if i % 2 == 0:
            lista_ordenada_pares.append(i)
    print(f"Lista con elementos pares: {lista_ordenada_pares}")

    # Realizar una suma de todos los números que quedan.
    suma_elementos_lista = sum(lista_ordenada_pares)
    print(f"La suma de los números que conforman la lista es: {suma_elementos_lista}")

    # Añadir como primer elemento la lista de la suma realizada.
    lista_ordenada_pares= [suma_elementos_lista] + lista_ordenada_pares
    
    # Devolver la lista modificada.
    return lista_ordenada_pares
    
    # Comprobar que la suma de todos los números a partir del segundo, concuerda con el primer elemento de la lista.
lista_ordenada_pares = modificar(lista)
print(lista_ordenada_pares[0] == sum(lista_ordenada_pares[1:]))
    
    
'''
    for i in lista:
        if i not in lista_nueva:
            lista_nueva.append(i)
    print(f"Lista con elementos duplicados eliminados: {lista_nueva}")
 '''


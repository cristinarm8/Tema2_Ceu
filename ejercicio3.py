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
'''
lista = [2,5,1,12,7,8,3,8,6,4,2,5,3,12]

def modificar(lista:list):

    # Borrar elmentos duplicados
    lista_nueva = list(set(lista))
    print(f"Lista nueva con los elementos duplicados eliminados: {lista_nueva}")

    # Ordenar la lista de mayor a menor
    lista_nueva = sorted(lista_nueva, reverse = True)
    print(f"Lista ordenada de mayor a menor: {lista_nueva}")

    # Eliminar todos los números impares
    lista_ordenada_pares = []

    for i in lista_nueva:
        if i % 2 == 0:
            lista_ordenada_pares.append(i) # Añadir elemento sólo si es par. Así no incluyes los impares en tu nueva lista.
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
# Ejercicio realizado con clases:

class Modificar:

    # Método contructor.
    def __init__(self, lista):
        self.lista = lista

    # Método para borrar elementos duplicados.
    def borrar_duplicados(self):
        return list(set(self.lista))

    # Método para ordenar la lista de mayor a menor.
    def ordenar_lista(self):
        return sorted(self.borrar_duplicados(), reverse = True)

    # Método para eliminar todos los números impares.
    def eliminar_num_impares(self):
    
        lista_ordenada_pares = []
        '''
        for i in self.ordenar_lista():
            if i % 2 == 0:
                lista_ordenada_pares.append(i)
        return lista_ordenada_pares
        '''
        return [lista_ordenada_pares.append(i) for i in self.ordenar_lista() if i % 2 ==0]

    # Método para realizar la suma de todos los números que quedan.
    def sumar_elementos_lista(self):
        return sum(self.eliminar_num_impares())

    # Método para añadir como primer elemento de la lista la suma realizada.
    def añadir_elemento_lista(self):
        return [self.sumar_elementos_lista()] + self.eliminar_num_impares()

lista = [2,5,1,12,7,8,6,4,2,5,3,12]

# Creación de un objeto / instancia de clase.
lista_final = Modificar(lista)

print(f"Lista: {lista_final.borrar_duplicados()}")
print(f"Lista ordenados:{lista_final.ordenar_lista()}")
print(f"Lista sin impares: {lista_final.eliminar_num_impares()}")
print(f"Suma de los números que conforman la lista: {lista_final.sumar_elementos_lista()}")
print(f"Lista con suma al inicio: {lista_final.añadir_elemento_lista()}")

# Comprobación que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista.
nueva_lista = lista_final.añadir_elemento_lista()
print(nueva_lista[0] == sum(nueva_lista[1:]))




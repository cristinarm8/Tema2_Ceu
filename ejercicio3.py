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
        return [i for i in self.ordenar_lista() if i % 2 == 0]

        # Otra opción: 
        #for i in self.ordenar_lista():
            #if i % 2 == 0:
                #lista_ordenada_pares.append(i)
        #return lista_ordenada_pares
        
    # Método para realizar la suma de todos los números que quedan.
    def sumar_elementos_lista(self):
        return sum(self.eliminar_num_impares())

    # Método para añadir como primer elemento de la lista la suma realizada.
    def añadir_elemento_lista(self):
        return [self.sumar_elementos_lista()] + self.eliminar_num_impares()

lista = [2,5,1,12,7,8,6,4,2,5,3,12]

# Creación de un objeto / instancia de clase.
lista_final = Modificar(lista)

# Lista modificada
nueva_lista = lista_final.añadir_elemento_lista()

# Imprimimos por pantalla resultados.
print(f"Lista nueva con los elementos duplicados: {lista_final.borrar_duplicados()}")
print(f"Lista con elementos ordenados de mayor a menor: {lista_final.ordenar_lista()}")
print(f"Lista sin impares: {lista_final.eliminar_num_impares()}")
print(f"Suma de los números que conforman la lista: {lista_final.sumar_elementos_lista()}")
print(f"Lista con el resultado de la suma como primer elemento: {lista_final.añadir_elemento_lista()}")

# Comprobación que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista.
#nueva_lista = lista_final.añadir_elemento_lista()
print(nueva_lista[0] == sum(nueva_lista[1:]))




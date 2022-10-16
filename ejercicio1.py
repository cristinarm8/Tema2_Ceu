# Si quisiera utilizar funciones de un archivo que se localiza en otra carpeta.
# import sys
# sys.path.insert(0, direccion_de_carpeta)

#import math
from math import *

class Punto:

    # Método constructor -> método especial. Si no se recibe coordenada parámetro por defecto 0.
    def __init__(self, x_inicial = 0, y_inicial = 0):
        # Atributos de instancia.
        self.x = x_inicial
        self.y = y_inicial
    
    # Método str -> método especial. Nos devuelve una cadena de caracteres con lo que queremos mostrar.
    def __str__(self):
        return ("({},{})".format(self.x, self.y))

    # Método cuadrante que indica a qué cuadrante pertence el punto.
    def cuadrante(self):
        if self.x != 0 and self.y !=0:
            if self.x > 0:
                if self.y > 0:
                    print(f"El punto ({self.x},{self.y}) pertenece al I cuadrante")
                else:
                    print("El punto ({},{}) pertenece al IV cuadrante".format(self.x, self.y))
        
            elif self.y > 0:
                print("El punto ({},{}) pertenece al II cuadrante".format(self.x, self.y))
            else: 
                print("El punto ({},{}) pertenece al III cuadrante".format(self.x, self.y))
        
        elif self.x != 0 and self.y == 0:
            print("El punto ({},{}) está en el eje X".format(self.x, self.y))
        
        elif self.x == 0 and self.y != 0:
            print("El punto ({},{}) está en el eje Y".format(self.x, self.y))

        else:
            print("El punto ({},{}) está en el origen".format(self.x, self.y))


    # Método vector que calcula el vector resultante entre los dos puntos.
    def vector(self, pto_nuevo):
        #nueva_x = self.x - pto_nuevo.x
        #nueva_y = self.y - pto_nuevo.y
        return Punto((self.x - pto_nuevo.x), (self.y - pto_nuevo.y))   

    # Método distancia, que tome otro punto y calcule la distancia entre los dos puntos.

    # Opción 1:

    #def longitud(self):
        #return sqrt((self.x)**2 + (self.y)**2)
    
    #def distancia(self, pto_nuevo):
        #return self.vector(pto_nuevo).longitud

    # Opción 2:
    def distancia(self, pto_nuevo):
        #x_distancia = (pto_nuevo.x - self.x) **2 # Resto la x del punto nuevo con la x del punto incial.
        #y_distancia = (pto_nuevo.y - self.y) **2 # Resto la y del punto nuevo con la y del punto inicial.
        return sqrt(((pto_nuevo.x - self.x)**2) + ((pto_nuevo.y- self.y)**2)) # Sumo los cuadrados y hago la raíz de todo ello.

class Rectangulo:

    # Método constructor -> método especial. 
    def __init__(self, p_inicial = Punto(), p_final = Punto()):
        self.p_inicial = p_inicial
        self.p_final = p_final

    # Método que muestra la base.
    def base(self):
        return abs(self.p_final.x - self.p_inicial.x)
    
    # Método que muestra la altura.
    def altura(self):
        return abs(self.p_final.y - self.p_inicial.y)

    # Método que muestra el área.    
    def area(self):
        return self.base() * self.altura()


# Creación punto A
A = Punto(2,3)
print(f"El punto A está formado por las siguiente coordenadas: {A}")
# Conocer en qué cuadrante se encuentra el punto A.
A.cuadrante()

# Creación punto B
B = Punto(5,5)
print(f"El punto B está formado por las siguiente coordenadas: {B}")

# Creación punto C
C = Punto(-3,-1)
print(f"El punto C está formado por las siguientes coordenadas: {C}")
# Conocer en qué cuadrante se encuentra el punto C.
C.cuadrante()

# Creación punto D
D = Punto(0,0)
print(f"El punto D está formado por las siguientes coordenadas: {D}")
# Conocer en qué cuadrante se encuentra el punto D.
D.cuadrante()

# Vector AB
vector_AB = A.vector(B)
print(f"El vector AB es el siguiente:{vector_AB}")

# Vector BA
vector_BA = B.vector(A)
print(f"El vector BA es el siguiente: {vector_BA}")

# Distancia entre los puntos A y B
distancia_entre_puntos_AB = A.distancia(B)
print(f"La distancia entre los puntos A y B es: {distancia_entre_puntos_AB}")

# Distancia entre los puntos B y A
distancia_entre_puntos_BA = B.distancia(A)
print(f"La distancia entre los puntos B y A es: {distancia_entre_puntos_BA}")

# Determinar cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
distanciaA_con_origen = A.distancia(Punto())
#print(distanciaA_con_origen)

distanciaB_con_origen = B.distancia(Punto())
#print(distanciaB_con_origen)

distanciaC_con_origen = C.distancia(Punto())
#print(distanciaC_con_origen)

distancia_origen = max(distanciaA_con_origen, distanciaB_con_origen, distanciaC_con_origen)
#print(distancia_origen)

if distanciaA_con_origen == distancia_origen:
    print(f"El punto A es el que se encuentra más lejos del origen a una distancia de {distanciaA_con_origen}")

elif distanciaB_con_origen == distancia_origen:
    print(f"El punto B es el que se encuentra más lejos del origen, a una distancia de {distanciaB_con_origen}")

else:
    print(f"El punto C es el que se encuentra más lejos del origen, a una distancia de {distanciaC_con_origen}")

# Creación rectángulo
rectangulo = Rectangulo(A,B) 

# Creción base
base_rectangulo = rectangulo.base()
print(f"La base del rectángulo es: {base_rectangulo}")
# Creación altura
altura_rectangulo = rectangulo.altura()
print(f"La altura del rectángulo es: {altura_rectangulo}")
# Creación área
area_rectangulo = rectangulo.area()
print(f"El área del rectángulo es: {area_rectangulo}")

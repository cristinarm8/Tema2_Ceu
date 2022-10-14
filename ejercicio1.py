#import math

from math import *

class Punto:

    # Método constructor. Si no se recibe coordenada parámetro por defecto 0.
    def __init__(self, x_inicial = 0, y_inicial = 0):
        self.x = x_inicial
        self.y = y_inicial
    
    def __str__(self):
        return ("({},{})".format(self.x, self.y))

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
            print(f"El punto está en el eje X")
        
        elif self.x == 0 and self.y != 0:
            print(f"El punto está en el eje Y")

        else:
            print(f"El punto está en el origen")


    def vector(self, pto_nuevo):
        nueva_x = self.x - pto_nuevo.x
        nueva_y = self.y - pto_nuevo.y

        return Punto(nueva_x, nueva_y)   

    #def longitud(self):
        #return math.sqrt((self.x)**2 + (self.y)**2)

    def distancia(self, pto_nuevo):
        #x_distancia = (pto_nuevo.x - self.x) **2 # Resto la x del punto nuevo con la x del punto incial.
        #y_distancia = (pto_nuevo.y - self.y) **2 # Resto la y del punto nuevo con la y del punto inicial.

        return sqrt(((pto_nuevo.x - self.x)**2) + ((pto_nuevo.y- self.y)**2)) # Sumo los cuadrados y hago la raíz de todo ello.

class Rectangulo:

    def __init__(self, p_inicial = Punto(), p_final = Punto()):
        self.p_inial = p_inicial
        self.p_final = p_final

    def base(self):
        return abs(self.p_final.x - self.p_incial.x)
    
    def altura(self):
        return abs(self.p_final.y - self.p_inial.y)

    def area(self):
        return self.base() * self.altura()


A = Punto(2,3)
print(A)
A.cuadrante()

B = Punto(5,5)
print(B)
#B.cuadrante()

C = Punto(-3,-1)
print(C)
C.cuadrante()

D = Punto(0,0)
print(D)
D.cuadrante()

nuevo_vector = B.vector(A)
print(f"El nuevo vector es {nuevo_vector}")

distancia_entre_vectores = C.distancia(A)
print(f"La distancia es: {distancia_entre_vectores}")
    
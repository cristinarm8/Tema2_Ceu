#import sys

#sys.path.insert(0,"C:/Users/crisr/OneDrive/Documentos/GitHub/Tema2_Ceu")

from ejercicio1 import Punto,Rectangulo

if __name__ == "__main__":

    # Creación punto A
    A = Punto(2,3)
    print(A)
    A.cuadrante()

    # Creación punto B
    B = Punto(5,5)
    print(B)

    # Creación punto C
    C = Punto(-3,-1)
    print(C)
    C.cuadrante()

    # Creación punto D
    D = Punto(0,0)
    print(D)
    D.cuadrante()

    # Vector AB
    vector_AB = A.vector(B)
    print(f"El vector AB es el siguiente:{vector_AB}")

    # Vcetor BA
    vector_BA = B.vector(A)
    print(f"El vector BA es el siguiente: {vector_BA}")

    # Distancia entre los puntos A y B
    distancia_entre_puntos_AB = A.distancia(B)
    print(f"La distancia entre los puntos A y B es: {distancia_entre_puntos_AB}")

    # Distancia entre los puntos B y A
    distancia_entre_puntos_BA = B.distancia(A)
    print(f"La distancia entre los puntos B y A es: {distancia_entre_puntos_BA}")

    A.distancia(Punto())
    B.distancia(Punto())
    C.distancia(Punto())

    # Creación rectángulo
    rectangulo = Rectangulo(A,B)

    # Creación base
    base_rectangulo = Rectangulo.base()

    # Creación altura
    altura_rectangulo = Rectangulo.altura()

    # Creación área
    area_rectangulo = Rectangulo.area()




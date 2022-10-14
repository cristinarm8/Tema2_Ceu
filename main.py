import sys

sys.path.insert(0,"C:/Users/crisr/OneDrive/Documentos/GitHub/Tema2_Ceu")

from ejercicio1 import Punto,Rectangulo

if __name__ == "__main__":
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

    vector_AB = A.vector(B)
    print(f"El vector AB es el siguiente:{vector_AB}")

    vector_BA = B.vector(A)
    print(f"El vector BA es el siguiente: {vector_BA}")

    distancia_entre_puntos_AB = A.distancia(B)
    print(f"La distancia entre los puntos A y B es: {distancia_entre_puntos_AB}")

    distancia_entre_puntos_BA = B.distancia(A)
    print(f"La distancia entre los puntos B y A es: {distancia_entre_puntos_BA}")

    B.distancia(Punto())

    rectangulo = Rectangulo(A,B)

# Si quisiera utilizar funciones de un archivo que se localiza en otra carpeta.
#import sys
#sys.path.insert(0,"C:/Users/crisr/OneDrive/Documentos/GitHub/Tema2_Ceu")

# Del archivo ejercicio1 importo las clases Punto y Rectangulo
from ejercicio1 import Punto,Rectangulo 

if __name__ == "__main__":

    # Creación punto A
    A = Punto(2,3)
    # Conocer en qué cuadrante se encuentra el punto A.
    A.cuadrante()

    # Creación punto B
    B = Punto(5,5)
    
    # Creación punto C
    C = Punto(-3,-1)
    # Conocer en qué cuadrante se encuentra el punto C.
    C.cuadrante()

    # Creación punto D
    D = Punto(0,0)
    # Conocer en qué cuadrante se encuentra el punto D.
    D.cuadrante()

    # Vector AB
    vector_AB = A.vector(B)
    print(f"El vector AB es el siguiente:{vector_AB}")

    # Vector BA
    vector_BA = B.vector(A)
    print(f"El vector BA es el siguiente:{vector_BA}")

    # Distancia entre los puntos A y B
    distancia_entre_puntos_AB = A.distancia(B)
    print(f"La distancia entre los puntos A y B es: {distancia_entre_puntos_AB}")

    # Distancia entre los puntos B y A
    distancia_entre_puntos_BA = B.distancia(A)
    print(f"La distancia entre los puntos B y A es: {distancia_entre_puntos_BA}")

    # Determina cual de los 3 puntos A,B o C, se encuentra más lejos del origen, punto(0,0).
    distanciaA_con_origen = A.distancia(Punto())
    #print(distanciaA_con_origen)

    distanciaB_con_origen = B.distancia(Punto())
    #print(distanciaB_con_origen)

    distanciaC_con_origen = C.distancia(Punto())
    #print(distanciaC_con_origen)

    distancia_origen = max(distanciaA_con_origen, distanciaB_con_origen, distanciaC_con_origen)
    #print(distancia_origen)

    if distanciaA_con_origen == distancia_origen:
        print(f"El punto A es el que se encuentra más lejos del origen, a una distancia de {distanciaA_con_origen}")

    elif distanciaB_con_origen == distanciaB_con_origen:
        print(f"El punto B es el que se encuentra más lejos del origen, a una distancia de {distanciaB_con_origen}")

    else:
        print(f"El punto C es el que se encuentra más lejos del origen, a una distancia de {distanciaC_con_origen}")
    
    # Creación rectángulo
    rectangulo = Rectangulo(A,B)

    # Creación base 
    base_rectangulo = rectangulo.base()
    print(f"La base del rectángulo es: {base_rectangulo}")
    # Creación altura
    altura_rectangulo = rectangulo.altura()
    print(f"La altura del rectángulo es: {altura_rectangulo}")
    # Creación área
    area_rectangulo = rectangulo.area()
    print(f"El área del rectángulo es: {area_rectangulo}")



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
                    print(f"El punto ({self.x}, {self.y}) pertenece al IV cuadrante")
        
            elif self.y > 0:
                print(f"El punto pertenece al II cuadrante")
            else: 
                print(f"El punto pertenece al III cuadrante")
        
        elif self.x != 0 and self.y == 0:
            print(f"El punto está en el eje X")
        
        elif self.x == 0 and self.y != 0:
            print(f"El punto está en el eje Y")

        else:
            print(f"El punto está en el origen")


p1 = Punto(2,3)
print(p1)
p1.cuadrante()

p2 = Punto(1,4)
print(p2)
p2.cuadrante()
    
class Punto:

    # Método constructor. Si no se recibe coordenada parámetro por defecto 0.
    def __init__(self, x_inicial = 0, y_inicial = 0):
        self.x = x_inicial
        self.y = y_inicial
    
    def __str__(self):
        return ("({},{})".format(self.x, self.y))

p1 = Punto(2,3)
print(p1)
    
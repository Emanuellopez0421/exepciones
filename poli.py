import math

# Clase base
class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcularArea(self):
        return None

# Clase derivada: Circulo
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def calcularArea(self):
        return math.pi * (self.radio ** 2)

# Clase derivada: Rectangulo
class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho, alto):
        super().__init__("Rectángulo")
        self.ancho = ancho
        self.alto = alto

    def calcularArea(self):
        return self.ancho * self.alto

# Clase derivada: Triangulo
class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Triángulo")
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return 0.5 * self.base * self.altura

# Función principal
def main():
    # Lista de figuras
    figuras = [
        Circulo(10),
        Rectangulo(9, 8),
        Triangulo(6, 14)
    ]
    
    # Imprimir encabezados
    print(f"| {'Figura':<10} | {'Área':<10} |")
    print(f"|{'-'*12}|{'-'*12}|")
    
    # Imprimir los datos de las figuras usando polimorfismo
    for figura in figuras:
        print(f"| {figura.nombre:<10} | {figura.calcularArea():<10.2f} |")

if __name__ == "__main__":
    main()

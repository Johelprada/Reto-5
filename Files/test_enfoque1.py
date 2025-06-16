print("PROBANDO ENFOQUE 1:")
from enfoque1.shape_package import Point, Square, Rectangle, Scalene

# Cuadrado de lado 2
p1 = Point(0, 0)
p2 = Point(0, 2)
p3 = Point(2, 2)
p4 = Point(2, 0)
cuadrado = Square([p1, p2, p3, p4])

print("CUADRADO:")
cuadrado.compute_perimeter()
cuadrado.compute_area()
print(f"¿Es regular? {'Sí' if cuadrado.get_is_regular() else 'No'}")

print("\n" + "="*50 + "\n")

# Triángulo escaleno
p1 = Point(0, 0)
p2 = Point(4, 0)
p3 = Point(2, 3)
triangulo = Scalene([p1, p2, p3])

print("TRIÁNGULO ESCALENO:")
triangulo.compute_perimeter()
triangulo.compute_area()
print(f"¿Es regular? {'Sí' if triangulo.get_is_regular() else 'No'}")
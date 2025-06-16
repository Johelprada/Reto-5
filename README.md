# Reto_5

Ejercicio de creacion de paquetes con la clase shape.

La estructura del paquete se vera de la siguiente forma:

```
mi_proyecto/
├── enfoque1/
│   └── shape_package/
│       ├── __init__.py
│       └── figuras.py
├── enfoque2/
│   └── shape_package/
│       ├── __init__.py
│       ├── point.py
│       ├── line.py
│       ├── shape.py
│       ├── rectangle.py
│       ├── triangle.py
│       └── square.py
├── test_enfoque1.py
└── test_enfoque2.py
```

El paquete principal mi_proyecto se subdivide en dos enfoques, mismos los cuales cumplen con la parte 1 y 2 de la actividad por separado.

Un ejemplo del codigo que se ejecuto para probar el enfoque 1 fue:
```python
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
```
El output esperado es el siguiente:

```python
líneas que forman la figura:
  Lado 1 de longitud 2.00
  Lado 2 de longitud 2.00
  Lado 3 de longitud 2.00
  Lado 4 de longitud 2.00
CUADRADO:
  Perímetro total: 8.00
  Área = 2.00 x 2.00 = 4.00
¿Es regular? Sí

líneas que forman la figura:
  Lado 1 de longitud 4.00
  Lado 2 de longitud 3.61
  Lado 3 de longitud 3.61
TRIÁNGULO ESCALENO:
  Perímetro total: 11.21
  Lados: 4.00, 3.61, 3.61
  Semiperímetro: 5.61
  Área: 6.00
```
De forma parecida sucede con la segunda parte y el test2

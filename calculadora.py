"""
Calculadora interactiva de números complejos.
Usa la librería complejos_lib.py
"""
"""
Calculadora interactiva de números complejos.
Usa la librería complejos_lib.py
"""

import math
import complejos as cl

def leer_complejo(mensaje="Ingrese número complejo"):
    """Lee un número complejo desde la entrada del usuario."""
    print(f"\n{mensaje}:")
    try:
        a = float(input("  Parte real: "))
        b = float(input("  Parte imaginaria: "))
        return (a, b)
    except ValueError:
        print("Error: Ingrese números válidos")
        return leer_complejo(mensaje)

def leer_polar():
    """Lee un número complejo en forma polar."""
    print("\nIngrese número en forma polar:")
    try:
        r = float(input("  Magnitud (módulo): "))
        theta = float(input("  Ángulo (radianes): "))
        return (r, theta)
    except ValueError:
        print("Error: Ingrese números válidos")
        return leer_polar()

def mostrar_resultado(resultado, titulo="Resultado"):
    """Muestra el resultado de forma formateada."""
    print(f"\n{titulo}:")
    if isinstance(resultado, tuple):
        if len(resultado) == 2:
            # Es un número complejo
            print(f"  Forma cartesiana: {cl.formato_cartesiano(resultado)}")
            polar = cl.a_polar(resultado)
            print(f"  Forma polar: {cl.formato_polar(polar)}")
        else:
            print(f"  {resultado}")
    else:
        # Es un número real (módulo o fase)
        print(f"  {resultado}")

def main():
    """Función principal del programa interactivo."""
    print("=" * 50)
    print("CALCULADORA DE NÚMEROS COMPLEJOS")
    print("=" * 50)
    
    while True:
        print("\n" + "=" * 50)
        print("MENÚ PRINCIPAL")
        print("=" * 50)
        print("1. Suma de dos números complejos")
        print("2. Resta de dos números complejos")
        print("3. Producto de dos números complejos")
        print("4. División de dos números complejos")
        print("5. Módulo de un número complejo")
        print("6. Conjugado de un número complejo")
        print("7. Convertir de cartesiano a polar")
        print("8. Convertir de polar a cartesiano")
        print("9. Fase de un número complejo")
        print("10. Potencia de un número complejo")
        print("0. Salir")
        
        try:
            opcion = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("Error: Ingrese un número válido")
            continue
        
        if opcion == 0:
            print("\n¡Gracias por usar la calculadora!")
            break
        
        try:
            if opcion in [1, 2, 3, 4]:
                # Operaciones binarias
                z1 = leer_complejo("Primer número")
                z2 = leer_complejo("Segundo número")
                
                if opcion == 1:
                    resultado = cl.suma(z1, z2)
                    mostrar_resultado(resultado, "Suma")
                elif opcion == 2:
                    resultado = cl.resta(z1, z2)
                    mostrar_resultado(resultado, "Resta")
                elif opcion == 3:
                    resultado = cl.producto(z1, z2)
                    mostrar_resultado(resultado, "Producto")
                elif opcion == 4:
                    try:
                        resultado = cl.division(z1, z2)
                        mostrar_resultado(resultado, "División")
                    except ValueError as e:
                        print(f"\nError: {e}")
            
            elif opcion in [5, 6, 7, 9]:
                # Operaciones unarias
                z = leer_complejo("Número complejo")
                
                if opcion == 5:
                    resultado = cl.modulo(z)
                    mostrar_resultado(resultado, "Módulo")
                elif opcion == 6:
                    resultado = cl.conjugado(z)
                    mostrar_resultado(resultado, "Conjugado")
                elif opcion == 7:
                    resultado = cl.a_polar(z)
                    mostrar_resultado(resultado, "Forma polar")
                    print(f"  Ángulo en grados: {math.degrees(resultado[1]):.2f}°")
                elif opcion == 9:
                    resultado = cl.fase(z)
                    mostrar_resultado(resultado, "Fase")
                    print(f"  Fase en grados: {math.degrees(resultado):.2f}°")
            
            elif opcion == 8:
                # Conversión polar a cartesiano
                polar = leer_polar()
                resultado = cl.a_cartesiano(polar)
                mostrar_resultado(resultado, "Forma cartesiana")
            
            elif opcion == 10:
                # Potencia
                z = leer_complejo("Base")
                try:
                    n = float(input("Exponente: "))
                    resultado = cl.potencia(z, n)
                    mostrar_resultado(resultado, f"Potencia ({cl.formato_cartesiano(z)})^{n}")
                except ValueError:
                    print("Error: Exponente debe ser un número")
            
            else:
                print("\nOpción no válida. Intente de nuevo.")
        
        except Exception as e:
            print(f"\nError inesperado: {e}")

if __name__ == "__main__":
    main()
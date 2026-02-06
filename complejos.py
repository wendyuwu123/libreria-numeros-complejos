"""
Librería para operaciones con números complejos.
Autor: [Tu nombre]
Fecha: [Fecha]
"""

import math

# Operaciones básicas
def suma(z1, z2):
    """Suma de dos números complejos en forma cartesiana.
    
    Args:
        z1: Tupla (real, imaginario) del primer número
        z2: Tupla (real, imaginario) del segundo número
        
    Returns:
        Tupla (real, imaginario) con el resultado
    """
    return (z1[0] + z2[0], z1[1] + z2[1])

def resta(z1, z2):
    """Resta de dos números complejos en forma cartesiana.
    
    Args:
        z1: Tupla (real, imaginario) del minuendo
        z2: Tupla (real, imaginario) del sustraendo
        
    Returns:
        Tupla (real, imaginario) con el resultado
    """
    return (z1[0] - z2[0], z1[1] - z2[1])

def producto(z1, z2):
    """Producto de dos números complejos en forma cartesiana.
    
    Args:
        z1: Tupla (real, imaginario) del primer número
        z2: Tupla (real, imaginario) del segundo número
        
    Returns:
        Tupla (real, imaginario) con el resultado
    """
    a, b = z1
    c, d = z2
    return (a * c - b * d, a * d + b * c)

def division(z1, z2):
    """División de dos números complejos en forma cartesiana.
    
    Args:
        z1: Tupla (real, imaginario) del numerador
        z2: Tupla (real, imaginario) del denominador
        
    Returns:
        Tupla (real, imaginario) con el resultado
        
    Raises:
        ValueError: Si se intenta dividir por cero
    """
    a, b = z1
    c, d = z2
    denom = c**2 + d**2
    if denom == 0:
        raise ValueError("No se puede dividir entre cero")
    return ((a * c + b * d) / denom, (b * c - a * d) / denom)

def modulo(z):
    """Módulo (magnitud) de un número complejo.
    
    Args:
        z: Tupla (real, imaginario)
        
    Returns:
        Módulo (float) del número complejo
    """
    a, b = z
    return math.sqrt(a**2 + b**2)

def conjugado(z):
    """Conjugado de un número complejo.
    
    Args:
        z: Tupla (real, imaginario)
        
    Returns:
        Tupla (real, -imaginario) con el conjugado
    """
    a, b = z
    return (a, -b)

def a_polar(z):
    """Convierte de representación cartesiana a polar.
    
    Args:
        z: Tupla (real, imaginario)
        
    Returns:
        Tupla (magnitud, fase) donde fase está en radianes
    """
    a, b = z
    r = math.sqrt(a**2 + b**2)
    theta = math.atan2(b, a)
    return (r, theta)

def a_cartesiano(p):
    """Convierte de representación polar a cartesiana.
    
    Args:
        p: Tupla (magnitud, fase) con fase en radianes
        
    Returns:
        Tupla (real, imaginario)
    """
    r, theta = p
    a = r * math.cos(theta)
    b = r * math.sin(theta)
    return (a, b)

def fase(z):
    """Fase (ángulo) de un número complejo en radianes.
    
    Args:
        z: Tupla (real, imaginario)
        
    Returns:
        Fase en radianes (float)
    """
    a, b = z
    return math.atan2(b, a)

# Operaciones adicionales
def potencia(z, n):
    """Potencia de un número complejo usando forma polar.
    
    Args:
        z: Tupla (real, imaginario)
        n: Exponente (int o float)
        
    Returns:
        Tupla (real, imaginario) con z^n
    """
    r, theta = a_polar(z)
    r_n = r ** n
    theta_n = theta * n
    return a_cartesiano((r_n, theta_n))

def formato_cartesiano(z, precision=3):
    """Formatea un número complejo como string.
    
    Args:
        z: Tupla (real, imaginario)
        precision: Número de decimales a mostrar
        
    Returns:
        String con formato "a + bi"
    """
    a, b = z
    signo = '+' if b >= 0 else '-'
    return f"{a:.{precision}f} {signo} {abs(b):.{precision}f}i"

def formato_polar(p, precision=3):
    """Formatea un número complejo polar como string.
    
    Args:
        p: Tupla (magnitud, fase)
        precision: Número de decimales a mostrar
        
    Returns:
        String con formato "r ∠ θ rad"
    """
    r, theta = p
    return f"{r:.{precision}f} ∠ {theta:.{precision}f} rad"
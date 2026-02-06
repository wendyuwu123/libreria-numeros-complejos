"""
Pruebas unitarias para la librería de números complejos.
Autor: [Tu nombre]
Fecha: [Fecha]
"""
"""
Pruebas unitarias para la librería de números complejos.
Autor: [Tu nombre]
Fecha: [Fecha]
"""

import unittest
import math

# Importamos las funciones directamente
from complejos import (
    suma, resta, producto, division,
    modulo, conjugado, a_polar, a_cartesiano,
    fase, potencia, formato_cartesiano, formato_polar
)

class TestComplejos(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para las pruebas."""
        # Números de prueba
        self.z1 = (3, 4)     # 3 + 4i
        self.z2 = (1, -2)    # 1 - 2i
        self.z3 = (0, 5)     # 5i
        self.z4 = (-2, 0)    # -2
        self.z5 = (0, 0)     # 0
        self.z6 = (1, 1)     # 1 + i
    
    # ---------- PRUEBAS PARA SUMA ----------
    def test_suma_basica(self):
        """Prueba suma de dos números complejos."""
        resultado = suma(self.z1, self.z2)
        self.assertEqual(resultado, (4, 2))
    
    def test_suma_con_cero(self):
        """Prueba suma con el elemento neutro (0, 0)."""
        resultado = suma(self.z1, self.z5)
        self.assertEqual(resultado, self.z1)
    
    # ---------- PRUEBAS PARA RESTA ----------
    def test_resta_basica(self):
        """Prueba resta de dos números complejos."""
        resultado = resta(self.z1, self.z2)
        self.assertEqual(resultado, (2, 6))
    
    def test_resta_mismo_numero(self):
        """Prueba que z - z = 0."""
        resultado = resta(self.z1, self.z1)
        self.assertEqual(resultado, (0, 0))
    
    # ---------- PRUEBAS PARA PRODUCTO ----------
    def test_producto_basico(self):
        """Prueba producto de dos números complejos."""
        resultado = producto(self.z1, self.z2)
        # 3*1 - 4*(-2) = 3 + 8 = 11
        # 3*(-2) + 4*1 = -6 + 4 = -2
        self.assertEqual(resultado, (11, -2))
    
    def test_producto_por_cero(self):
        """Prueba producto por el elemento cero."""
        resultado = producto(self.z1, self.z5)
        self.assertEqual(resultado, (0, 0))
    
    # ---------- PRUEBAS PARA DIVISIÓN ----------
    def test_division_basica(self):
        """Prueba división de dos números complejos."""
        resultado = division(self.z1, self.z2)
        # Resultado esperado: (-1.0, 2.0)
        self.assertAlmostEqual(resultado[0], -1.0, places=5)
        self.assertAlmostEqual(resultado[1], 2.0, places=5)
    
    def test_division_por_cero(self):
        """Prueba que división por cero lanza ValueError."""
        with self.assertRaises(ValueError):
            division(self.z1, self.z5)
    
    # ---------- PRUEBAS PARA MÓDULO ----------
    def test_modulo_3_4i(self):
        """Prueba módulo de 3 + 4i (debe ser 5)."""
        resultado = modulo(self.z1)
        self.assertAlmostEqual(resultado, 5.0, places=5)
    
    def test_modulo_cero(self):
        """Prueba módulo de 0 + 0i."""
        resultado = modulo(self.z5)
        self.assertEqual(resultado, 0.0)
    
    # ---------- PRUEBAS PARA CONJUGADO ----------
    def test_conjugado_basico(self):
        """Prueba conjugado de un número complejo."""
        resultado = conjugado(self.z1)
        self.assertEqual(resultado, (3, -4))
    
    def test_conjugado_real_puro(self):
        """Prueba conjugado de un número real puro."""
        resultado = conjugado(self.z4)
        self.assertEqual(resultado, (-2, 0))
    
    # ---------- PRUEBAS PARA CONVERSIÓN A POLAR ----------
    def test_a_polar_1_1(self):
        """Prueba conversión a polar de 1 + i."""
        r, theta = a_polar(self.z6)
        self.assertAlmostEqual(r, math.sqrt(2), places=5)
        self.assertAlmostEqual(theta, math.pi/4, places=5)
    
    def test_a_polar_real_negativo(self):
        """Prueba conversión a polar de -2."""
        r, theta = a_polar(self.z4)
        self.assertAlmostEqual(r, 2.0, places=5)
        self.assertAlmostEqual(theta, math.pi, places=5)
    
    # ---------- PRUEBAS PARA CONVERSIÓN A CARTESIANO ----------
    def test_a_cartesiano_basico(self):
        """Prueba conversión a cartesiano desde polar."""
        polar = (5.0, math.atan2(4, 3))
        resultado = a_cartesiano(polar)
        self.assertAlmostEqual(resultado[0], 3.0, places=5)
        self.assertAlmostEqual(resultado[1], 4.0, places=5)
    
    def test_a_cartesiano_angulo_cero(self):
        """Prueba conversión de polar con ángulo cero."""
        resultado = a_cartesiano((2.0, 0))
        self.assertAlmostEqual(resultado[0], 2.0, places=5)
        self.assertAlmostEqual(resultado[1], 0.0, places=5)
    
    # ---------- PRUEBAS PARA FASE ----------
    def test_fase_cuarto_cuadrante(self):
        """Prueba fase de un número en el cuarto cuadrante."""
        resultado = fase((1, -1))
        self.assertAlmostEqual(resultado, -math.pi/4, places=5)
    
    def test_fase_eje_imaginario_positivo(self):
        """Prueba fase de un número en el eje imaginario positivo."""
        resultado = fase(self.z3)
        self.assertAlmostEqual(resultado, math.pi/2, places=5)
    
    # ---------- PRUEBAS ADICIONALES ----------
    def test_potencia(self):
        """Prueba de potencia de un número complejo."""
        resultado = potencia(self.z6, 2)  # (1+i)^2 = 2i
        self.assertAlmostEqual(resultado[0], 0.0, places=5)
        self.assertAlmostEqual(resultado[1], 2.0, places=5)
    
    def test_formato_cartesiano(self):
        """Prueba de formato de número complejo."""
        resultado = formato_cartesiano(self.z1, precision=2)
        self.assertEqual(resultado, "3.00 + 4.00i")
    
    def test_formato_polar(self):
        """Prueba de formato de número polar."""
        polar = a_polar(self.z6)
        resultado = formato_polar(polar, precision=2)
        self.assertIn("1.41 ∠ 0.79 rad", resultado)
    
    def test_propiedad_conversiones(self):
        """Prueba que ida y vuelta de conversiones da el mismo número."""
        cartesiano = (2.5, -1.3)
        polar = a_polar(cartesiano)
        vuelta = a_cartesiano(polar)
        self.assertAlmostEqual(cartesiano[0], vuelta[0], places=5)
        self.assertAlmostEqual(cartesiano[1], vuelta[1], places=5)

if __name__ == '__main__':
    unittest.main(verbosity=2)
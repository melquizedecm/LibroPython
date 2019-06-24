# coding=utf-8
#########################################################################################
#########################################################################################
# Program Name: mainFigura.py
# Date: jun-13, 2019
# Authors: Melquizedec Moo Medina, Rodrigo Mazun Cruz
# Description: Clase principal que objetos de las Clases Triangulo y Rectangulo.
#
#########################################################################################
#########################################################################################

from Triangulo import *
from Rectangulo import *

#Se dibuja un Triangulo
figura1 = Triangulo(200, 100, 200, 200)
figura1.calcularArea()
figura1.dibujar()
print("Area de Triangulo:" + str(figura1))


#Se dinuja un rectangulo
figura2 = Rectangulo(200, 100, 200,200)
figura2.calcularArea()
figura2.dibujar()
print("Area de Rectangulo" + str(figura2))
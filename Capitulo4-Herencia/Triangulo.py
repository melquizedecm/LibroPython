# coding=utf-8
#########################################################################################
#########################################################################################
# Program Name: Triangulo.py
# Date: jun-13, 2019
# Authors: Melquizedec Moo Medina, Rodrigo Mazun Cruz
# Description: Clase Derivada de la clase Figura que configura los valores o atributos
# de una Figura Geometrica de tipo Triangular y permite dibujar y calcular el area
#########################################################################################
#########################################################################################

from Figura import *

class Triangulo(Figura):
    def __init__(self, base, altura, x, y):
        Figura.__init__(self, base, altura, x, y)

    #Se usa el metodo create_polygon(), donde se le pasan los valores de los tres puntos
    #del triangulo. Las formulas se describen en este apartado del libro.
    def dibujar(self):
        self.root.title('Triangulo Rectangulo')
        x1=self.posX
        y1=self.posY
        x2=x1+self.base
        y2=y1
        x3=x2
        y3 = y2 - self.altura
        self.ventana.create_polygon([x1,y1,x2,y2,x3,y3],outline='black', fill='yellow', width='5')
        self.root.mainloop()

    #area = base * altura  /2
    def calcularArea(self):
        self.area = float(self.base) * float(self.altura) / 2

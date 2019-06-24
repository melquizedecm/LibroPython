# coding=utf-8
#########################################################################################
#########################################################################################
# Program Name: Rectangulo.py
# Date: jun-13, 2019
# Authors: Melquizedec Moo Medina, Rodrigo Mazun Cruz
# Description: Clase Derivada de la clase Figura que configura los valores o atributos
# de una Figura Geometrica de tipo Rectangular y permite dibujar y calcular el area
#########################################################################################
#########################################################################################

from Figura import *

class Rectangulo(Figura):
    def __init__(self, base, altura, x, y):
        Figura.__init__(self, base, altura, x, y)

    def dibujar(self):
        self.root.title('Rectangulo')
        self.ventana.create_rectangle(self.posX, self.posY, self.base+self.posX, self.posY+self.altura, outline='black', fill='yellow', width='5')
        self.root.mainloop()


    def calcularArea(self):
        self.area = float(self.base) * float(self.altura)

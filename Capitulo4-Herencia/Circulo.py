# coding=utf-8
#########################################################################################
#########################################################################################
# Program Name: Circulo.py
# Date: jun-14, 2019
# Authors: Melquizedec Moo Medina, Rodrigo Mazun Cruz
# Description: Clase Derivada de la clase Figura que configura los valores o atributos
# de una Figura Geometrica de tipo Circular y permite dibujar y calcular el area
#########################################################################################
#########################################################################################

from Figura import *
import math

class Circulo(Figura):
    def __init__(self, x, y,radio):
        self.radio=radio
        base= radio*2
        altura=radio*2
        Figura.__init__(self, base, altura, x, y)

    #Se usa el metodo create_oval(), donde se le pasan los valores de posición
    #del círculo. Las fórmulas se describen en este apartado del libro.
    def dibujar(self):
        self.root.title('Círculo')
        x1=self.posX
        y1=self.posY
        x2=self.base + self.posX
        y2=self.altura + self.posY
        #x3=x2
        #y3 = y2 - self.altura
        #self.ventana.create_oval( x1, y1, x2, y2, x3, y3, outline='black', fill='yellow' )
        self.ventana.create_oval(x1,y1,x2,y2,width=2, fill='blue')
        self.root.mainloop()

    # se calcula el área del círculo
    def calcularArea(self):
        self.area =  float(math.pi) * float(self.radio)** 2
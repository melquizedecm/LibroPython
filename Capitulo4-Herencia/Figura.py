# coding=utf-8
#########################################################################################
#########################################################################################
# Program Name: Figura.py
# Date: jun-13, 2019
# Authors: Melquizedec Moo Medina, Rodrigo Mazun Cruz
# Description: Clase Base que configura los valores o atributos de una Figura Geometrica
# Note:Se requiere instalar la libreria Tkinter
#########################################################################################
#########################################################################################
from tkinter import *
class Figura(object):
    def __init__(self, base, altura, x, y):
        self.base = base
        self.altura = altura
        self.posX = x
        self.posY = y
        self.area = 0
        self.root = Tk()
        self.ventana = Canvas(width=800, height=600, bg='white')
        self.ventana.pack(expand=YES, fill=BOTH)
    # Métodos para cambiar la Base y la altura
    def setBase(self, nuevaBase):
        self.base = nuevaBase
    def setAltura(self, nuevaAltura):
        self.altura = nuevaAltura
    # Metodo especial que devolverá al llamar un String del objeto
    def __str__(self):
        return str(self.area)


# coding=utf-8
#########################################################################################
#########################################################################################
# Program Name: Division.py
# Date: jun-14, 2019
# Authors: Melquizedec Moo Medina
# Description: Clase Validacion que construye un método para realizar la division de dos
# numeros sin procesar una validacion entre ellos. retorna la parte entera de la division.
#########################################################################################
#########################################################################################

# inicio de la Clase Validacion

class Validacion:
    resultado = 0.0  # atributo resultado, guarda el valor de la operacion.

    # metodo que permite realizar la division de dos numeros y devuelve la parte entera.
    def dividir(self, a, b):
        self.resultado = a / b
        return self.resultado

# fin de la Clase Validacion

#Se define la funcion principal
def main():
    validar = Validacion()
    a = input("escribe un numero a dividir: ")
    b = input("Escribe el numero divisor: ")
    print(validar.dividir(a, b))

#Se llama a la funcion principal
if __name__ == "__main__":
    main()

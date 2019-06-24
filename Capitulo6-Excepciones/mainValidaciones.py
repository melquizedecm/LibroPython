from ValidacionesClass import *

validar =ValidacionesClass()
while True:
    print("MENU")
    print("1. Validar un Entero")
    print("2. Validar un Flotante")
    print("3. Validar un Entero dentro de un rango")
    print("4. Validar letras")
    print("5. Validar largo de cadena")
    print("6. Salir")
    opcion = raw_input("Selecciona una opcion:  ")

    if opcion=="1":
        dato=raw_input("Escribe el entero")
        if(validar.validarEntero(dato)):
            print("Es un entero")
        else:
            print("No es entero")


    elif opcion=="2":
        pass


    elif opcion=="3":
        minimo=raw_input("Escribe el valor minimo del rango")
        maximo=raw_input("Escribe el valor maximo")
        dato=raw_input("Escribe el valor dentro del rango")
        if validar.validarRangoEntero(minimo,maximo,dato):
            print("El valor si esta en el rango")
        else:
            print("El valor o el rango es incorrecto")

    elif opcion=="4":
        pass
    elif opcion=="5":
        pass
    elif opcion=="6":
        break
    else:
        print("Error en la seleccion")



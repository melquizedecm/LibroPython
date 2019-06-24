class ValidacionesClass:

    def validarEntero(self,dato):
        try:
            if int(dato) or dato =="0":
                return True
        except ValueError:
            return  False

    def validarFlotante(self,dato):
        pass

    def validarRangoEntero(self,minimo,maximo,dato):
        try:
            if(int(dato)>=int(minimo) and int(dato)<=int(maximo)):
                return True
            else:
                return False
        except ValueError:
            return False

    def validarLetras(self,dato):
        pass
    def validarCadenaNumeros(self,tamanio):
        pass
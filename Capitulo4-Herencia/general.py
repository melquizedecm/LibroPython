class   General:
    #r = 0
    s = 0
    def __init__(self,valor_A,valor_B,valor_C): #constructor
        self.valor_A=valor_A
        self.valor_B=valor_B
        self.valor_C=valor_C

    def raiz(self):
           self.s = self.valor_A + self.valor_B + self.valor_C
           return self.s

x=General(1,2,3)
w=x.raiz()
print("Suma es ", w)
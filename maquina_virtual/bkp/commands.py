
class MV(self):
    def __init__(self, lista_instrucao, lista_endereco, lista_atributo_1, lista_atributo_2, lista_valor):
        self.P =  lista_instrucao
        self.M = lista_valor
        self.s = -1
        self.i = 0

    def ldc(self, k):
        s = self.s
        self.s = s + 1
        self.M[s] = k

    def ldv(self, n):
        self.s = s + 1
        self.M[s] = self.M[n]

    def add(self):
        s = self.s
        self.M[s-1] = self.M[s-1] + self.M[s]
        self.s = s-1

    def sub(self):    
        s = self.s
        self.M[s-1] = self.M[s-1] - self.M[s]
        self.s = s-1

    def mult(self):
        s = self.s
        self.M[s-1] = self.M[s-1] * self.M[s]
        self.s = s-1

    def div(self):    
        s = self.s
        self.M[s-1] = self.M[s-1] / self.M[s]
        self.s = s-1

    def inv(self):
        s = self.s
        self.M[s] = - self.M[s]
    
    def and(self):
        s = self.s
        if self.M[s-1] == 1 and self.M[s] == 1:
            self.M[s-1] = 1
        else:    
            self.M[s-1] = 0
        self.s = s-1    

    def or(self):
        s = self.s
        if self.M[s-1] == 1 or self.M[s] == 1:
            self.M[s-1] = 1
        else:    
            self.M[s-1] = 0
        self.s = s-1    
    
    def neg(self):
        s = self.s
        self.M[s] = 1 - self.M[s]

    def cme(self):
        s = self.s
        if self.M[s-1] < self.M[s]:
            self.M[s-1] = 1
        else:    
            self.M[s-1] = 0
        self.s = s-1    

    def cma(self):
        s = self.s
        if self.M[s-1] > self.M[s]:
            self.M[s-1] = 1
        else:    
            self.M[s-1] = 0
        self.s = s-1    

    def ceq(self):
        s = self.s
        if self.M[s-1] == self.M[s]:
            self.M[s-1] = 1
        else:    
            self.M[s-1] = 0
        self.s = s-1    

    def cdif(self):
        s = self.s
        if self.M[s-1] != self.M[s]:
            self.M[s-1] = 1
        else:    
            self.M[s-1] = 0
        self.s = s-1    

    def cmeq(self):
        s = self.s
        if self.M[s-1] <= self.M[s]:
            self.M[s-1] = 1
        else:    
            self.M[s-1] = 0
        self.s = s-1    

    def cmaq(self):
        s = self.s
        if self.M[s-1] >= self.M[s]:
            self.M[s-1] = 1
        else:    
            self.M[s-1] = 0
        self.s = s-1    

    def start(self):
        self.s = -1

    def hlt(self):
        return False

    #atribuição
    def str(self, n):
        s = self.s
        self.M[n] = self.M[s]
        self.s = -1

    #desvios
    def jmp(self, t):
        self.i = t

    def jmpf(self, t):
        s = self.s
        if self.M[s] == 0:
            self.i = t
        else:
            self.i = self.i + 1
        self.s = s - 1    
    
    #operação nula
    def null(self):
        return None

    #entrada
    def rd(self, entrada):
        self.s = self.s + 1
        self.M[self.s] = entrada
    
    #saída
    def prn(self):
        saida = self.M[self.s]
        self.s = self.s -1
        return saida

    #alocação
    def alloc(self, m ,n):
        for k in range(n-1):
            self.s = self.s + 1
            self.M[self.s] = self.M[m+k]

    def dalloc(self, m ,n):
        for k in range(n-1, 0, -1):
            self.M[m+k] = self.M[self.s]
            self.s = self.s - 1
    
    #chamda de rotina
    def call(self, t):
        self.s = self.s + 1
        self.M[self.s] = self.i + 1
        self.i = t

    def return(self):
        self.i = self.M[self.s]
        self.s = self.s - 1



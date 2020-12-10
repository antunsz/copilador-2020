
class MV:
    def __init__(self):
        self.P = []
        self.M = [None for i in range(15)]
        self.s = -1
        self.i = 0

    def ldc(self, k):
        self.s = self.s + 1
        try:
            self.M[self.s] = k
        except:
            self.M.append('')
            self.M[self.s] = k

    def ldv(self, n):
        self.s = self.s + 1
        try:
            self.M[self.s] = self.M[int(n)]
        except:
            self.M.append('')
            self.M[self.s] = self.M[int(n)]
            
    def add(self):
        self.M[self.s-1] = self.M[self.s-1] + self.M[self.s]
        self.s = self.s-1

    def sub(self):    
        self.M[self.s-1] = float(self.M[self.s-1]) - float(self.M[self.s])
        self.s = self.s-1

    def mult(self):
        self.M[self.s-1] = self.M[self.s-1] * self.M[self.s]
        self.s = self.s-1

    def divi(self):
        self.M[self.s-1] = self.M[self.s-1] / self.M[self.s]
        self.s = self.s-1

    def inv(self):
        self.M[self.s] = - self.M[self.s]
    
    def funcao_and(self):
        if self.M[self.s-1] == 1 and self.M[self.s] == 1:
            self.M[self.s-1] = 1
        else:    
            self.M[self.s-1] = 0
        self.s = self.s-1    

    def funcao_or(self):
        if self.M[self.s-1] == 1 or self.M[self.s] == 1:
            self.M[self.s-1] = 1
        else:    
            self.M[self.s-1] = 0
        self.s = self.s-1    
    
    def neg(self):
        self.M[self.s] = 1 - self.M[self.s]

    def cme(self):
        if self.M[self.s-1] < self.M[self.s]:
            self.M[self.s-1] = 1
        else:    
            self.M[self.s-1] = 0
        self.s = self.s-1    

    def cma(self):
        if self.M[self.s-1] > self.M[self.s]:
            self.M[self.s-1] = 1
        else:    
            self.M[self.s-1] = 0
        self.s = self.s-1    

    def ceq(self):
        if self.M[self.s-1] == self.M[self.s]:
            self.M[self.s-1] = 1
        else:    
            self.M[self.s-1] = 0
        self.s = self.s-1    

    def cdif(self):
        if self.M[self.s-1] != self.M[self.s]:
            self.M[self.s-1] = 1
        else:    
            self.M[self.s-1] = 0
        self.s = self.s-1    

    def cmeq(self):
        if self.M[self.s-1] <= self.M[self.s]:
            self.M[self.s-1] = 1
        else:    
            self.M[self.s-1] = 0
        self.s = self.s-1    

    def cmaq(self):
        if self.M[self.s-1] >= self.M[self.s]:
            self.M[self.s-1] = 1
        else:    
            self.M[self.s-1] = 0
        self.s = self.s-1    

    def start(self):
        self.s = -1

    def hlt(self):
        return False

    #atribuição
    def str(self, n):
        self.M[int(n)] = self.M[self.s]
        self.s = self.s - 1

    #desvios
    def jmp(self, t):
        self.i = t

    def jmpf(self, t):
        if self.M[self.s] == 0:
            self.i = t
        else:
            self.i = self.i + 1
        self.s = self.s - 1    
    
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
        for k in range(int(n)): #por especificação do python, não tem necessidade de fazer -1
            self.s = self.s + 1
            self.M.append(0) #criando posição na lista antes de "alocar"
            self.M[self.s] = self.M[int(m)+k]

    #TODO
    def dalloc(self, m ,n):
        for k in range(int(n)-1, -1, -1):#n-1 e 0-1 para que o for execute corretamente
            self.M[int(m)+k] = self.M[self.s]
            self.s = self.s - 1
    
    #chamda de rotina
    def call(self, t):
        self.s = self.s + 1
        self.M[self.s] = self.i + 1
        self.i = t

    def funcao_return(self):
        self.i = self.M[self.s]
        self.s = self.s - 1

    #MÉTODOS AUXILIARES
    def converte_p_int(self):
        self.M = [int(x) if type(x) == type('') else x for x in self.M]

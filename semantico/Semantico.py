from pythonds.basic.stack import Stack
import re
class Semantico:
    def __init__(self):
        self.rotulo = None
        self.nivel = 0
        self.ind = None
        self.aux_tipos = []
        self.pilha_operadores = []
        self.pilha_alloc = []
        self.i_pilha = 0
        self.qtd_var_local = 0
        self.qtd_var = 0
        self.tabela = []
        self.ERROS = {
                        'duplic_var':'Variável duplicada.',
                        'decl_var':'Variável não declarada.',
                        'decl_proc':'Procedimento não declarado ou duplicado.',
                        'funcao':'Deveria ter uma função aqui?',
                        'decl_func':'Função não declarado.',
                        'inc_tipo':'Tipos incompatíveis',
                        'inc_ident':'Identificador incompatível ou não declarado',
                        'fator_desconhecido':'Não foi possível encontrar o fator',
                        'fecha_parenteses':'Não foi possível encontrar o }',

        }
        self.assemble = []
    
    def coloca_tipo(self, tipo):    
        for token in self.tabela:
            if token['tipo_lexema'] == 'variavel':
                if token['tipo_especifico'] == None:
                    token['tipo_especifico'] = tipo


    def retorna_tipo_especifico(self, lexema):
        if lexema.isdigit():
            return 'inteiro'
        for token in self.tabela:
            if token['token'] == lexema:
                return token['tipo_especifico']
    
    def empilha_operador(self, operador):
        if not self.pilha_operadores:
            self.pilha_operadores.insert(0, operador)
        else:
            if operador['tipo'] == "parenteses":
                self.pilha_operadores.insert(0, operador)
            else:
                while True:
                    if not self.pilha_operadores:
                        self.pilha_operadores.insert(0, operador)
                        break
                    if self.pilha_operadores[-1]['prioridade'] > operador['prioridade']:
                        self.pilha_operadores.insert(0, operador)
                        break
                    else:
                        if self.pilha_operadores[-1]['tipo'] == 'unarios':
                            if self.pilha_operadores[-1]['lexema'] == "-":
                                self.gera(comando="INV")
                            if self.pilha_operadores[-1]['lexema'] == "nao":
                                self.gera(comando="NEG")
                            self.pilha_operadores.pop(0)    
                            break
                        elif self.pilha_operadores[-1]['tipo'] == 'multDiv':
                            if self.pilha_operadores[-1]['lexema'] == "*":
                                self.gera(comando="MULT")
                            else:
                                self.gera(comando="DIV")
                            self.pilha_operadores.pop(0)    
                            break
                        elif self.pilha_operadores[-1]['tipo'] == 'maisMenos':
                            if self.pilha_operadores[-1]['lexema'] == "+":
                                self.gera(comando="ADD")
                            else:
                                self.gera(comando="SUB")
                            self.pilha_operadores.pop(0)    
                            break
                        elif self.pilha_operadores[-1]['tipo'] == 'comparadores':
                            if self.pilha_operadores[-1]['lexema'] == "<":
                                self.gera(comando="CME")
                            elif self.pilha_operadores[-1]['lexema'] == ">":
                                self.gera(comando="CMA")
                            elif self.pilha_operadores[-1]['lexema'] == "=":
                                self.gera(comando="CEQ")
                            elif self.pilha_operadores[-1]['lexema'] == "<=":
                                self.gera(comando="CMEQ")
                            elif self.pilha_operadores[-1]['lexema'] == ">=":
                                self.gera(comando="CMAQ")
                            elif self.pilha_operadores[-1]['lexema'] == "!=":
                                self.gera(comando="CDIF")
                            self.pilha_operadores.pop(0)    
                            break
                        elif self.pilha_operadores[-1]['tipo'] == 'e':
                            self.gera(comando="AND")
                            self.pilha_operadores.pop(0)    
                            break
                        elif self.pilha_operadores[-1]['tipo'] == 'ou':
                            self.gera(comando="OR")
                            self.pilha_operadores.pop(0)    
                            break
                        elif self.pilha_operadores[-1]['tipo'] == 'parenteses':
                            self.pilha_operadores.pop(0)    
                            break
                        else:
                            break


    def desempilha_operador(self):
        if self.pilha_operadores:
            while True:
                if self.pilha_operadores[-1]['lexema'] == "(":
                    self.pilha_operadores.pop(0)    
                    break

                elif self.pilha_operadores[-1]['tipo'] == 'unarios':
                    if self.pilha_operadores[-1]['lexema'] == "-":
                        self.gera(comando="INV")
                    if self.pilha_operadores[-1]['lexema'] == "nao":
                        self.gera(comando="NEG")
                    self.pilha_operadores.pop(0)    
                    break
                elif self.pilha_operadores[-1]['tipo'] == 'multDiv':
                    if self.pilha_operadores[-1]['lexema'] == "*":
                        self.gera(comando="MULT")
                    else:
                        self.gera(comando="DIV")
                    self.pilha_operadores.pop(0)    
                    break
                elif self.pilha_operadores[-1]['tipo'] == 'maisMenos':
                    if self.pilha_operadores[-1]['lexema'] == "+":
                        self.gera(comando="ADD")
                    else:
                        self.gera(comando="SUB")
                    self.pilha_operadores.pop(0)    
                    break
                elif self.pilha_operadores[-1]['tipo'] == 'comparadores':
                    if self.pilha_operadores[-1]['lexema'] == "<":
                        self.gera(comando="CME")
                    elif self.pilha_operadores[-1]['lexema'] == ">":
                        self.gera(comando="CMA")
                    elif self.pilha_operadores[-1]['lexema'] == "=":
                        self.gera(comando="CEQ")
                    elif self.pilha_operadores[-1]['lexema'] == "<=":
                        self.gera(comando="CMEQ")
                    elif self.pilha_operadores[-1]['lexema'] == ">=":
                        self.gera(comando="CMAQ")
                    elif self.pilha_operadores[-1]['lexema'] == "!=":
                        self.gera(comando="CDIF")
                    self.pilha_operadores.pop(0)    
                    break
                elif self.pilha_operadores[-1]['tipo'] == 'e':
                    self.gera(comando="AND")
                    self.pilha_operadores.pop(0)    
                    break
                elif self.pilha_operadores[-1]['tipo'] == 'ou':
                    self.gera(comando="OR")
                    self.pilha_operadores.pop(0)    
                    break
                elif self.pilha_operadores[-1]['tipo'] == 'parenteses':
                    self.pilha_operadores.pop(0)    
                    break
                else:
                    break

    def verifica_compatibilidade_tipos(self, linha):
        print("TIPOS:", self.aux_tipos)
        for i, o in enumerate(self.aux_tipos):
            if o != self.aux_tipos[i-1]:
                raise Exception('Erro de semântica: '+self.ERROS['inc_tipo']+". Linha: "+str(linha+1))


    def mostra_erro(self, erro, token):
        print('Tabela:', self.tabela)
        print('Assemble:', self.assemble)
        raise Exception('Erro de semântica: '+self.ERROS[erro]+ ' Linha: '+str(token['linha']+1))

    def gera(self, rotulo=None, comando=None, attr1=None, attr2=None):
        self.assemble.insert(0, {"rotulo":rotulo, "comando":comando, "attr1":attr1, "attr2":attr2})
        
    def insere_tabela(self, token, lexema, tipo_lexema, tipo_especifico=None, nivel=None,posicao_mem=None, rotulo=None, i=None):
        self.tabela.insert(0, {'token':token, 'lexema':lexema, 'tipo_lexema':tipo_lexema, 'tipo_especifico':tipo_especifico, 'posicao_mem':posicao_mem, 'nivel':nivel, 'rotulo':rotulo, 'i':i})
    

    def pesquisa_duplic_var_tabela(self, lexema):
        nivel = self.tabela[-1]['nivel']
        for linha in self.tabela:
            if linha['lexema'] == lexema and nivel == linha['nivel']:
                return True
        return False

    def coloca_tipo_tabela(self, lexema):
        nivel = self.tabela[-1]['nivel']
        for linha in self.tabela:
            if linha['tipo_lexema'] == 'variavel' and nivel == linha['nivel']:
                linha['tipo_lexema'] = lexema

    def pesquisa_declvar_tabela(self, lexema):
        for linha in self.tabela:
            print(f"{linha['token']} - {lexema}")
            if linha['token'] == lexema['token']:
                return True
        return False

    def pesquisa_declvarfunc_tabela(self, lexema):
        pass

    def pesquisa_declproc_tabela(self, lexema):
        for linha in self.tabela:
            print(f"{linha['token']} - {lexema}")
            if linha['token'] == lexema['token']:
                self.mostra_erro('decl_proc', lexema)
                return True
        return False

    def pesquisa_declfunc_tabela(self, lexema, nivel):
        for linha in self.tabela:
            if linha['lexema'] == lexema and nivel == linha['nivel']:
                return True
        return False

    def desempilha(self):
        pass

    def volta_nivel(self):
        pass

    def pesquisa_tabela(self, lexema, nivel):
        while nivel>=0:
            for i, linha in enumerate(self.tabela):
                if linha['token'] == lexema and (linha['nivel'] == nivel or linha['nivel'] == None):
                    return True, linha['i'], i
            nivel -= 1    
        return False, None, None

    def get_nivel_rotulo_procedimento(self, proc_name):
        for i, linha in enumerate(self.tabela):
            if linha['token'] == proc_name and linha['tipo_lexema'] == 'procedimento':
                return True, linha['nivel'], linha['rotulo']
        return False, None, None

    def get_indice_var(self, var):
        nivel = self.nivel
        while nivel >=0:
            for linha in self.tabela:
                if linha['token'] == var:
                    return linha['i']
            nivel -= 1    
        return False

import sys
import os
sys.path.append(os.path.abspath('../lexico'))
sys.path.append(os.path.abspath('../semantico'))
import re
import pprint as pp
from tkinter.filedialog import askopenfilename
from sintatico_utils import *
from Lexico import Lexico
import traceback
from Semantico import Semantico


class Sintatico:
    def __init__(self,txt=None):
        # self.lexico = MockLexico()
        self.lexico = Lexico()
        print("#####INICIO LEXICO########")
        if not txt:
            self.lexico.le_arquivo()
        else:
            self.lexico.txt_arquivo = txt
        self.lexico.inicia_lexico()
        print("#####INICIO SINTATICO########")
        self.txt_arquivo = ""
        self.expressao_temp = ""
        self.pilha_expressao = []
        self.LISTA_OPERADORES = {}
        self.ERROS = {
            "is_identificador":"'!#!' não é um identificador.",
            "is_programa":"'!#!' não é um início de programa válido.",
            "is_ponto_virgula":"Deveria ser um ';' ao invés de '!#!'.",
            "is_ponto_final":"O pragrama deveria terminar com '.' ao invés de '!#!'.",
            "is_dois_pontos":"Deveria ser ':' ao invés de '!#!'.",
            "analisa_tipo":"'!#!' não é um tipo válido.",
            "is_procedimento":"'!#!' não é um procedimento.",
            "is_procedimento_ou_funcao":"'!#!' não é um procedimento ou uma função.",
            "is_funcao":"'!#!' deveria ser um início de função.",
            "is_fim":"'!#!' deveria ser um fim de função ou procedimento.",
            "is_inicio":"'!#!' Sintaxe inválida.",
            "is_se":"'!#!' deveria ser um se.",
            "is_entao":"'!#!' deveria ser um entao.",
            "is_var":"'!#!' deveria ser uma variável.",
            "is_tipo":"'!#!' deveria ser um tipo.",
        }
        print("#####INICIO SEMÂNTICO########")
        self.semantico = Semantico()

    def mostra_erro(self, nome_metodo, token):    
        raise Exception('Erro de sintáxe: '+self.ERROS[nome_metodo].replace('!#!', token['token'])+" Linha: "+str(token['linha']+1))

    def analisa_programa(self):

        self.semantico.rotulo = 1

        token = self.lexico.pop_token()
        if is_programa(token):
            token = self.lexico.pop_token()
            if is_identificador(token):
                self.semantico.insere_tabela(token["token"], token["lexema"], 'programa', posicao_mem=0)
                token = self.lexico.pop_token()
                if is_ponto_virgula(token, 'analisa_programa'):
                    self.semantico.gera(comando='START')
                    self.analisa_bloco()
                    dalloc = self.semantico.pilha_alloc.pop()
                    self.semantico.gera(comando='DALLOC', attr1=dalloc[0], attr2=dalloc[1])
                    token = self.lexico.pop_token()
                    if is_ponto_final(token):
                        self.semantico.gera(comando='HLT')
                        return True
                    else:            
                        self.mostra_erro('is_ponto_final', token)
                else:            
                    self.mostra_erro('is_ponto_virgula', token)
            else:            
                self.mostra_erro('is_identificador', token)
        else:            
            self.mostra_erro('is_programa', token)


    def analisa_bloco(self):
        print('--analisa_bloco')
        self.analisa_etapa_declaracao_vars() 
        self.analisa_etapa_declaracao_sub_rotinas() 
        self.analisa_comandos()

    def analisa_etapa_declaracao_vars(self):
        print("--analisa_etapa_declaracao_vars")
        token = self.lexico.pop_token()
        if is_var(token):
            while self.analisa_declaracao_vars():
                token = self.lexico.pop_token()
                if not is_ponto_virgula(token, 'analisa_etapa_decalracao_vars'):
                    self.mostra_erro('is_ponto_virgula', token)
                self.semantico.gera(comando='ALLOC', attr1=self.semantico.i_pilha, attr2=self.semantico.qtd_var_local)
                self.semantico.pilha_alloc.append((self.semantico.i_pilha, self.semantico.qtd_var_local))
                self.semantico.i_pilha = self.semantico.qtd_var_local
                self.semantico.qtd_var_local = 0
                token = self.lexico.pop_token()
                #TODO:rever
                if token["lexema"] == 'sprocedimento' or token["lexema"] == 'sfuncao' or token["lexema"] == 'sinicio':    
                    self.lexico.insert_token(token)
                    break
                self.lexico.insert_token(token)
            return True        
        # self.lexico.insert_token(token)
        else:
            self.mostra_erro('is_var', token)

    def analisa_variavel(self):
        print("--analisa_variavel")
        token = self.lexico.pop_token()
        if is_identificador(token):
            return True
        else:
            self.mostra_erro('is_identificador', token)

    def analisa_declaracao_vars(self):
        print("--analisa_declaracao_vars")
        token = self.lexico.pop_token()
        while is_identificador(token):

            if not self.semantico.pesquisa_duplic_var_tabela(token):
                self.semantico.insere_tabela(token["token"], token['lexema'], 'variavel',nivel=self.semantico.nivel, i=self.semantico.qtd_var)

                self.semantico.qtd_var_local += 1
                self.semantico.qtd_var += 1
            else:
                self.semantico.mostra_erro('duplic_var', token)

            token = self.lexico.pop_token()
            if not is_virgula(token):
                if is_dois_pontos(token):
                    tipo = self.analisa_tipo()
                    if tipo:
                        self.semantico.coloca_tipo(tipo)
                        return True
                    else:    
                         self.mostra_erro('analisa_tipo', token)
                else:    
                     self.mostra_erro('is_dois_pontos', token)
            token =  self.lexico.pop_token()        
        self.mostra_erro('is_identificador', token)

    def analisa_tipo(self):
        print('--analisa_tipo')
        token = self.lexico.pop_token()
        if is_inteiro(token) or is_booleano(token):
            # self.semantico.coloca_tipo_tabela(token['lexema'])
            return token['token']
        else:
            self.mostra_erro('is_tipo', token)

    def analisa_etapa_declaracao_sub_rotinas(self):
        print('--analisa_etapa_declaracao_sub_rotinas')
        auxrot = None
        flag = False
        token = self.lexico.pop_token()
        if is_procedimento(token) or is_funcao(token):
            auxrot = self.semantico.rotulo
            self.semantico.gera(comando='JMP', attr1="L"+str(self.semantico.rotulo))
            self.semantico.rotulo += 1
            flag = True

        while is_procedimento(token) or is_funcao(token):
            # token = self.lexico.pop_token()
            if is_procedimento(token):
                print("entrei")
                self.analisa_declaracao_procedimento(token)
                # token = self.lexico.pop_token()
                # if not is_ponto_virgula(token, 'dec_sub_rotinas'):
                    # self.mostra_erro('is_ponto_virgula', token)
            elif is_funcao(token):
                self.analisa_declaracao_funcao(token)
            token = self.lexico.pop_token()
            if not is_ponto_virgula(token, 'dec_sub_rotinas'):
                self.mostra_erro('is_ponto_virgula', token)
            else:
                token = self.lexico.pop_token()

        if is_inicio(token):
            self.lexico.insert_token(token)
        if flag:
            self.semantico.gera(rotulo=auxrot, comando='NULL')

    def analisa_declaracao_procedimento(self, token):
        print("--analisa_declaracao_procedimento")
        if is_procedimento(token):
            token = self.lexico.pop_token()

            # self.semantico.nivel = 'L'

            if is_identificador(token):
                if not self.semantico.pesquisa_declproc_tabela(token):
                    self.semantico.insere_tabela(token["token"], token['lexema'], 'procedimento', nivel=self.semantico.nivel, rotulo=self.semantico.rotulo)
                    self.semantico.gera(rotulo=self.semantico.rotulo, comando='NULL')
                    self.semantico.rotulo += 1

                    token = self.lexico.pop_token()
                    if is_ponto_virgula(token, 'ana_dec_proc'):
                        self.analisa_bloco()
                        dalloc = self.semantico.pilha_alloc.pop()
                        self.semantico.gera(comando='DALLOC', attr1=dalloc[0], attr2=dalloc[1])
                        self.semantico.gera(comando='RETURN')
                        return True
                    else:            
                        self.mostra_erro('is_ponto_virgula', token)
                else:
                    self.semantico.mostra_erro('decl_proc', token)

            else:            
                self.mostra_erro('is_identificador', token)
        else:            
            self.semantico.volta_nivel()
            self.mostra_erro('is_identificador', token)

    def analisa_declaracao_funcao(self, token=None): 
        print('--analisa_declaracao_funcao')
        if is_funcao(token):
            token = self.lexico.pop_token()
            # self.semantico.nivel = 'L'
            if is_identificador(token):

                if self.semantico.pesquisa_declfunc_tabela(token['lexema'], self.semantico.nivel):
                    self.semantico.insere_tabela(token["token"], token['lexema'], 'funcao', self.semantico.nivel, self.semantico.rotulo)
                    self.semantico.gera(comando='NULL', attr1=self.semantico.nivel)
                    self.semantico.nivel += 1

                    token = self.lexico.pop_token()
                    if is_dois_pontos(token):
                        
                        token = self.lexico.pop_token()
                        if is_inteiro(token) or is_booleano(token):
                            if is_inteiro(token):
                                self.semantico.tabela[0]['tipo_lexema'] = 'função inteiro'
                                self.semantico.tabela[0]['tipo_especifico'] = 'inteiro'
                            else:
                                self.semantico.tabela[0]['tipo_lexema'] = 'função boolean'
                                self.semantico.tabela[0]['tipo_especifico'] = 'boolean'
                            token = self.lexico.pop_token()
                            if is_ponto_virgula(token, 'ana_dec_func'):
                                self.analisa_bloco()
                                return True
                        else:            
                            self.mostra_erro('func_erro_tipo', token)
                    else:            
                        self.mostra_erro('is_dois_pontos', token)
                else:
                    self.semantico.mostra_erro('decl_func', token)
            else:            
                self.mostra_erro('is_identificador', token)
            #semantico: desempilha ou volta nself.nivelivel
        else:            
            self.mostra_erro('is_funcao', token)


    def analisa_comandos(self):
        print('--analisa_comandos')
        token = self.lexico.pop_token()
        if is_inicio(token):
            self.analisa_comando()
            token = self.lexico.pop_token()
            while not is_fim(token):
                # if is_ponto_final(token):
                    # dalloc = self.semantico.pilha_alloc.pop()
                    # self.semantico.gera(comando='DALLOC', attr1=dalloc[0], attr2=dalloc[1])
                    # self.semantico.gera(comando='RETURN')
                    # break
                if is_ponto_virgula(token, 'ana_com'):
                    token = self.lexico.get_token()
                    if not is_fim(token):
                        self.analisa_comando()

                    token = self.lexico.pop_token()
                else:    
                    self.mostra_erro('is_ponto_virgula', token)
        else:            
            self.mostra_erro('is_inicio', token)

    def analisa_comando(self):
        print('--analisa_comando')
        token = self.lexico.get_token()
        if is_identificador(token):
            var_ind = self.semantico.get_indice_var(token['token'])
            # if var_ind:
                # token = self.lexico.pop_token()
                
            tipo = self.semantico.retorna_tipo_especifico(token['token'])
            _, posicao_mem, _ = self.semantico.pesquisa_tabela(token['token'], self.semantico.nivel)
            token = self.lexico.pop_token()
            self.analisa_atribuicao_chprocedimento(tipo, posicao_mem, token)
        elif is_se(token):
            self.analisa_comando_condicional()
        elif is_enquanto(token):
            self.analisa_comando_enquanto()
        elif is_leia(token): 
            self.semantico.gera(comando='RD')
            self.analisa_comando_leitura()
        elif is_escreva(token):
            self.analisa_comando_escrita()
        else:
            self.analisa_comandos()

    def analisa_atribuicao_chprocedimento(self, tipo, posicao_mem, token_anterior):
        print('--analisa_atribuicao_chprocedimento')
        token = self.lexico.pop_token()
        if is_atribuicao(token):
            self.analisa_comando_atribuicao(tipo,posicao_mem)
        else:    
            self.lexico.insert_token(token)
            if not token['token'] == ";":
                self.lexico.insert_token(token_anterior)
            self.analisa_chamada_procedimento()

    def analisa_comando_atribuicao(self, tipo, posicao_mem, token=None):
        print('--analisa_comando_atribuicao')
        token = self.lexico.get_token()
        tipo_retorno = self.semantico.retorna_tipo_especifico(token['token'])
        if tipo_retorno:
            _, tipo_retorno = self.analisa_expressao()
            if tipo != tipo_retorno:
                self.semantico.mostra_erro('inc_tipo', token)
            else:
                self.semantico.gera(comando="STR", attr1=posicao_mem)    
        # elif token['token'].isdigit():
            # return
        else:
            self.semantico.mostra_erro('inc_ident', token)


    def analisa_chamada_procedimento(self):
        token = self.lexico.get_token()
        # if is_identificador(token):
        exists, nivel, rotulo = self.semantico.get_nivel_rotulo_procedimento(token['token'])    
        if exists:
            self.semantico.gera(comando='CALL', attr1='L'+str(rotulo))
            self.lexico.pop_token()
            return True

    def analisa_comando_condicional(self):
        print('--analisa_comando_condicional')

        executando_se = True

        token = self.lexico.pop_token()
        if is_se(token):
            self.analisa_expressao()
            token = self.lexico.pop_token()
            if is_entao(token):
                self.semantico.gera(comando='JMPF', attr1='L'+str(self.semantico.rotulo))
                self.semantico.rotulo += 1

                self.analisa_comando()

                self.semantico.gera(comando='JMP', attr1='L'+str(self.semantico.rotulo))
                self.semantico.gera(rotulo=self.semantico.rotulo-1, comando='NULL')
                self.semantico.rotulo += 1

                token = self.lexico.get_token()
                if is_senao(token):
                    self.lexico.pop_token()
                    self.analisa_comando()
                    
                self.semantico.gera(rotulo=self.semantico.rotulo-1, comando='NULL')
                return True
            else:            
                self.mostra_erro('is_entao', token)
        else:            
            self.mostra_erro('is_se', token)

    def analisa_comando_enquanto(self):
        auxrot1 = None
        auxrot2 = None

        token = self.lexico.pop_token()
        if is_enquanto(token):

            auxrot1 = self.semantico.rotulo
            self.semantico.gera(rotulo=self.semantico.rotulo, comando='NULL')
            self.semantico.rotulo += 1

            self.analisa_expressao()
            token = self.lexico.pop_token()
            if is_faca(token):
                auxrot2 = self.semantico.rotulo
                self.semantico.gera(comando='JMPF', attr1='L'+str(self.semantico.rotulo))
                self.semantico.rotulo += 1

                self.analisa_comando()

                self.semantico.gera(comando='JMP', attr1='L'+str(auxrot1))
                self.semantico.gera(rotulo=auxrot2, comando='NULL')

                return True
            else:            
                self.mostra_erro('is_faca', token)
        else:            
            self.mostra_erro('is_enquanto', token)

    def analisa_comando_leitura(self): 
        print('--analisa_comando_leitura')
        token = self.lexico.pop_token()
        if is_leia(token):
            token = self.lexico.pop_token()
            if is_abre_parenteses(token):
                token = self.lexico.pop_token()
                if is_identificador(token):
                    
                    if self.semantico.pesquisa_declvar_tabela(token):
                        i = self.semantico.get_indice_var(token['token'])
                        self.semantico.gera(comando='STR', attr1=i)

                        token = self.lexico.pop_token()
                        if is_fecha_parenteses(token):
                            return True
                        else:            
                            self.mostra_erro('is_fecha_parenteses', token)

                    else:
                        self.semantico.mostra_erro('decl_var', token)

                else:            
                    self.mostra_erro('is_identificador', token)
            else:            
                self.mostra_erro('is_abre_parenteses', token)
        else:            
            self.mostra_erro('is_leia', token)

    def analisa_comando_escrita(self):
        print('--analisa_comando_escrita')
        token = self.lexico.pop_token()
        if is_escreva(token):
            token = self.lexico.pop_token()
            if is_abre_parenteses(token):
                token = self.lexico.pop_token()
                if is_identificador(token):
                    if self.semantico.pesquisa_declvar_tabela(token):
                        i = self.semantico.get_indice_var(token['token'])
                        self.semantico.gera(comando='LDV', attr1=i)
                        self.semantico.gera(comando='PRN')
                        token = self.lexico.pop_token()
                        if is_fecha_parenteses(token):
                            return True
                        else:            
                            self.mostra_erro('is_fecha_parenteses', token)
                    else:
                        self.semantico.mostra_erro('decl_var', token)
                else:            
                    self.mostra_erro('is_identificador', token)
            else:            
                self.mostra_erro('is_abre_parenteses', token)
        else:            
            self.mostra_erro('is_escreva', token)

    def analisa_expressao(self):
        print('--analisa_expressao')
        self.expressao_temp = ""
        _, return_tipo = self.analisa_expressao_simples()
        token = self.lexico.get_token()

        if return_tipo == "inteiro":
            if is_operador(['>', '>=', '==', '<', '<=', '!='], token):
                self.semantico.empilha_operador({'lexema':token['token'], 'prioridade':3, 'tipo':'comparadores'})
                token = self.lexico.pop_token()
                _, return_tipo = self.analisa_expressao_simples()

                if return_tipo == "inteiro":
                    self.semantico.desempilha_operador()
                    return True, 'booleano'
                else:
                    raise self.semantico.mostra_erro('not_boolean', token)

        if token['lexema'] != 'sfecha_parenteses':
            self.semantico.desempilha_operador()

        return True, return_tipo 

    def analisa_funcao(self):
        print('--analisa_funcao')
        token = self.lexico.pop_token()
        if is_identificador(token):
            self.semantico.gera(comando='CALL', attr1=self.semantico.nivel+str(self.semantico.rotulo))
            return self.semantico.retorna_tipo_especifico(token['token'])
        else:            
            self.mostra_erro('is_identificador', token)

    def analisa_expressao_simples(self):
        print('--analisa_expressao_simples')
        token = self.lexico.get_token()
        self.semantico.aux_tipos = []
        if is_operador(['+','-'], token):
            token = self.lexico.pop_token()
            self.semantico.aux_tipos.append('inteiro')
        self.semantico.aux_tipos.append(self.analisa_termo())
        token = self.lexico.get_token()
        while is_operador(['+','-','ou'], token):
            if is_operador(['+', '-'], token):
                self.semantico.empilha_operador({'lexema':token['token'],'tipo':'maisMenos','prioridade':0})
                self.semantico.aux_tipos.append('inteiro')
            else:
                self.semantico.empilha_operador({'lexema':token['token'],'tipo':'ou','prioridade':2})
                self.semantico.aux_tipos.append('booleano')
                
            token = self.lexico.pop_token()
            self.semantico.aux_tipos.append(self.analisa_termo())
            token = self.lexico.get_token()
            
        return True, self.semantico.aux_tipos[0]

    def analisa_termo(self):
        print('--analisa_termo')
        # flag = False
        print('primeiro fator')
        # self.semantico.aux_tipos = []
        self.semantico.aux_tipos.append(self.analisa_fator())
        token = self.lexico.get_token()
        while is_operador(['*','div','e'], token):
            if is_operador(['*', 'div'], token):
                self.semantico.aux_tipos.append('inteiro')
                self.semantico.empilha_operador({'lexema':token['token'],'tipo':'multDiv','prioridade':5})
            else:
                self.semantico.aux_tipos.append('booleano')
                self.semantico.empilha_operador({'lexema':token['token'],'tipo':'e','prioridade':2})

            self.semantico.verifica_compatibilidade_tipos(token['linha'])
            token = self.lexico.pop_token()
            print('segundo fator')
            self.semantico.aux_tipos.append(self.analisa_fator())
            token = self.lexico.get_token()
        
        self.semantico.verifica_compatibilidade_tipos(token['linha'])
        return self.semantico.aux_tipos[0]

    def analisa_fator(self):
        print('--analisa_fator')
        token = self.lexico.get_token()
        self.expressao_temp += " "+token["token"]
        if is_identificador(token):

            flag, mem, i =  self.semantico.pesquisa_tabela(token['token'], self.semantico.nivel)
            if not flag:
                raise self.semantico.mostra_erro('inc_ident', token)

            if self.semantico.tabela[i]['tipo_especifico'] == "inteiro":
                if self.semantico.tabela[i]['tipo_lexema'] == "variavel":
                    self.semantico.gera(comando="LDV", attr1=int(mem))
                    self.lexico.pop_token()
                    return "inteiro"
                else:
                    return self.analisa_funcao()
            else:
                if self.semantico.tabela[i]['tipo_lexema'] == "variavel":
                    self.semantico.gera(comando="LDV", attr1=int(i))
                    self.lexico.pop_token()
                    return "booleano"
                else:
                    return self.analisa_funcao()
        else: 
            if is_numero(token):
                self.semantico.gera(comando='LDC', attr1=int(token['token']))
                self.lexico.pop_token()
                return 'inteiro'
            else:
                if is_nao(token):
                    self.semantico.empilha_operador({'lexema':'nao','tipo':'unarios', 'prioridade':6})
                    self.lexico.pop_token()
                    return self.analisa_fator()
                else:
                    if is_abre_parenteses(token):
                        self.semantico.empilha_operador({'lexema':'(','tipo':'parenteses', 'prioridade':0})
                        self.lexico.pop_token()
                        _, retorno_expressao = self.analisa_expressao()
                        token = self.lexico.pop_token()
                        if is_fecha_parenteses(token):
                            self.semantico.desempilha_operador()
                            # token = self.lexico.pop_token()
                        else:
                            self.semantico.mostra_erro('fecha_parenteses', token)
                        return retorno_expressao    
                    else:
                        if is_verdadeiro(token):        
                            self.semantico.gera(comando="LDC", attr1=1)
                            self.lexico.pop_token()
                            return True, 'booleano'
                        elif is_falso(token):        
                            self.semantico.gera(comando="LDC", attr1=0)
                            self.lexico.pop_token()
                            return True, 'booleano'
                        else:
                            self.semantico.mostra_erro('fator_desconhecido', token)


if __name__ == '__main__':
    try:
        s = Sintatico()
        s.analisa_programa()
    except Exception as e:
        traceback.print_exc()
        print(str(e))
    print('gera:', pp.pprint(s.semantico.assemble))
    print('tabela:', pp.pprint(s.semantico.tabela))

    with open('cod_saida.txt', 'w') as f:
        for i in reversed(s.semantico.assemble):
            if i['comando'] == 'NULL':
                i['comando'] = "L"+str(i['rotulo'])
                attr1 = "NULL"
            # elif i['rotulo']:
                # attr1 = "L"+str(i['rotulo'])
                # attr2 = ""
            else:
                attr1 = i['attr1'] if i['attr1'] is not None  else ''
                attr2 = ", "+str(i['attr2']) if i['attr2'] is not None else ''
            f.write(i['comando']+" "+str(attr1)+" "+attr2+"\n")



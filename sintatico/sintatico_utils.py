import re
def is_programa(token):
    print(token['token']+" == sprograma")
    return token['lexema'] == 'sprograma'


def is_virgula(token):
    print(token['token']+" == svirgula")
    return token['lexema'] == 'svirgula'

def is_dois_pontos(token):
    print(token['token']+" == sdois_pontos")
    return token['lexema'] == 'sdois_pontos'

def is_ponto_virgula(token, funcao_nome):
    print(token['token']+" == sponto_virgula - "+funcao_nome)
    return token['lexema'] == 'sponto_virgula'

def is_ponto_final(token):
    print(token['token']+" == sponto_final")
    return token['lexema'] == 'sponto_final'

def is_var(token):
    print(token['token']+" == svar")
    return token['lexema'] == 'svar'

def is_inteiro(token):
    print(token['token']+" == sinteiro")
    return token['lexema'] == 'sinteiro'

def is_booleano(token):
    print(token['token']+" == sbooleano")
    return token['lexema'] == 'sbooleano'

def is_procedimento(token):
    print(token['token']+" == sprocedimento - "+token['lexema'])
    return token['lexema'] == 'sprocedimento'

def is_funcao(token):
    print(token['token']+" == sfuncao")
    return token['lexema'] == 'sfuncao'

def is_inicio(token):
    print(token['token']+" == sinicio")
    return token['lexema'] == 'sinicio'

def is_se(token):
    print(token['token']+" == sse")
    return token['lexema'] == 'sse'

def is_maior(token):
    print(token['token']+" == smaior")
    return token['lexema'] == 'smaior'

def is_numero(token):
    print(token['token']+" == snumero")
    return token['lexema'] == 'snumero'

def is_entao(token):
    print(token['token']+" == sentao")
    return token['lexema'] == 'sentao'

def is_atribuicao(token):
    print(token['token']+" == satribuicao")
    return token['lexema'] == 'satribuicao'

def is_senao(token):
    print(token['token']+" == ssenao")
    return token['lexema'] == 'ssenao'

def is_enquanto(token):
    print(token['token']+" == senquanto")
    return token['lexema'] == 'senquanto'

def is_leia(token):
    print(token['token']+" == sleia")
    return token['lexema'] == 'sleia'

def is_verdadeiro(token):
    print(token['token']+" == sverdadeiro")
    return token['lexema'] == 'sverdadeiro'

def is_falso(token):
    print(token['token']+" == sfalso")
    return token['lexema'] == 'sfalso'

def is_nao(token):
    print(token['token']+" == snao")
    return token['lexema'] == 'snao'

def is_faca(token):
    print(token['token']+" == sfaca")
    return token['lexema'] == 'sfaca'

def is_escreva(token):
    print(token['token']+" == sescreva")
    return token['lexema'] == 'sescreva'

def is_abre_parenteses(token):
    print(token['token']+" == sabre_parenteses")
    return token['lexema'] == 'sabre_parenteses'

def is_fecha_parenteses(token):
    print(token['token']+" == sfecha_parenteses")
    return token['lexema'] == 'sfecha_parenteses'

def is_operador(options, token):
    print(token['token']+" == "+str(options))
    return token['token'] in options

def is_fim(token):
    print(token['token']+" == sfim")
    return token['lexema'] == "sfim"

def is_operador_relacional(token):
    print(token['token']+" == soprelacional")
    op_relacionais = ['!=','=','<','<=','>','>=']
    return token['token'] in op_relacionais

def is_identificador(token):
    print(token['token']+" == sidentificador")
    # return re.fullmatch(r'(^[a-zA-Z]([\w\d]*)?)', token['token'])
    return token['lexema'] == 'sidentificador'

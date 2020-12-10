import re 
from tkinter.filedialog import askopenfilename

class Lexico:
    def __init__(self):
        self.txt_arquivo = ""
        self.TOKENS = []
        self.TOKENS_DICT = {
                  "programa": "sprograma",
                  "inicio": "sinicio",
                  "fim": "sfim",
                  "procedimento": "sprocedimento",
                  "funcao": "sfuncao",
                  "se": "sse",
                  "entao": "sentao",
                  "senao": "ssenao",
                  "enquanto": "senquanto",
                  "faca": "sfaca",
                  "escreva": "sescreva",
                  "leia": "sleia",
                  "var": "svar",
                  "inteiro": "sinteiro",
                  "booleano": "sbooleano",
                  "identificador": "sidentificador",
                  "numero": "snumero",
                  ".": "sponto_final",
                  ";": "sponto_virgula",
                  ",": "svirgula",
                  "(": "sabre_parenteses",
                  ")": "sfecha_parenteses",
                  ">": "smaior",
                  ":=": "satribuicao",
                  ">=": "smaiorig",
                  "=": "sig",
                  "<": "smenor",
                  "<=": "smenorig",
                  "!=": "sdif",
                  "+": "smais",
                  "-": "smenos",
                  "*": "smult",
                  "div": "sdiv",
                  "e": "se",
                  "ou": "sou",
                  "nao": "snao",
                  ":": "sdois_pontos"
                }

        self.LISTA_REGRAS = {
            "sprograma":"programa",
            "sinicio":"inicio",
            "sfim":"fim",
            "sprocedimento":"procedimento",
            "sfuncao":"funcao",
            "sse":"se",
            "ssenao":"senao",
            "senquanto":"enquanto",
            "sfaca":"faca",
            "sescreva":"escreva",
            "sinteiro":"inteiro",
            "sentao":"entao",
            "sbooleano":"booleano",
            "sleia":"leia",
            "sidentificador":"(^[a-zA-Z]([\w\d]*)?)",
            "snumero":"^\d+\.?(\d+)?",
            "sabre_parenteses":"^\(",
            "satribuicao":":=",
            "smaiorig":">=",
            "smenorig":"<=",
            "smaior":">",
            "smenor":"<",
            "sdif":"!=",
            "snao":"nao",
            "se":" e ",
            "sou":"ou",
            "sdiv":"div",
            "smenos":"-",
            "svirgula":",",
            "sdois_pontos":":",
            "smais":"\+",
            "sfecha_comentario":"}",
            "sfecha_comentario2":"\*/",
            "smult":"\*",
            "sfecha_parenteses":"\)",
            "sponto_virgula":"\;",

            
        }
    def inicia_lexico(self):
        if self.txt_arquivo:
            #remover comentários
            # texto_sem_comentario = re.sub('{.*[^}]}', '', self.txt_arquivo)
            texto_sem_comentario = re.sub('{.*?(?=}).', '', self.txt_arquivo, flags=re.S)
            texto_sem_comentario = re.sub('\/\*.*?(?=\*\/)..', '', texto_sem_comentario, flags=re.S)

            for i, texto_linha in enumerate(texto_sem_comentario.split('\n')):
                for token in texto_linha.split():
                    if not self.aplica_regras(i, token):
                        exit()

    def le_arquivo(self):
        self.txt_arquivo = ""
        self.lexemas_simbolos = []
        filename = askopenfilename() 
        try:
            with open(filename, "r", encoding="utf-8") as f:
                self.txt_arquivo = f.read()
        except:
            with open(filename, "r", encoding="iso-8859-1") as f:
                self.txt_arquivo = f.read()


    def aplica_regra_recursiva(self, regra, i, token):
        if re.match(self.LISTA_REGRAS[regra], token): 
            sub_token = re.match(self.LISTA_REGRAS[regra], token).group() 
            print("{} - {}".format(sub_token, regra))
            self.TOKENS.append({"lexema":regra, "token":sub_token, "linha":i})#{"lexema":sub_token, "simbolo":regra, "linha":i})
            token = token.replace(sub_token, '', 1)
            return True, token 
        return False, token
    
    def aplica_regras(self, i, token):
        mensagem = "Erro geral: Linha {} - {} não faz parte da linguagem".format(i+1, token)
        try:
            print("{} - {}".format(token, self.TOKENS_DICT[token]))
            self.TOKENS.append({"lexema":self.TOKENS_DICT[token], "token":token, "linha":i})#{"lexema":token, "simbolo":self.TOKENS_DICT[token], "linha":i})
            return True
        except KeyError:
            #verifica se é variável
            for regra, lexema in self.LISTA_REGRAS.items():
                # print("Aplicando regra: {} no token {}".format(regra, token))
                if token in ['*/', '}']:
                    mensagem = "Erro geral: Linha {} - {} não possui inicia comentário".format(i+1, token)
                    break
                flag, token = self.aplica_regra_recursiva(regra, i, token) #se for dígito
                if flag:
                    if not token:
                        return True
                    else:
                        return self.aplica_regras(i, token)

            print(mensagem)
            return False

                
    def pop_token(self):
        if self.TOKENS:
            return self.TOKENS.pop(0)
        else:
            return None

    def get_token(self):
        if self.TOKENS:
            return self.TOKENS[0]
        else:
            return None

    def insert_token(self, token):
        if self.TOKENS:
            return self.TOKENS.insert(0, token)
        else:
            return None

if __name__ == '__main__':
    l = Lexico()
    l.inicia_lexico()

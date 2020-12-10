#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Aug 19, 2020 12:10:30 PM -03  platform: Windows NT

import sys
import traceback

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import maquina_virtual_support
from .commands import MV

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    maquina_virtual_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    maquina_virtual_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        # Dicionario dos Comentarios das Instrucoes
        self.COMENTARIOS_DICT = {
            "LDC": "S:=s + 1 ; M [s]: = k",
            "LDV": "S:=s + 1 ; M[s]:=M[n]",
            "ADD": "M[s-1]:=M[s-1] + M[s]; s:=s - 1",
            "SUB": "M[s-1]:=M[s-1] - M[s]; s:=s - 1",
            "MULT": "M[s - 1] := M[s - 1] * M[s]; s := s - 1",
            "DIVI": "M[s - 1] := M[s - 1] div M[s]; s := s - 1",
            "INV": "M[s] := -M[s]",
            "AND": "se M[s - 1] = 1 e M[s] = 1 então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1",
            "OR": "se M[s - 1] = 1 ou M[s] = 1 então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1",
            "NEG": "M[s] := 1 - M[s]",
            "CME": "se M[s - 1] < M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1",
            "CMA": "se M[s - 1] > M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1",
            "CEQ": "se M[s - 1] = M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1",
            "CDIF": "se M[s - 1] ≠ M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1",
            "CMEQ": "se M[s - 1] ≤ M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1",
            "CMAQ": "se M[s - 1] ≥ M[s] então M[s - 1] := 1 senão M[s - 1] := 0; s := s - 1",
            "START": "S := -1",
            "HLT": "“Pára a execução da MVD”",
            "STR": "M[n] := M[s]; s := s - 1",
            "JMP": "i := t",
            "JMPF": "se M[s] = 0 então i := t senão i := i + 1; s := s - 1",
            "NULL": "(Nada)",
            "RD":"S := s + 1; M[s] := “próximo valor de entrada”",
            "PRN": "“Imprimir M[s]”; s := s - 1 ",
            "ALLOC": "Para k := 0 até n - 1 faça { s := s + 1; M[s] := M[m + k] }",
            "DALLOC": "Para k := n - 1 até 0 faça { M[m + k] := M[s]; s := s - 1 }",
            "CALL": "S := s + 1; M[s] := i + 1; i := t",
            "RETURN": "i := M[s]; s := s - 1"
        }

        top.geometry("1576x941+308+3")
        top.minsize(148, 1)
        top.maxsize(4804, 1325)
        top.resizable(1, 1)
        top.title("Simulador")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.006, rely=0.011, relheight=0.846, relwidth=0.987)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.006, rely=0.013, relheight=0.069, relwidth=0.755)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")

        self.title_instrucoes = tk.Label(self.Frame2)
        self.title_instrucoes.place(relx=0.20, rely=0.182, height=26, width=600)
        self.title_instrucoes.configure(background="#d9d9d9")
        self.title_instrucoes.configure(disabledforeground="#a3a3a3")
        self.title_instrucoes.configure(foreground="#000000")
        self.title_instrucoes.configure(text='''Instrucoes a serem executadas pela MV''')
        self.title_instrucoes.configure(fg="navy blue")
        self.title_instrucoes.configure(font="Helvetica 16 bold")

        self.Frame3 = tk.Frame(self.Frame1)
        self.Frame3.place(relx=0.765, rely=0.013, relheight=0.069, relwidth=0.228)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")

        self.title_conteudo = tk.Label(self.Frame3)
        self.title_conteudo.place(relx=0.230, rely=0.182, height=26, width=200)
        self.title_conteudo.configure(background="#d9d9d9")
        self.title_conteudo.configure(disabledforeground="#a3a3a3")
        self.title_conteudo.configure(foreground="#000000")
        self.title_conteudo.configure(text='''Conteudo da Pilha''')
        self.title_conteudo.configure(fg="navy blue")
        self.title_conteudo.configure(font="Helvetica 16 bold")

        self.title_I = tk.Label(self.Frame1)
        self.title_I.place(relx=0.025, rely=0.101, height=27, width=40)
        self.title_I.configure(background="#d9d9d9")
        self.title_I.configure(disabledforeground="#a3a3a3")
        self.title_I.configure(foreground="#000000")
        self.title_I.configure(text='''I''')
        self.title_I.configure(fg="black")
        self.title_I.configure(font="Arial 12 bold")

        self.title_instrucao = tk.Label(self.Frame1)
        self.title_instrucao.place(relx=0.070, rely=0.101, height=27, width=100)
        self.title_instrucao.configure(background="#d9d9d9")
        self.title_instrucao.configure(disabledforeground="#a3a3a3")
        self.title_instrucao.configure(foreground="#000000")
        self.title_instrucao.configure(text='''Instrucao''')
        self.title_instrucao.configure(fg="black")
        self.title_instrucao.configure(font="Arial 12 bold")

        self.title_atributo_1 = tk.Label(self.Frame1)
        self.title_atributo_1.place(relx=0.157, rely=0.101, height=27, width=100)
        self.title_atributo_1.configure(background="#d9d9d9")
        self.title_atributo_1.configure(disabledforeground="#a3a3a3")
        self.title_atributo_1.configure(foreground="#000000")
        self.title_atributo_1.configure(text='''Atributo #1''')
        self.title_atributo_1.configure(fg="black")
        self.title_atributo_1.configure(font="Arial 12 bold")

        self.title_atributo_2 = tk.Label(self.Frame1)
        self.title_atributo_2.place(relx=0.239, rely=0.101, height=27, width=100)
        self.title_atributo_2.configure(background="#d9d9d9")
        self.title_atributo_2.configure(disabledforeground="#a3a3a3")
        self.title_atributo_2.configure(foreground="#000000")
        self.title_atributo_2.configure(text='''Atributo #2''')
        self.title_atributo_2.configure(fg="black")
        self.title_atributo_2.configure(font="Arial 12 bold")

        self.title_comentario = tk.Label(self.Frame1)
        self.title_comentario.place(relx=0.469, rely=0.101, height=27, width=150)
        self.title_comentario.configure(background="#d9d9d9")
        self.title_comentario.configure(cursor="fleur")
        self.title_comentario.configure(disabledforeground="#a3a3a3")
        self.title_comentario.configure(foreground="#000000")
        self.title_comentario.configure(text='''Comentario''')
        self.title_comentario.configure(fg="black")
        self.title_comentario.configure(font="Arial 12 bold")

        self.title_endereco = tk.Label(self.Frame1)
        self.title_endereco.place(relx=0.80, rely=0.101, height=27, width=90)
        self.title_endereco.configure(background="#d9d9d9")
        self.title_endereco.configure(disabledforeground="#a3a3a3")
        self.title_endereco.configure(foreground="#000000")
        self.title_endereco.configure(text='''Endereco''')
        self.title_endereco.configure(fg="black")
        self.title_endereco.configure(font="Arial 12 bold")

        self.title_valor = tk.Label(self.Frame1)
        self.title_valor.place(relx=0.907, rely=0.101, height=27, width=65)
        self.title_valor.configure(background="#d9d9d9")
        self.title_valor.configure(disabledforeground="#a3a3a3")
        self.title_valor.configure(foreground="#000000")
        self.title_valor.configure(text='''Valor''')
        self.title_valor.configure(fg="black")
        self.title_valor.configure(font="Arial 12 bold")

        self.title_janela_in = tk.Label(self.Frame1)
        self.title_janela_in.place(relx=0.055, rely=0.704, height=27, width=200)
        self.title_janela_in.configure(background="#d9d9d9")
        self.title_janela_in.configure(disabledforeground="#a3a3a3")
        self.title_janela_in.configure(foreground="#000000")
        self.title_janela_in.configure(text='''Janela de Entrada''')
        self.title_janela_in.configure(fg="navy blue")
        self.title_janela_in.configure(font="Helvetica 16 bold")

        self.title_janela_out = tk.Label(self.Frame1)
        self.title_janela_out.place(relx=0.270, rely=0.704, height=27, width=200)
        self.title_janela_out.configure(background="#d9d9d9")
        self.title_janela_out.configure(cursor="fleur")
        self.title_janela_out.configure(disabledforeground="#a3a3a3")
        self.title_janela_out.configure(foreground="#000000")
        self.title_janela_out.configure(text='''Janela de Saida''')
        self.title_janela_out.configure(fg="navy blue")
        self.title_janela_out.configure(font="Helvetica 16 bold")

        self.title_breakpoints = tk.Label(self.Frame1)
        self.title_breakpoints.place(relx=0.560, rely=0.704, height=27, width=230)
        self.title_breakpoints.configure(background="#d9d9d9")
        self.title_breakpoints.configure(disabledforeground="#a3a3a3")
        self.title_breakpoints.configure(foreground="#000000")
        self.title_breakpoints.configure(text='''Break Point's''')
        self.title_breakpoints.configure(fg="navy blue")
        self.title_breakpoints.configure(font="Helvetica 16 bold")

        self.Listbox_I = tk.Listbox(self.Frame1)
        self.Listbox_I.place(relx=0.013, rely=0.138, relheight=0.539, relwidth=0.048)
        self.Listbox_I.configure(background="white")
        self.Listbox_I.configure(disabledforeground="#a3a3a3")
        self.Listbox_I.configure(font="TkFixedFont")
        self.Listbox_I.configure(foreground="#000000")

        self.Listbox_instrucao = tk.Listbox(self.Frame1)
        self.Listbox_instrucao.place(relx=0.064, rely=0.138, relheight=0.538, relwidth=0.08)
        self.Listbox_instrucao.configure(background="white")
        self.Listbox_instrucao.configure(disabledforeground="#a3a3a3")
        self.Listbox_instrucao.configure(font="TkFixedFont")
        self.Listbox_instrucao.configure(foreground="#000000")

        self.Listbox_atributo_1 = tk.Listbox(self.Frame1)
        self.Listbox_atributo_1.place(relx=0.148, rely=0.138, relheight=0.539, relwidth=0.08)
        self.Listbox_atributo_1.configure(background="white")
        self.Listbox_atributo_1.configure(disabledforeground="#a3a3a3")
        self.Listbox_atributo_1.configure(font="TkFixedFont")
        self.Listbox_atributo_1.configure(foreground="#000000")

        self.Listbox_atributo_2 = tk.Listbox(self.Frame1)
        self.Listbox_atributo_2.place(relx=0.231, rely=0.138, relheight=0.539, relwidth=0.08)
        self.Listbox_atributo_2.configure(background="white")
        self.Listbox_atributo_2.configure(disabledforeground="#a3a3a3")
        self.Listbox_atributo_2.configure(font="TkFixedFont")
        self.Listbox_atributo_2.configure(foreground="#000000")

        self.Listbox_comentario = tk.Listbox(self.Frame1)
        self.Listbox_comentario.place(relx=0.315, rely=0.138, relheight=0.539, relwidth=0.445)
        self.Listbox_comentario.configure(background="white")
        self.Listbox_comentario.configure(disabledforeground="#a3a3a3")
        self.Listbox_comentario.configure(font="TkFixedFont")
        self.Listbox_comentario.configure(foreground="#000000")

        self.Listbox_endereco = tk.Listbox(self.Frame1)
        self.Listbox_endereco.place(relx=0.784, rely=0.138, relheight=0.839, relwidth=0.093)
        self.Listbox_endereco.configure(background="white")
        self.Listbox_endereco.configure(disabledforeground="#a3a3a3")
        self.Listbox_endereco.configure(font="TkFixedFont")
        self.Listbox_endereco.configure(foreground="#000000")

        self.Listbox_valor = tk.Listbox(self.Frame1)
        self.Listbox_valor.place(relx=0.88, rely=0.138, relheight=0.839, relwidth=0.093)
        self.Listbox_valor.configure(background="white")
        self.Listbox_valor.configure(disabledforeground="#a3a3a3")
        self.Listbox_valor.configure(font="TkFixedFont")
        self.Listbox_valor.configure(foreground="#000000")

        self.Listbox_janela_in = tk.Listbox(self.Frame1)
        self.Listbox_janela_in.place(relx=0.026, rely=0.741, relheight=0.236, relwidth=0.183)
        self.Listbox_janela_in.configure(background="white")
        self.Listbox_janela_in.configure(disabledforeground="#a3a3a3")
        self.Listbox_janela_in.configure(font="TkFixedFont")
        self.Listbox_janela_in.configure(foreground="#000000")

        self.Listbox_janela_out = tk.Listbox(self.Frame1)
        self.Listbox_janela_out.place(relx=0.238, rely=0.741, relheight=0.236, relwidth=0.19)
        self.Listbox_janela_out.configure(background="white")
        self.Listbox_janela_out.configure(disabledforeground="#a3a3a3")
        self.Listbox_janela_out.configure(font="TkFixedFont")
        self.Listbox_janela_out.configure(foreground="#000000")

        self.Listbox_breakpoints = tk.Listbox(self.Frame1)
        self.Listbox_breakpoints.place(relx=0.559, rely=0.741, relheight=0.236, relwidth=0.15)
        self.Listbox_breakpoints.configure(background="white")
        self.Listbox_breakpoints.configure(disabledforeground="#a3a3a3")
        self.Listbox_breakpoints.configure(font="TkFixedFont")
        self.Listbox_breakpoints.configure(foreground="#000000")

        self.Button_carrega_file = tk.Button(top)
        self.Button_carrega_file.place(relx=0.019, rely=0.882, height=53, width=256)
        self.Button_carrega_file.configure(activebackground="#ececec")
        self.Button_carrega_file.configure(activeforeground="#000000")
        self.Button_carrega_file.configure(background="#d9d9d9")
        self.Button_carrega_file.configure(disabledforeground="#a3a3a3")
        self.Button_carrega_file.configure(foreground="#000000")
        self.Button_carrega_file.configure(highlightbackground="#d9d9d9")
        self.Button_carrega_file.configure(highlightcolor="black")
        self.Button_carrega_file.configure(pady="0")
        self.Button_carrega_file.configure(text='''Carregar Arquivo''')
        self.Button_carrega_file.configure(command=self.carrega_arquivo)
        self.Button_carrega_file.configure(fg="black")
        self.Button_carrega_file.configure(font="Arial 12")


        self.Button_debug = tk.Button(top)
        self.Button_debug.place(relx=0.197, rely=0.882, height=53, width=256)
        self.Button_debug.configure(activebackground="#ececec")
        self.Button_debug.configure(activeforeground="#000000")
        self.Button_debug.configure(background="#d9d9d9")
        self.Button_debug.configure(disabledforeground="#a3a3a3")
        self.Button_debug.configure(foreground="#000000")
        self.Button_debug.configure(highlightbackground="#d9d9d9")
        self.Button_debug.configure(highlightcolor="black")
        self.Button_debug.configure(pady="0")
        self.Button_debug.configure(text='''DEBUG''')
        self.Button_debug.configure(fg="black")
        self.Button_debug.configure(font="Arial 12")

        self.Button_run = tk.Button(top)
        self.Button_run.place(relx=0.374, rely=0.882, height=53, width=256)
        self.Button_run.configure(activebackground="#ececec")
        self.Button_run.configure(command=self.run)
        self.Button_run.configure(activeforeground="#000000")
        self.Button_run.configure(background="#d9d9d9")
        self.Button_run.configure(disabledforeground="#a3a3a3")
        self.Button_run.configure(foreground="#000000")
        self.Button_run.configure(highlightbackground="#d9d9d9")
        self.Button_run.configure(highlightcolor="black")
        self.Button_run.configure(pady="0")
        self.Button_run.configure(text='''RUN''')
        self.Button_run.configure(fg="black")
        self.Button_run.configure(font="Arial 12")

        self.Listbox_I.bind("<Down>", self.down)
        self.Listbox_I.bind("<Up>", self.up)
        self.Listbox_I.bind("<Double-Button>", self.select)
        self.Listbox_instrucao.bind("<Down>", self.down)
        self.Listbox_instrucao.bind("<Up>", self.up)
        self.Listbox_atributo_1.bind("<Down>", self.down)
        self.Listbox_atributo_1.bind("<Up>", self.up)
        self.Listbox_atributo_2.bind("<Down>", self.down)
        self.Listbox_atributo_2.bind("<Up>", self.up)
        self.Listbox_comentario.bind("<Down>", self.down)
        self.Listbox_comentario.bind("<Up>", self.up)

    def select(self, event):
        widget = event.widget
        selection = widget.curselection()
        try:
            selection = selection[0]
            listbox_size = self.Listbox_breakpoints.size()
            if str(selection) in list(self.Listbox_breakpoints.get(0, listbox_size)):
                self.Listbox_breakpoints.delete(list(self.Listbox_breakpoints.get(0, listbox_size)).index(str(selection)))
                self.Listbox_I.itemconfig(selection, {'bg':'white'})
            else:
                self.Listbox_breakpoints.insert(listbox_size, str(selection))
                self.Listbox_I.itemconfig(selection, {'bg':'red'})

        except Exception as e:
            print(traceback.print_exc())
            print(str(e))

    def up(self, event):
        self.Listbox_I.yview_scroll(-1, "units")
        self.Listbox_instrucao.yview_scroll(-1, "units")
        self.Listbox_atributo_1.yview_scroll(-1, "units")
        self.Listbox_atributo_2.yview_scroll(-1, "units")
        self.Listbox_comentario.yview_scroll(-1, "units")

    def down(self, event):
        self.Listbox_I.yview_scroll(1, "units")
        self.Listbox_instrucao.yview_scroll(1, "units")
        self.Listbox_atributo_1.yview_scroll(1, "units")
        self.Listbox_atributo_2.yview_scroll(1, "units")
        self.Listbox_comentario.yview_scroll(1, "units")
    
    def run(self):
        lista_instrucao = list(self.Listbox_instrucao.get(0, tk.END))
        lista_atributo_1 = list(self.Listbox_atributo_1.get(0, tk.END))
        lista_atributo_2 = list(self.Listbox_atributo_2.get(0, tk.END))
        lista_breackpoints =list(self.Listbox_breakpoints.get(0, tk.END))

        lista_endereco = list(self.Listbox_endereco.get(0, tk.END))
        lista_valor = list(self.Listbox_valor.get(0, tk.END))

        mv = MV(lista_instrucao, lista_endereco, lista_atributo_1, lista_atributo_2, lista_valor)

        for i, commando in enumerate(lista_instrucao):
            if i in lista_breackpoints:
                #tem breackpoints
                print("Com breakpoint")
            else:
                #não tem breakpoints
                if commando == 'LDC':
                    k = lista_atributo_1[i]
                    mv.ldc(k)
                elif commando == 'LDV':
                    n = lista_atributo_1[i]
                    mv.ldv(n)
                elif commando == 'ALLOC':
                    m = lista_atributo_1[i]
                    n = lista_atributo_2[i]
                    mv.alloc(m, n)
                

    def carrega_arquivo(self):
        with open("./dados/programaMV.txt", "r") as f:
            for i, item in enumerate(f.readlines()):
                # inserir índice
                self.Listbox_I.insert(i, str(i))
                # pega só o comando
                item_splitado = item.split()
                comando = item_splitado[0]
                self.Listbox_instrucao.insert(i, str(comando))
                try:
                    self.Listbox_comentario.insert(i, self.COMENTARIOS_DICT[str(comando)])
                except:
                    self.Listbox_comentario.insert(i, "")
                # pega os parâmetros
                if len(item_splitado) > 1:
                    atributos = item_splitado[1].split(",")
                    self.Listbox_atributo_1.insert(i, str(atributos[0]))
                    if len(atributos) > 1:
                        self.Listbox_atributo_2.insert(i, str(atributos[1]))
                    else:
                        self.Listbox_atributo_2.insert(i, "")
                else:
                    self.Listbox_atributo_1.insert(i, "")
                    self.Listbox_atributo_2.insert(i, "")

if __name__ == '__main__':
    vp_start_gui() 

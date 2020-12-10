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

from tkinter import simpledialog
from tkinter.filedialog import askopenfilename
import maquina_virtual_support
from commands import MV

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

        self.mv = MV()
        
        self.i = 0
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        # Dicionario dos Comentarios das Instrucoes
        self.COMENTARIOS_DICT = {
            "LDC": "S:=s + 1 ; M[s]: = k",
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
        self.title_instrucoes.configure(text='''Instruções a serem executadas pela MV ''')
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
        self.title_conteudo.configure(text='''Conteúdo da Pilha ''')
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
        self.title_instrucao.configure(text='''Instrução''')
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
        self.title_comentario.configure(text='''Comentário''')
        self.title_comentario.configure(fg="black")
        self.title_comentario.configure(font="Arial 12 bold")

        self.title_endereco = tk.Label(self.Frame1)
        self.title_endereco.place(relx=0.80, rely=0.101, height=27, width=90)
        self.title_endereco.configure(background="#d9d9d9")
        self.title_endereco.configure(disabledforeground="#a3a3a3")
        self.title_endereco.configure(foreground="#000000")
        self.title_endereco.configure(text='''Endereço''')
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
        self.title_janela_in.place(relx=0.035, rely=0.704, height=27, width=250)
        self.title_janela_in.configure(background="#d9d9d9")
        self.title_janela_in.configure(disabledforeground="#a3a3a3")
        self.title_janela_in.configure(foreground="#000000")
        self.title_janela_in.configure(text='''Histórico de Entradas''')
        self.title_janela_in.configure(fg="navy blue")
        self.title_janela_in.configure(font="Helvetica 16 bold")

        self.title_janela_out = tk.Label(self.Frame1)
        self.title_janela_out.place(relx=0.270, rely=0.704, height=27, width=200)
        self.title_janela_out.configure(background="#d9d9d9")
        self.title_janela_out.configure(cursor="fleur")
        self.title_janela_out.configure(disabledforeground="#a3a3a3")
        self.title_janela_out.configure(foreground="#000000")
        self.title_janela_out.configure(text='''Janela de Saída''')
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

        #Botoes da Maquina Virtual
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
        self.Button_carrega_file.configure(text='''CARREGAR''')
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
        self.Button_debug.configure(command=lambda: self.run_comandos(debug=True))

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

        self.Button_continuar = tk.Button(top)
        self.Button_continuar.place(relx=0.550, rely=0.882, height=53, width=256)
        self.Button_continuar.configure(activebackground="#ececec")
        self.Button_continuar.configure(activeforeground="#000000")
        self.Button_continuar.configure(background="#d9d9d9")
        self.Button_continuar.configure(disabledforeground="#a3a3a3")
        self.Button_continuar.configure(foreground="#000000")
        self.Button_continuar.configure(highlightbackground="#d9d9d9")
        self.Button_continuar.configure(highlightcolor="black")
        self.Button_continuar.configure(pady="0")
        self.Button_continuar.configure(text='''CONTINUAR''')
        self.Button_continuar.configure(fg="black")
        self.Button_continuar.configure(font="Arial 12")
        self.Button_continuar.configure(command=lambda: self.run_comandos(breakpoint=True))

        # Atribuindo o evento Scroll nas Listboxs
        self.Listbox_I.bind("<Down>", self.down)
        self.Listbox_I.bind("<MouseWheel>", self.OnMouseWheel)
        self.Listbox_I.bind("<Up>", self.up)
        self.Listbox_I.bind("<Double-Button>", self.select)
        self.Listbox_instrucao.bind("<Down>", self.down)
        self.Listbox_instrucao.bind("<Up>", self.up)
        self.Listbox_instrucao.bind("<MouseWheel>", self.OnMouseWheel)
        self.Listbox_atributo_1.bind("<Down>", self.down)
        self.Listbox_atributo_1.bind("<Up>", self.up)
        self.Listbox_atributo_1.bind("<MouseWheel>", self.OnMouseWheel)
        self.Listbox_atributo_2.bind("<Down>", self.down)
        self.Listbox_atributo_2.bind("<Up>", self.up)
        self.Listbox_atributo_2.bind("<MouseWheel>", self.OnMouseWheel)
        self.Listbox_comentario.bind("<Down>", self.down)
        self.Listbox_comentario.bind("<Up>", self.up)
        self.Listbox_comentario.bind("<MouseWheel>", self.OnMouseWheel)

    #rolagem de todos os listboxes
    def OnMouseWheel(self, event):
        self.Listbox_I.yview_scroll(int(-1*(event.delta/120)),"units")
        self.Listbox_instrucao.yview_scroll(int(-1*(event.delta/120)),"units")
        self.Listbox_atributo_1.yview_scroll(int(-1*(event.delta/120)),"units")
        self.Listbox_atributo_2.yview_scroll(int(-1*(event.delta/120)),"units")
        self.Listbox_comentario.yview_scroll(int(-1*(event.delta/120)),"units")
        return "break"

    # Selecao dos Breakpoints
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

    # Para encontrar as linhas dos erros
        except Exception as e:
            print(traceback.print_exc())
            print(str(e))

    # Scroll das Listboxs
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

    # RUN
    def run(self):
        global root

        self.run_comandos()

    def run_comandos(self, breakpoint=False, debug=False):
        if not breakpoint and not debug:
            self.i = 0

        if breakpoint:
            self.i = self.i + 1

        lista_instrucao = list(self.Listbox_instrucao.get(0, tk.END))
        lista_atributo_1 = list(self.Listbox_atributo_1.get(0, tk.END))
        lista_atributo_2 = list(self.Listbox_atributo_2.get(0, tk.END))
        lista_breakpoints = [int(x) for x in list(self.Listbox_breakpoints.get(0, tk.END))]

        lista_janela_in = list(self.Listbox_janela_in.get(0, tk.END))

        lista_endereco = list(self.Listbox_endereco.get(0, tk.END))
        lista_valor = list(self.Listbox_valor.get(0, tk.END))

        while True:    
            self.pinta_I()
            self.Listbox_I.see(self.i)
            self.Listbox_instrucao.see(self.i)
            self.Listbox_atributo_1.see(self.i)
            self.Listbox_atributo_2.see(self.i)
            self.Listbox_comentario.see(self.i)
            comando, attr_1, attr_2 = self.busca_funcao(self.i, lista_instrucao, lista_atributo_1, lista_atributo_2) 
            self.mv.i = self.i
            if self.i in lista_breakpoints:
                #tem breakpoints
                print("Com breakpoint")
                break
            else:
                #não tem breakpoints
                if comando == 'LDC':
                    k = attr_1
                    self.mv.ldc(k)
                elif comando == 'LDV':
                    n = attr_1
                    self.mv.ldv(n)
                elif comando == 'ADD':
                    self.mv.add()
                elif comando == 'SUB':
                    self.mv.sub()
                elif comando == 'MULT':
                    self.mv.mult()
                elif comando == 'DIVI':
                    self.mv.divi()
                elif comando == 'INV':
                    self.mv.inv()
                elif comando == 'AND':
                    self.mv.funcao_and()
                elif comando == 'OR':
                    self.mv.funcao_or()
                elif comando == 'NEG':
                    self.mv.neg()
                elif comando == 'CME':
                    self.mv.cme()
                elif comando == 'CMA':
                    self.mv.cma()
                elif comando == 'CEQ':
                    self.mv.ceq()
                elif comando == 'CDIF':
                    self.mv.cdif()
                elif comando == 'CMEQ':
                    self.mv.cmeq()
                elif comando == 'CMAQ':
                    self.mv.cmaq()
                elif comando == 'START':
                    self.mv.start()
                elif comando == 'HLT':
                    # self.mv.hlt()
                    break
                elif comando == 'STR':
                    n = attr_1
                    self.mv.str(n)
                elif comando == 'JMP':
                    t = self.busca_indice_funcao(attr_1, lista_instrucao)
                    print("Indice da função é:", t)
                    self.mv.jmp(t)
                elif comando == 'JMPF':
                    t = self.busca_indice_funcao(attr_1, lista_instrucao)
                    print("Indice da função é:", t)
                    self.mv.jmpf(t)
                elif comando == 'NULL':
                    self.mv.null()
                elif comando == 'RD':
                    entrada = self.pede_entrada()
                    self.Listbox_janela_in.insert(tk.END, str(entrada))
                    self.mv.rd(entrada)
                elif comando == 'PRN':
                    saida = self.mv.prn()
                    self.Listbox_janela_out.insert(tk.END, str(saida))
                elif comando == 'ALLOC':
                    m = attr_1
                    n = attr_2
                    self.mv.alloc(m, n)
                elif comando == 'DALLOC':
                    m = attr_1
                    n = attr_2
                    self.mv.dalloc(m, n)
                elif comando == 'CALL':
                    t = self.busca_indice_funcao(attr_1, lista_instrucao)
                    print("Indice da função é:", t)
                    self.mv.call(t)
                elif comando == 'RETURN':
                    self.mv.funcao_return()
                else:
                    print('Procedimento:', comando)
            
            print('*'*20)
            print(self.Listbox_instrucao.get(self.i))
            print(self.Listbox_comentario.get(self.i))
            print("S:", self.mv.s)    
            print("I:", self.i)    
            print("MV.I:", self.mv.i)
            print("M:", self.mv.M)    
            print('*'*20)

            if self.i == self.mv.i:
                self.i += 1
            else:
                self.i = self.mv.i

            self.mv.converte_p_int() #Garante que todo o valor no "array" para int

            self.Listbox_valor.delete(0, tk.END)
            self.Listbox_endereco.delete(0, tk.END)

            for j, valor in enumerate(self.mv.M):
                self.Listbox_valor.insert(j, valor)
                self.Listbox_endereco.insert(j, j)

            self.Listbox_endereco.update_idletasks() #Atualiza a interface grafica na execucao
            root.update()

            if debug:
                break



    def pinta_I(self):
        for i in list(self.Listbox_I.get(0, tk.END)):
            i = int(i)
            if i == self.i:
                self.Listbox_I.itemconfig(i, {'bg':'green'})
            else:
                self.Listbox_I.itemconfig(i, {'bg':'white'})


    def pede_entrada(self):
        entrada = tk.simpledialog.askstring('Digite uma entrada', '')
        print(entrada)
        return entrada

    def busca_indice_funcao(self, nome_funcao, lista_instrucao):
        for i, comando in enumerate(lista_instrucao):
            if comando == nome_funcao:
                return i

    def busca_funcao(self, i, lista_instrucao, lista_atributo_1, lista_atributo_2):
        return (lista_instrucao[i], lista_atributo_1[i], lista_atributo_2[i])

    def continua_execucao(self, i, mv):
        self.run_comandos(i, mv)

    # Carrega Arquivo
    def carrega_arquivo(self):
        self.Listbox_I.delete(0, tk.END)
        self.Listbox_instrucao.delete(0, tk.END)
        self.Listbox_comentario.delete(0, tk.END)
        self.Listbox_atributo_1.delete(0, tk.END)
        self.Listbox_atributo_2.delete(0, tk.END)
        self.Listbox_endereco.delete(0, tk.END)
        self.Listbox_valor.delete(0, tk.END)
        self.Listbox_janela_in.delete(0, tk.END)
        self.Listbox_janela_out.delete(0, tk.END)
        self.Listbox_breakpoints.delete(0, tk.END)
        self.i = 0
        self.mv = MV()

        filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        print(filename)

        with open(filename, "r") as f:
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


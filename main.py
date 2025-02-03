#   Nome Brian Schu Motta
#   Atualizado 03/02/2025


import tkinter
from tkinter import *
from tkinter import ttk

co0 = "#444466" #preto
co1 = "#feffff" #branco
co2 = "#6f9fbd" #azul

fundo_dia = "#6cc4cc"
fundo_noite = "#484f60"
fundo_tarde = "#bfb86d"
fundo = fundo_dia

janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, column=1, ipadx=157)

# criando frames
frame_top = Frame(janela, width=320,  height=50, bg=fundo, pady=0, padx=0)
frame_top.grid(row=1, column=0)

frame_corpo = Frame(janela, width=320,  height=300, bg=fundo, pady=0, padx=0)
frame_corpo.grid(row=2, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')



# configurando frame top

e_local = Entry(frame_top, width=20, justify='left', font=("", 14), highlightthickness=1, relief='solid')
e_local.place(x=15, y=10)
b_ver = Button(frame_top, text='Ver Clima', bg=co1, fg=co2, font=("Ivy 9 bold"), relief='raised', overrelief=RIDGE)
b_ver.place(x=250, y=10)

# configurando frame corpo

l_cidade = Label(frame_corpo, text='Novo Hamburgo - Brasil / America', anchor='center', bg=fundo, fg=co1, font=("Arial 14"))
l_cidade.place(x=10, y=4)


l_data = Label(frame_corpo, text='27 01 2025 | 17:00 AM', anchor='center', bg=fundo, fg=co1, font=("Arial 10"))
l_data.place(x=10, y=54)


l_umidade = Label(frame_corpo, text='84', anchor='center', bg=fundo, fg=co1, font=("Arial 45"))
l_umidade.place(x=10, y=100)


l_umidade_simbol = Label(frame_corpo, text='%', anchor='center', bg=fundo, fg=co1, font=("Arial 10 bold"))
l_umidade_simbol.place(x=85, y=110)


l_umidade_nome = Label(frame_corpo, text='Umidade', anchor='center', bg=fundo, fg=co1, font=("Arial 8"))
l_umidade_nome.place(x=85, y=140)


l_pressao = Label(frame_corpo, text='Pressão: 1000', anchor='center', bg=fundo, fg=co1, font=("Arial 10"))
l_pressao.place(x=10, y=184)


l_pressao = Label(frame_corpo, text='Velocidade do vento: 1.03', anchor='center', bg=fundo, fg=co1, font=("Arial 10"))
l_pressao.place(x=10, y=184)


janela.mainloop() 
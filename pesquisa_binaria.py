# Bibliotecas
import tkinter as tk
from tkinter.font import Font
from random import choice

# GUI
janela = tk.Tk()
janela.title('Pesquisa Binária')
janela.geometry('270x150')

# Fonte números
fonte_numero = Font(family="Helvetica", size=20, weight="bold")
fonte_botao = Font(family="Helvetica", size=14, weight="bold")



label_numero_sortido = tk.Label(janela, text='16', font=fonte_numero)
label_numero_sortido.pack(pady=10)

botao_numero_maior = tk.Button(janela, text='Meu Número é Maior')
botao_numero_maior.pack(pady=3)

botao_numero_menor = tk.Button(janela, text='Meu Número é Menor')
botao_numero_menor.pack(pady=3)

botao_acertou_numero = tk.Button(janela, text='Acertou!')
botao_acertou_numero.pack(pady=3)

janela.mainloop()
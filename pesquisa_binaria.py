# Bibliotecas
import tkinter as tk
from tkinter.font import Font
from random import choice

# GUI
janela = tk.Tk()
janela.title('Pesquisa Binária')
janela.geometry('270x250')

label_numero_sortido = tk.Label(janela, text='')
label_numero_sortido.pack(pady=5)

botao_numero_maior = tk.Button()
botao_numero_menor = tk.Button()
botao_acertou_numero = tk.Button()


janela.mainloop()
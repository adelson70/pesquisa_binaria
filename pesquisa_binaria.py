# Bibliotecas
import tkinter as tk
from tkinter.font import Font
from random import choice

numeros = [n for n in range(0,100+1)]
tentativas = 0

def atualizar_label(label, info):
    label.config(text=info)

def pesquisa_binaria(maior=False, menor=False, acertou=False):
    global numeros
    global tentativas
    tentativas += 1

    if acertou:
        atualizar_label(label_numero_sortido, ':D')

    elif maior:# Se o número escolhido pelo usuario for maior que o sortido
        numero_inicial = numeros[(len(numeros)//2)]# Descobrir o numero do meio da lista por indice
        numero_final = numeros[-1]
        numeros = [n for n in range(numero_inicial, numero_final+1)]

        novo_palpite = numeros[(len(numeros)//2)]
        
        atualizar_label(label_numero_sortido, novo_palpite)

    elif menor:# Se o número escolhido pelo usuario for menor que o sortido
        numero_inicial = numeros[0]
        numero_final = numeros[(len(numeros)//2)]# Descobrir o numero do meio da lista por indice
        numeros = [n for n in range(numero_inicial, numero_final+1)]

        novo_palpite = numeros[(len(numeros)//2)]
        
        atualizar_label(label_numero_sortido, novo_palpite)

    # print(numeros, f'Tentativas: {tentativas}')

# # # # # GUI # # # # #
janela = tk.Tk()
janela.title('Pesquisa Binária')
janela.geometry('270x190')

# Fonte números
fonte_numero = Font(family="Helvetica", size=26, weight="bold")
fonte_botao = Font(family="Helvetica", size=12)

label_numero_sortido = tk.Label(janela, text='50', font=fonte_numero)
label_numero_sortido.pack(pady=10)

botao_numero_maior = tk.Button(janela, text='Meu Número é Maior', font=fonte_botao, command=lambda: pesquisa_binaria(maior=True))
botao_numero_maior.pack(pady=4)

botao_numero_menor = tk.Button(janela, text='Meu Número é Menor', font=fonte_botao, command=lambda:pesquisa_binaria(menor=True))
botao_numero_menor.pack(pady=4)

botao_acertou_numero = tk.Button(janela, text='Acertou!', font=fonte_botao, command=lambda:pesquisa_binaria(acertou=True))
botao_acertou_numero.pack(pady=4)

janela.mainloop()
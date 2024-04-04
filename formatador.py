import tkinter as tk
from tkinter import ttk
import pyperclip  # Para copiar para a área de transferência
import re  # Para validar o endereço MAC
import sys
import os

# Verifica se o script está sendo executado no formato de arquivo .exe
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)

# Função para formatar o endereço MAC
def formatar_mac(mac, formato='padrao'):
    mac_limpo = ''.join(c for c in mac if c.isalnum())
    tamanho = len(mac_limpo)

    while tamanho != 12:
        label_status_copia.config(text="Quantidade de caracteres inválida! Por favor informe um tamanho de MAC correto:", fg="red")
        return

    if formato == 'dois_pontos':
        mac_formatado = ':'.join(mac_limpo[i:i+2] for i in range(0, len(mac_limpo), 2))
    elif formato == 'tracos':
        mac_formatado = '-'.join(mac_limpo[i:i+2] for i in range(0, len(mac_limpo), 2))
    elif formato == 'satelite':
        mac_formatado = ':'.join(mac_limpo[i:i+2] for i in range(0, len(mac_limpo), 2))
    else:
        mac_formatado = mac_limpo

    if formato == 'satelite':
        return mac_formatado.lower()
    else:
        return mac_formatado.upper()

def formatar():
    # Obtendo o endereço MAC inserido pelo usuário
    mac_input = entry_mac.get().strip()

    # Verificando se o endereço MAC é válido
    if not re.match(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', mac_input):
        label_status_copia.config(text="Endereço MAC inválido", fg="red")
        return

    # Obtendo o formato escolhido pelo usuário
    formato_escolhido = combo_formato.get()

    # Formatando o endereço MAC usando a função do script
    mac_formatado = formatar_mac(mac_input, formato_escolhido)
    label_resultado.config(text=f"MAC formatado: {mac_formatado}", fg="black")

def copiar_para_area_de_transferencia():
    mac_formatado = label_resultado.cget("text").split(": ")[1]
    pyperclip.copy(mac_formatado)
    label_status_copia.config(text="Endereço MAC copiado para a área de transferência", fg="green")

# Criando a janela principal
root = tk.Tk()
root.title("Formatador de MAC")

# Criando os widgets
label_mac = tk.Label(root, text="Endereço MAC:")
label_mac.grid(row=0, column=0, padx=5, pady=5)

entry_mac = tk.Entry(root, width=30)
entry_mac.grid(row=0, column=1, padx=5, pady=5)

label_formato = tk.Label(root, text="Formato:")
label_formato.grid(row=1, column=0, padx=5, pady=5)

combo_formato = ttk.Combobox(root, values=["padrao", "dois_pontos", "tracos", "satelite"], state="readonly", width=27)
combo_formato.current(0)  # Definindo o formato padrão
combo_formato.grid(row=1, column=1, padx=5, pady=5)

botao_formatar = tk.Button(root, text="Formatar", command=formatar)
botao_formatar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

label_resultado = tk.Label(root, text="", font=("Helvetica", 12))
label_resultado.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

botao_copiar = tk.Button(root, text="Copiar para Área de Transferência", command=copiar_para_area_de_transferencia)
botao_copiar.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

label_status_copia = tk.Label(root, text="", fg="green")
label_status_copia.grid(row=5, column=0, columnspan=2)

# Iniciando o loop principal da interface gráfica
root.mainloop()

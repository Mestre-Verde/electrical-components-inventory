import tkinter as tk

INPUT = "tmp/input.tmp"
OUTPUT = "tmp/output.tmp"


# Funções I/O
def saveInputToFile():
    #escreve o texto a calcular no ficheiro de output 
    ...

def readOutputFromFile():
    #Python ← lê resultado de output.tmp
    #O executavel vai escrever em cima do texto anterior não o python
    ...

def sendCommandToExecutable():
   
    ...

def updateHistory():
    #- abre history.txt
#- lê tudo
#- mostra no Listbox
    ...

# Funções da interface    

def clicar(valor):
    display.insert(tk.END, valor)

def limpar():
    display.delete(0, tk.END)

def apagar_um():
    texto = display.get()
    if texto:
        display.delete(0, tk.END)
        display.insert(0, texto[:-1])

def toggle_extra():
    if frame_extra.winfo_ismapped():
        frame_extra.grid_remove()
    else:
        frame_extra.grid(row=0, column=0, rowspan=6, padx=10)

# --- Janela ---
janela = tk.Tk()
janela.title("Calculadora GUI")

# --- Botões adicionais (ESQUERDA) ---
frame_extra = tk.Frame(janela)

botoesAdicionais = [
    ('(', lambda: clicar("(")),
    (')', lambda: clicar(")")),
    ('^', lambda: clicar("^")),
    ('n!', lambda: clicar("!")),
]

for i, (texto, comando) in enumerate(botoesAdicionais):
    tk.Button(frame_extra, text=texto, width=5, command=comando)\
        .grid(row=i, column=0, pady=2)

frame_extra.grid_remove()

# --- Entrada (CENTRO) ---
display = tk.Entry(janela, width=25, borderwidth=5)
display.grid(row=0, column=1, columnspan=4, padx=10, pady=10)

# --- Botões principais ---
botoes = [
    ('7',1,1), ('8',1,2), ('9',1,3), ('/',1,4),
    ('4',2,1), ('5',2,2), ('6',2,3), ('*',2,4),
    ('1',3,1), ('2',3,2), ('3',3,3), ('-',3,4),
    ('0',4,1), ('.',4,2), ('+',4,4)
]

for (texto, linha, coluna) in botoes:
    tk.Button(janela, text=texto, width=5,
              command=lambda t=texto: clicar(t)
              ).grid(row=linha, column=coluna)

tk.Button(janela, text="=", width=5, command=function)\
    .grid(row=4, column=3)

tk.Button(janela, text="C", width=5, command=limpar)\
    .grid(row=5, column=1)

tk.Button(janela, text="DEL", width=5, command=apagar_um)\
    .grid(row=5, column=3)

tk.Button(janela, text="Mais", width=5, command=toggle_extra)\
    .grid(row=5, column=2)

# --- Histórico (DIREITA) ---
historico = tk.Listbox(janela, width=20, height=15)
historico.grid(row=0, column=5, rowspan=6, padx=10, pady=10)

# --- Loop ---
janela.mainloop()
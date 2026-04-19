import tkinter as tk

# caminhos 
INPUT = "tmp/input.tmp"
OUTPUT = "tmp/output.tmp"
HISTORY = "data/history.txt"

# ---------------- I/O ----------------
def saveInputToFile():
    with open(INPUT, "w") as f:
        f.write(display.get())

#O executavel vai escrever em cima do texto anterior não o python
def readOutputFromFile():
    try:
        with open(OUTPUT, "r") as f:
            return f.read()
    except:
        return "Erro"

def sendCommandToExecutable():
    # aqui vais ligar ao C depois
    pass

# - abre history.txt
# - lê tudo 
# - mostra no Listbox
def updateHistory():
    try:
        with open(HISTORY, "r") as f:
            historico.delete(0, tk.END)
            for line in f:
                historico.insert(tk.END, line.strip())
    except:
        pass

# ---------------- UI logic ----------------
def clicar(valor):
    display.insert(tk.END, valor)

def limpar():
    display.delete(0, tk.END)

def apagar_um():
    texto = display.get()
    if texto:
        display.delete(0, tk.END)
        display.insert(0, texto[:-1])

def calcular():
    saveInputToFile()
    sendCommandToExecutable()
    updateHistory()

# ---------------- páginas ----------------
def mostrar_normal():
    frame_fracoes.grid_remove()
    frame_normal.grid()

def mostrar_fracoes():
    frame_normal.grid_remove()
    frame_fracoes.grid()

# ---------------- janela ----------------
janela = tk.Tk()
janela.title("Calculadora Básica")

#  tornar janela expansível
janela.rowconfigure(1, weight=1)
janela.columnconfigure(0, weight=1)

# ---------------- topo (tabs) ----------------
top = tk.Frame(janela)
top.grid(row=0, column=0, columnspan=6)

tk.Button(top, text="Normal", command=mostrar_normal).grid(row=0, column=0)
tk.Button(top, text="Frações", command=mostrar_fracoes).grid(row=0, column=1)

# ---------------- FRAME NORMAL ----------------
frame_normal = tk.Frame(janela)
frame_normal.grid(row=1, column=0, sticky="nsew")

# 🔥 expandir grid interno
for i in range(7):
    frame_normal.columnconfigure(i, weight=1)
for i in range(6):
    frame_normal.rowconfigure(i, weight=1)

display = tk.Entry(frame_normal)
display.grid(row=0, column=1, columnspan=5, sticky="nsew")

botoes = [
    ('7',1,1), ('8',1,2), ('9',1,3), ('/',1,4), ('(',1,5),
    ('4',2,1), ('5',2,2), ('6',2,3), ('*',2,4), (')',2,5),
    ('1',3,1), ('2',3,2), ('3',3,3), ('-',3,4), ('!',3,5),
    ('0',4,1), ('.',4,2),            ('+',4,4)
]

for (t,l,c) in botoes:
    tk.Button(frame_normal, text=t, command=lambda x=t: clicar(x))\
        .grid(row=l, column=c, padx=2, pady=2, sticky="nsew")

tk.Button(frame_normal, text="=", command=calcular)\
    .grid(row=4, column=3, sticky="nsew")

tk.Button(frame_normal, text="C", command=limpar)\
    .grid(row=5, column=1, sticky="nsew")

tk.Button(frame_normal, text="DEL", command=apagar_um)\
    .grid(row=5, column=3, sticky="nsew")

historico = tk.Listbox(frame_normal)
historico.grid(row=0, column=6, rowspan=6, sticky="nsew")

# ---------------- FRAME FRAÇÕES ----------------
frame_fracoes = tk.Frame(janela)


def criar_fracao(parent):
    f = tk.Frame(parent)

    n = tk.Entry(f, width=5, justify="center")
    n.grid(row=0, column=0)

    tk.Frame(f, height=2, bg="black", width=40).grid(row=1, column=0)

    d = tk.Entry(f, width=5, justify="center")
    d.grid(row=2, column=0)

    return f, n, d

f1, n1, d1 = criar_fracao(frame_fracoes)
f1.grid(row=0, column=0, padx=10)

op = tk.StringVar(value="+")
tk.OptionMenu(frame_fracoes, op, "+", "-", "*", "/").grid(row=0, column=1)

f2, n2, d2 = criar_fracao(frame_fracoes)
f2.grid(row=0, column=2, padx=10)

tk.Label(frame_fracoes, text="=").grid(row=0, column=3)

f3, nr, dr = criar_fracao(frame_fracoes)
f3.grid(row=0, column=4, padx=10)

def calcular_fracao():
    expr = f"{n1.get()}/{d1.get()} {op.get()} {n2.get()}/{d2.get()}"
    print(expr)  # ligar ao C depois
    

tk.Button(frame_fracoes, text="=", command=calcular_fracao)\
    .grid(row=1, column=2)

# ---------------- start ----------------
frame_normal.grid()
janela.mainloop()
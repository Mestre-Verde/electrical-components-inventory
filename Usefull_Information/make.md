# 🛠️ Make e Makefile — Guia Rápido

## 📌 O que é o `make`?

O `make` é uma ferramenta usada para **automatizar tarefas**, principalmente a **compilação de programas**.

Ele lê um ficheiro chamado **Makefile**, que contém regras sobre como construir um projeto.


## 💡 Para que serve?

O `make` é usado para:

- 🧱 Compilar programas automaticamente
- 🔁 Evitar recompilar tudo desnecessariamente
- 📦 Gerir projetos com vários ficheiros
- ⚙️ Automatizar tarefas (build, clean, test, run)



## 🧠 Ideia principal

O `make` funciona com base em **dependências**:

> Só executa uma tarefa se algo tiver mudado.



## 📄 Estrutura básica de um Makefile

```makefile
alvo: dependências
	comando
````

⚠️ IMPORTANTE:
O comando tem de começar com um **TAB**, não espaços.



## 🔧 Exemplo simples

```makefile
CC = gcc

all: programa

programa: main.c
	$(CC) main.c -o programa
```

* `all` é o alvo principal (executável)
* `programa` depende de `main.c`
* o comando compila o código



##  Como usar

Vá ao terminal e vá para o diretório do projeto.

### Compilar projeto:


```bash
make
```

### Limpar ficheiros gerados:

```bash
make clean
```



## 🧩 Exemplo mais real

```makefile
CC = cc
CFLAGS = -Wall -Wextra

SRC = main.c utils.c
OBJ = main.o utils.o

programa: $(OBJ)
	$(CC) $(OBJ) -o programa

clean:
	rm -f *.o programa
```



## 📁 Conceitos importantes

### 🔹 Variáveis

```makefile
CC = cc
```

Usadas para evitar repetição.



### 🔹 Regras

```makefile
target: dependencies
	command
```



### 🔹 Dependências

O `make` só recompila o que mudou.



## 🧠 Vantagens

* ⚡ Mais rápido que compilar manualmente
* 🧼 Código organizado
* 🔁 Automático e inteligente
* 📦 Ideal para projetos grandes



## ⚠️ Erros comuns

* Usar espaços em vez de TAB
* Não declarar dependências corretamente
* Não perceber que o `make` usa timestamps



## 📌 Resumo

O `make` é uma ferramenta que:

> automatiza a construção de projetos com base em regras e dependências.



## 🔥 Em poucas palavras

👉 Escreves regras
👉 O `make` decide o que precisa ser executado
👉 Ele compila só o necessário

```



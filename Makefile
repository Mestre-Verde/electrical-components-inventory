# =========================================================
# Este Makefile automatiza:
# - Compilação dos ficheiros .c
# - Organização de ficheiros .o (build/)
# - Geração do executável (bin/)
# - Limpeza de ficheiros compilados
#
# Comandos principais:
#   make        -> compila o projeto
#   make clean  -> remove ficheiros gerados
#
# Estrutura:
#   src/   -> código fonte (.c)
#   build/ -> ficheiros objeto (.o)
#   bin/   -> executável final
# =========================================================

# compilador
CC = cc

# Variaveis para guardar os caminhos
OBJ_DIR = build/
BIN_DIR = bin/

# flags do CPU para o compilador usar.
CFLAGS = 

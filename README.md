# 1. Base de Dados para Componentes Eletrónicos
- Compativel para OS GNU/Linux


## 1.1. Conceito Geral

- Gui simples em Pyhton
- chamada de softwares por bash

* **Um componente = uma pasta**
* Tudo o que pertence ao componente fica dentro dessa pasta
* Os dados são legíveis e editáveis sem qualquer software especial

Esta abordagem permite:

* backups simples
* edição manual direta
* independência total de ferramentas externas
* longevidade do sistema

---

## 1.2. Estrutura Global da Base de Dados

Para melhorar a organização e a velocidade de navegação, os componentes são agrupados por **tipo**.

Exemplos de tipos:

* Resistencias
* Condensadores
* Dispositivos_de_medicao

### Exemplo de estrutura global

```text
data/
├── resistencias/
│   ├── 0001/
│   ├── 0003/
│   └── ...
├── condensadores/
│   ├── 0002/
│   └── ...
```

Cada pasta dentro de um tipo corresponde a **um componente individual**.

---

## 1.3. Estrutura da Pasta do Componente

Cada componente possui a sua própria pasta, contendo todos os ficheiros associados.

### Exemplo

```text
components_db/resistencias/0001/
├── component.json
├── images/
├── datasheets/
├── files/
└── notes.txt
```

### Conteúdo das pastas

| Ficheiro / Pasta | Função                                   |
| ---------------- | ---------------------------------------- |
| `component.json` | Dados estruturados do componente         |
| `images/`        | Imagens (fotografias, pinout, diagramas) |
| `datasheets/`    | Datasheets e documentação técnica        |
| `files/`         | Outros ficheiros relevantes              |
| `notes.txt`      | Descrição longa e notas pessoais         |

---

## 1.4. Identificação do Componente

* O nome da pasta do componente corresponde a um **ID numérico**
* O ID é atribuído no momento da criação
* O sistema **reutiliza IDs livres** (gaps), em vez de apenas incrementar

Isto mantém a base de dados compacta e organizada ao longo do tempo.

---

## 1.5. Ficheiro `component.yaml`

O ficheiro `component.yaml` contém os **dados estruturados** usados pelo programa.

### Informação armazenada

* Identificação:

  * ID
  * Nome
  * Categoria / tipo
  * Encapsulamento
  * Fabricante
* Quantidade em stock
* Caminho para a descrição (`notes.txt`)
* Caminhos para imagens, datasheets e outros ficheiros

👉 Todos os caminhos são **relativos à pasta do componente**, garantindo simplicidade e portabilidade interna.

---

## 1.6. Pasta `images/`

Contém imagens associadas ao componente, por exemplo:

* fotografia do componente
* pinout
* diagramas simples

A TUI abre diretamente esta pasta no **Gwenview**.

---

## 1.7. Pasta `datasheets/`

Contém datasheets e documentação técnica em PDF ou formatos similares.

Como pode conter vários ficheiros:

1. A TUI lista os ficheiros disponíveis
2. O utilizador escolhe um
3. O ficheiro selecionado é aberto no **Okular** como processo paralelo

---


---

## 1.9. Ficheiro `notes.txt`

Ficheiro de texto livre que contém:

* descrição detalhada do componente
* observações pessoais
* notas práticas de utilização

Este ficheiro permite descrições longas sem poluir os dados estruturados.


---

## Função do programa em c

## Função das scripst em bash
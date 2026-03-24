# 🧩 Sudoku em Python (Modo Interativo e Batch)

## 📌 Descrição

Este projeto consiste em uma implementação completa de um jogo de Sudoku em Python, desenvolvido como parte da disciplina de Fundamentos de Programação.

O sistema permite a execução em dois modos distintos:

* **Modo Interativo**: o usuário joga diretamente pelo terminal
* **Modo Batch**: o programa processa automaticamente um conjunto de jogadas a partir de arquivos

Além disso, o projeto implementa validações rigorosas das regras do Sudoku, tratamento de erros de entrada e um sistema de dicas para auxiliar o jogador.

---

## 🚀 Funcionalidades

* ✔️ Leitura de pistas a partir de arquivo
* ✔️ Validação de regras do Sudoku (linhas, colunas e submatrizes 3x3)
* ✔️ Interface no terminal com visualização da grade
* ✔️ Sistema de dicas (`?`) com valores possíveis
* ✔️ Remoção de valores (`!`)
* ✔️ Verificação de jogadas inválidas
* ✔️ Execução em modo automático (batch)
* ✔️ Tratamento de erros de formatação e entradas inválidas

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* Manipulação de arquivos
* Estruturas de dados (listas/matrizes)
* Programação modular

---

## ⚙️ Como Executar

### 🔹 Pré-requisitos

* Python 3 instalado

---

### 🔹 Modo Interativo

Execute o programa com um arquivo de pistas:

```bash
python sudoku.py pistas.txt
```

---

### 🔹 Modo Batch

Execute o programa com dois arquivos:

```bash
python sudoku.py pistas.txt jogadas.txt
```

---

## 📂 Estrutura do Projeto

```
.
├── sudoku.py        # Arquivo principal
├── functions.py     # Funções auxiliares (lógica do jogo)
├── pistas.txt       # Arquivo com pistas iniciais
├── jogadas.txt      # (Opcional) jogadas para modo batch
```

---

## 📥 Formato das Entradas

### 📌 Pistas

Formato:

```
<Coluna>,<Linha>: <Valor>
```

Exemplo:

```
C,3: 8
D,1: 6
H,9: 7
```

---

### 🎮 Comandos no modo interativo

* Inserir valor:

```
A,1: 5
```

* Remover valor:

```
!A,1
```

* Ver possibilidades:

```
?A,1
```

---

## 📖 Conceitos Aplicados

* Manipulação de strings e parsing de entrada
* Validação de regras lógicas
* Matrizes 2D
* Modularização de código
* Interação via terminal
* Tratamento de erros

---

## ⚠️ Tratamento de Erros

O sistema detecta automaticamente:

* Entradas mal formatadas
* Valores fora do intervalo permitido (1–9)
* Coordenadas inválidas
* Violações das regras do Sudoku
* Número inválido de pistas

---

## 👨‍💻 Autores

* Caio Emanuel
* Danny Secundino
* Guilherme Martins

Graduandos em Ciência da Computação - Universidade Federal do Ceará (UFC)

---

## 📚 Contexto Acadêmico

Projeto desenvolvido para a disciplina de **Fundamentos de Programação**, com foco em:

* Lógica de programação
* Boas práticas de desenvolvimento

---

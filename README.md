# # 🧠 Tabuleiro caminho - Caminho Inteligente - Busca com Backtracking, Branch and Bound e Heurística.

Projeto desenvolvido como parte da atividade do curso **Inteligência Artificial Aplicada** pelo programa **Vai na Web**.

Este algoritmo encontra o **melhor caminho possível** entre dois pontos em um tabuleiro NxN, respeitando obstáculos e aplicando técnicas clássicas de IA como:

- ✅ Backtracking
- ✅ Branch and Bound (poda de caminhos piores)
- ✅ Heurística baseada na distância de Manhattan

---

## 📌 Sobre o Projeto

O objetivo deste desafio é implementar uma **busca inteligente em um tabuleiro**, considerando obstáculos e encontrando o menor caminho entre uma origem e um destino.

- O algoritmo evita caminhos inúteis (poda).
- Ele usa uma **heurística admissível** para guiar a busca.
- Marca visualmente o trajeto ideal encontrado com `*`.

---

## ⚙️ Tecnologias Utilizadas

- Python
- Programação Recursiva
- Estrutura de dados com matrizes
- Heurística (distância de Manhattan)

---

## 🧠 Conceitos Envolvidos

- **Backtracking:** Tenta caminhos recursivamente e volta se for um beco sem saída.
- **Branch and Bound:** Corta caminhos que já estão piores do que a melhor solução encontrada.
- **Heurística:** Distância de Manhattan é usada como estimativa para acelerar a busca.
- **Busca Ótima:** Sempre encontra o menor caminho possível (ou nenhum, se for impossível).

---

## ✏️ Personalize seu Tabuleiro

Você pode alterar o tabuleiro diretamente na variável `tabuleiro` no início do script `main.py`.

### Exemplo:
```python
tabuleiro = [
    ['X', 'X', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', 'X', ' ', ' '],
    [' ', ' ', ' ', ' ']
]
```
---

## 🔤 Significado dos símbolos

| Símbolo | Significado                                  |
|---------|----------------------------------------------|
| `'X'`   | Obstáculo (o caminho está bloqueado)         |
| `' '`   | Espaço livre (o algoritmo pode passar)       |
| `'*'`   | Caminho escolhido como ideal (marcado pelo algoritmo) |

---

## 🧭 Origem e Destino

Você também pode definir os pontos de início e fim do caminho alterando as variáveis abaixo no código:

```python
linha_inicial, coluna_inicial = 3, 0
linha_destino, coluna_destino = 0, 3
```
---

## 📜 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo! 📄

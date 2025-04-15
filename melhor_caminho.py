import copy

# Função para imprimir o tabuleiro formatado
def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('| ' + ' | '.join(linha) + ' |')
    print()

# Verifica se a posição está dentro dos limites e é um espaço livre
def movimento_valido(tabuleiro, linha, coluna):
    return (0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0]) and tabuleiro[linha][coluna] == ' ')

# Verifica se a posição é o destino desejado
def chegou_destino(linha, coluna, linha_destino, coluna_destino):
    return (linha == linha_destino and coluna == coluna_destino)

# Brincando com heuristica usando distância de Manhattan (distância em blocos)
def heuristica(linha, coluna, linha_destino, coluna_destino):
    return (abs(linha - linha_destino) + abs(coluna - coluna_destino))

# Função principal com Branch and Bound + heurística para encontrar o melhor caminho
def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade, caminho_atual, melhor_profundidade, linha_destino, coluna_destino):
    if chegou_destino(linha_atual, coluna_atual, linha_destino, coluna_destino):
        return (profundidade, copy.deepcopy(caminho_atual))

    # Poda com heurística: se a estimativa total for pior do que o melhor já encontrado, corta o ramo
    estimativa_total = profundidade + heuristica(linha_atual, coluna_atual, linha_destino, coluna_destino)
    if estimativa_total >= melhor_profundidade[0]:
        return (float('inf'), [])

    direcoes = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # direita, esquerda, cima, baixo (respectivamente)
    melhor_caminho = []
    melhor_local_profundidade = float('inf')

    for direcao in direcoes:
        nova_linha = linha_atual + direcao[0]
        nova_coluna = coluna_atual + direcao[1]

        if movimento_valido(tabuleiro, nova_linha, nova_coluna):
            tabuleiro[nova_linha][nova_coluna] = '*'
            caminho_atual.append((nova_linha, nova_coluna))

            profundidade_encontrada, caminho_encontrado = proximo_movimento(
                tabuleiro, nova_linha, nova_coluna, profundidade + 1, caminho_atual, melhor_profundidade, linha_destino, coluna_destino
            )

            if profundidade_encontrada < melhor_local_profundidade:
                melhor_local_profundidade = profundidade_encontrada
                melhor_caminho = caminho_encontrado
                melhor_profundidade[0] = profundidade_encontrada  # Atualiza o melhor caminho global

            caminho_atual.pop()
            tabuleiro[nova_linha][nova_coluna] = ' '

    return (melhor_local_profundidade, melhor_caminho)

# Função principal para execução

def main():
    tabuleiro = [
        [' ', ' ', ' ', ' ', 'X'],
        ['X', 'X', ' ', 'X', ' '],
        [' ', ' ', ' ', 'X', ' '],
        ['*', 'X', ' ', ' ', ' '],
        ['X', ' ', 'X', 'X', ' ']
    ]

    linha_inicial, coluna_inicial = 3, 0
    linha_destino, coluna_destino = 0, 3

    mostrar_tabuleiro(tabuleiro)

    melhor_profundidade = [float('inf')]
    caminho_inicial = [(linha_inicial, coluna_inicial)]

    profundidade, melhor_caminho = proximo_movimento(
        tabuleiro, linha_inicial, coluna_inicial, 0, caminho_inicial, melhor_profundidade, linha_destino, coluna_destino
    )

    if melhor_caminho:
        # Marca o melhor caminho no tabuleiro
        for linha, coluna in melhor_caminho:
            if (linha, coluna) != (linha_inicial, coluna_inicial):
                tabuleiro[linha][coluna] = '*'
        print("\nMelhor caminho encontrado:")
        mostrar_tabuleiro(tabuleiro)
    else:
        print("\nCaminho impossível.")

if __name__ == "__main__":
    main()
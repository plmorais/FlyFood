LISTA_PERMUTADA = []


def permute(lista, k, tamanho_lista):
    # Verifica se a permutação está completa
    if k == tamanho_lista:
        LISTA_PERMUTADA.append(tuple(lista))
        # Adiciona a permutação atual à lista de permutações
    else:
        # Para cada elemento a partir do índice k até o final da lista
        for i in range(k, tamanho_lista):
            # Troca os elementos para explorar diferentes permutações
            lista[k], lista[i] = lista[i], lista[k]
            # Chama recursivamente a função para permutações restantes
            permute(lista, k + 1, tamanho_lista)
            lista[k], lista[i] = lista[i], lista[k]  # Desfaz a troca
    return LISTA_PERMUTADA


# função patra armazenar as distâncias totais percorridas em cada permutação
def calcular_distancias(lista_coordenadas, ponto_R):
    distancias = []
    coordenadas = permute(lista_coordenadas, 0, len(lista_coordenadas))
    for i, pontos in enumerate(coordenadas):
        pontos = list(pontos)
        pontos.append(ponto_R)
        posicao_atual = ponto_R
        distancia_total = 0
        for ponto in pontos:
            x = posicao_atual[0] - ponto[0]
            y = posicao_atual[1] - ponto[1]
            dist_percorrida = abs(x) + abs(y)
            distancia_total += dist_percorrida
            posicao_atual = ponto
        distancias.append(distancia_total)
    return distancias

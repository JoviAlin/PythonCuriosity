import time
import random

#func. linear
def busca_linear(lista, alvo):
    print(f'\n--- BUSCA LINEAR (Procurando {alvo}) ---')
    comparacoes = 0
    inicio = time.time()

    for i in range(len(lista)):
        comparacoes += 1
        if lista[i] == alvo:
            fim = time.time()
            print(f'Encontrado na posição {i}! Com {comparacoes} comparações | Tempo: {(fim-inicio)*1000:.4f} ms')
            return i

    fim = time.time()
    print(f'Não encontrado. {comparacoes} comparações realizadas | Tempo: {(fim-inicio)*1000:.4f} ms')
    return -1

#func. binária
def busca_binaria(lista, alvo):
    print(f'\n--- BUSCA BINÁRIA (Procurando {alvo}) ---')
    comparacoes = 0
    inicio = time.time()

    low_idx = 0
    high_idx = len(lista) - 1

    while low_idx <= high_idx:
        comparacoes += 1
        mid_idx = (low_idx + high_idx) // 2

        if lista[mid_idx] == alvo:
            fim = time.time()
            print(f'Encontrado na posição {mid_idx}! Com {comparacoes} comparações | Tempo: {(fim-inicio)*1000:.4f} ms\n')
            return mid_idx
        elif lista[mid_idx] < alvo:
            low_idx = mid_idx + 1
        else:
            high_idx = mid_idx - 1

    tempo_fim = time.time()
    print(f'Não encontrado. {comparacoes} comparações realizadas | Tempo: {(tempo_fim-inicio)*1000:.4f} ms')
    return -1

#Teste com 1bi de valores
size = 10000000
lista = list(range(size))
alvo = random.randint(0, size - 1)
print(f'\n| Gerando lista ordenada de {size} elementos... |\n: alvo gerado aleatóriamente: {alvo}')

busca_linear(lista, alvo)
busca_binaria(lista, alvo)

#Respostas
print(f'\n| PERGUNTAS E RESPOSTAS |')
#1
print(f'\n1. Qual a diferença entre os dois algoritmos em termos de quantidade de passos no pior caso?')
print(f'     R: Em uma amostra de 1 bilhão de elementos, no pior caso a pesquisa linear percorrerá toda a lista, resultando em 1 bilhão de comparações.\n        Já a busca binária necessita somente de 23 comparações para o pior caso.')
print(f'     TLDR: Lista de 1b. de elementos | linear: 1b. comparações | binária: 23 comparações')
#2
print(f'\n2. Por que a busca binária exige que a lista esteja ordenada?')
print(f'     R: A busca binária funciona dividindo a lista em metades buscando o valor do meio, assim comparando com o valor alvo e descartando os valores inferiores\n        ou superiores de acordo com o a comparação do meio para o alvo. Caso a lista não esteja ordenada, não é possível descartar os demais valores,\n        pois se não há garantia de que os valores estão em ordem, há a possibilidade de que o valor alvo será descartado também.')
#3
print(f'\n3. Escreva em suas palavras a diferença entre O(n) e O(log n).')
print(f'     R: A notação Big O é usada para descrever a complexidade de um algoritmo em passos de execução considerando o pior caso.\n        O(n) representa a execução da busca linear, onde o número de passos é proporcional ao número de elementos (n).\n        Já O(log n) representa a execução da busca binária, onde o número de passos é proporcional ao logaritmo do número de elementos.\n        Reduzindo assim o tempo e aumentando a eficiência do algoritmo.')
print(f'     TLDR: O(n) = linear, passos = n (elementos) | O(log n) = binária, passos = log(elementos)')
print()
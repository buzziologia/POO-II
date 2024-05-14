'''Desafio: Análise de Frequência de Palavras

Você deve escrever um programa em Python que recebe um texto como entrada e realiza as seguintes tarefas:

Conte o número total de palavras no texto.
Identifique as palavras únicas no texto.
Crie um dicionário onde as chaves são as palavras únicas e os valores são as frequências de cada palavra no texto.
Identifique e imprima a palavra mais frequente no texto.
Identifique e imprima a palavra menos frequente no texto.
Identifique e imprima as cinco palavras mais frequentes no texto, juntamente com suas frequências.
Isso vai te fazer trabalhar com strings para manipular o texto, listas e conjuntos para lidar com as palavras únicas, dicionários para contar as frequências e tuplas para ordenar e selecionar as palavras mais e menos frequentes. Divirta-se!'''


def freq_palavras(palavras, todas_palavras):
    frequencia = {}
    for p in todas_palavras:
        freq = 0
        for i in range(len(palavras)):
            if palavras[i] == p:
                freq += 1
        frequencia[p] = freq
    print(frequencia)
    return frequencia


def frequencia(frequencia):
    lista = []
    for n in frequencia.values():
        if n not in lista:
            lista.append(n)
    minima = min(lista)
    maxima = max(lista)
    
    min_frequencia []
    max_frequencia = []
    
    for p in frequencia:
        if frequencia[p].values == minima:
            min_frequencia.append(p)
        if frequencia[p].values == maxima:
            max_frequencia.append(p)
            
    print(f'Estas são as palavras que aparecem com a menor frequencia = {minima}')
    print(', '.join(min_frequencia))
    print()
    print(f'Estas são as palavras que aparecem com a maior frequencia = {maxima}')
    print(', '.join(max_frequencia)
    print()
        
        
        
texto = input()
palavras = texto.split()
todas_palavras = set(palavras)

print(freq_palavras(palavras, todas_palavras))



        


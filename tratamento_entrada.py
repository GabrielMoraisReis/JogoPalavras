import collections


def trata_entrada(letras_rodada, dicionario_pontuacao):
    letras_nao_usadas = list()
    for char in letras_rodada:      
        #Remove os caracteres inválidos(não presentes nas letras pontuadas) da lista de letras utilizáveis da rodada, 
        #o que irá poupar tempo no calculo da palavra possível de maior pontuação.
        if char not in dicionario_pontuacao.keys():
            letras_rodada = letras_rodada.replace(char, "")
            letras_nao_usadas.append(char)      #Caracteres inválidos são salvos para serem exibidos no final.
    num_letras_validas = len(letras_rodada)     #Esse valor será utilizado posteriormente para o calculo da palavra possível de maior pontuação
    letras_rodada = dict(collections.Counter(letras_rodada))        #Quantas vezes cada letra válida aparece na entrada
    return letras_rodada, letras_nao_usadas, num_letras_validas 
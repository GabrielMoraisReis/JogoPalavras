def calcula_pontuacao_palavra(palavra, dicionario_pontuacao):
    pontuacao = 0
    for letra in palavra:
        pontuacao += dicionario_pontuacao[letra]
    return pontuacao

def gera_banco_pontuado(banco_palavras, dicionario_pontuacao):
    pontuacao = 0
    banco_palavras_pontuado = dict()
    for palavra in banco_palavras:
        pontuacao = calcula_pontuacao_palavra(palavra, dicionario_pontuacao)
        banco_palavras_pontuado[palavra] = pontuacao
    return banco_palavras_pontuado

def calcula_pontuacao_maxima(banco_palavras):
    pontuacao_maxima = 0
    pontuacao_palavra = calcula_pontuacao_palavra()
    palavras_maior_valor = list()
    if pontuacao_palavra > pontuacao_maxima:
        pontuacao_maxima = pontuacao_palavra
        palavras_maior_valor.clear()
        #palavras_maior_valor.append(word)
    elif pontuacao_palavra == pontuacao_maxima:
        palavras_maior_valor.append(word)


def desempate(palavras_maior_valor):
    index = 0
    tam_menor_word = 0
    for word in palavras_maior_valor:
        if len(word) < tam_menor_word:
            tam_menor_word = len(word)
            best_word = word


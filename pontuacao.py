def calcula_pontuacao_maxima(banco_palavras, letras_validas, num_letras_validas):
    pontuacao_maxima = 0
    break_flag = False
    palavras_maior_valor = list()
    for palavra in banco_palavras:
        count = 0
        break_flag = False
        if ((len(palavra) <= num_letras_validas) and (banco_palavras[palavra].pontuacao >= pontuacao_maxima)) :     
            #Descarta palavras que não terão número de letras suficiente para serem formadas e palavras de pontuação inferior
            # a pontuação da palavra de maior valor atual.
            for char in banco_palavras[palavra].contagem_letras:
                if ((char not in letras_validas) or (char in letras_validas 
                and letras_validas[char] < banco_palavras[palavra].contagem_letras[char])):      
                    #Descarta palavras que não podem ser formadas pela falta de letras na rodada (seja pela letra ter sido inserida
                    # ou por inse quantidade insuficiente da letra).
                    break_flag = True
                    break
            if not break_flag:
                if palavras_maior_valor and banco_palavras[palavras_maior_valor[0]].pontuacao < banco_palavras[palavra].pontuacao:
                    palavras_maior_valor.clear()
                    palavras_maior_valor.append(palavra)
                    pontuacao_maxima = banco_palavras[palavras_maior_valor[0]].pontuacao
                    #reinicia a lista de palavras que fazem o maior número de pontos
                else:
                    palavras_maior_valor.append(palavra)
                    pontuacao_maxima = banco_palavras[palavras_maior_valor[0]].pontuacao
    melhor_palavra = ''
    if len(palavras_maior_valor) > 1:
        melhor_palavra = desempate(palavras_maior_valor)
    elif len(palavras_maior_valor) == 1:
        melhor_palavra = palavras_maior_valor[0]                    
    return melhor_palavra

def desempate(palavras_maior_valor):
    index = 0
    tam_menor_word = len(palavras_maior_valor[0])
    palavras_menor_len = list()
    melhor_palavra = ''
    for word in palavras_maior_valor:       #desempate por tamanho de palavra
        if len(word) < tam_menor_word:
            tam_menor_word = len(word)
            palavras_menor_len.clear()
            palavras_menor_len.append(word)
        elif len(word) == tam_menor_word:
            palavras_menor_len.append(word)
    if len(palavras_menor_len) > 1:     #desempate por ordem alfabética
        palavras_menor_len.sort()
    return palavras_menor_len[0]
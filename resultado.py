import collections

def imprime_resultado(melhor_palavra, pontuacao, letras_validas, letras_nao_usadas):
    
    print(f"\n{str.upper(melhor_palavra)}, palavra de {pontuacao} pontos.")

    count_letras_best_word = dict(collections.Counter(melhor_palavra))
    for char in letras_validas:
        if char in count_letras_best_word:
            letras_validas[char] = letras_validas[char] - count_letras_best_word[char]
            if letras_validas[char] > 0:
                for i in range(letras_validas[char]):
                    letras_nao_usadas.append(char)
        else:
            for i in range(letras_validas[char]):
                letras_nao_usadas.append(char)
    if letras_nao_usadas:
        print("Sobraram:", ", ".join([x.upper() for x in letras_nao_usadas]) + ".")
    print("\n---------------------------------------------------------------------------------\n")
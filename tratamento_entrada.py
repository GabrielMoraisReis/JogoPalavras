def freq_letra(letras_rodada, dicionario_pontuacao):
    letras_nao_usadas = list()
    for char in letras_rodada: #remove os caracteres inválidos(não presentes no dicionario) da lista de letras da rodada, o que irá poupar tempo na iteração seguinte
        if char not in dicionario_pontuacao.keys():
            letras_rodada = letras_rodada.replace(char, "")
            letras_nao_usadas.append(char) #caracteres não usados precisam são salvos para serem exibidos nos final
    return letras_rodada, letras_nao_usadas 


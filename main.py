import string
import tratamento_entrada
import pontuacao
import modificacao_banco_palavras
import resultado


dicionario_pontuacao = {"a" : 1, "b" : 3, "c" : 3, "d" : 2, "e" : 1, "f" : 5, "g" : 2, "h" : 5, "i" : 1, "j" : 8, "l" : 1,
"m" : 3, "n" : 1, "o" : 1, "p" : 3, "q" : 13, "r" : 1, "s" : 1, "t" : 1, "u" : 1, "v" : 5, "x" : 8, "z" : 13} 
banco_palavras = ['abacaxi', 'manada', 'mandar', 'porta', 'mesa', 'dado', 'mangas', 'ja', 'coisas', 'radiografia', 
'matematica', 'drogas', 'predios', 'implementacao', 'computador', 'balao', 'xicara', 'tedio', 'faixa', 'livro', 
'deixar', 'superior', 'profissao', 'reuniao', 'predios', 'montanha', 'botanica', 'banheiro', 'caixas', 'xingamento', 
'infestacao', 'cupim', 'premiada', 'empanada', 'ratos', 'ruido', 'antecedente', 'empresa', 'emissario', 'folga', 'fratura', 
'goiaba', 'gratuito', 'hidrico', 'homem', 'jantar', 'jogos', 'montagem', 'manual', 'nuvem', 'neve', 'operacao', 'ontem', 
'pato', 'pe', 'viagem', 'queijo', 'quarto', 'quintal', 'solto', 'rota', 'selva', 'tatuagem', 'tigre', 'uva', 'ultimo', 
'vituperio', 'voltagem', 'zangado', 'zombaria', 'dor', 'folga', 'uva']
banco_palavras = modificacao_banco_palavras.tratamento_banco_palavras(banco_palavras, dicionario_pontuacao)
#O banco passa a associar as palavra com a pontuação delas e a quantidade de cada letra única que as formam.

print("---------------------------------------------------------------------------------")
print("\nPara finalizar o programa digite 'SAIR' como as letras disponíveis na jogada.\n")
print("---------------------------------------------------------------------------------\n")
letras_rodada = input("Digite as letras disponíveis nesta jogada: ")

while (letras_rodada != "SAIR"):

    posicao_bonus = int(input("Digite a posição bônus: "))
    if posicao_bonus >= 0:
        for palavra in banco_palavras:
            banco_palavras[palavra].set_pontuacao_bonus(palavra, dicionario_pontuacao, posicao_bonus)
            #modifica a pontuação de cada palavra do banco de acordo
    elif posicao_bonus < 0:
        print("Posição inválida!")
        continue

    letras_validas, letras_nao_usadas, num_letras_validas = tratamento_entrada.trata_entrada(letras_rodada, dicionario_pontuacao)
    melhor_palavra = pontuacao.calcula_pontuacao_maxima(banco_palavras, letras_validas, num_letras_validas)
    if melhor_palavra != '':
        resultado.imprime_resultado(melhor_palavra, banco_palavras[melhor_palavra].pontuacao, letras_validas, letras_nao_usadas)
    else:
        print("\nNenhuma palavra encontrada.")
        print("Sobraram:", str.upper(letras_rodada))
        print("\n---------------------------------------------------------------------------------\n")
    letras_rodada = input("Digite as letras disponíveis nesta jogada: ")
    if letras_rodada == "SAIR":
        print("Programa finalizado!")
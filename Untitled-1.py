import string
import collections 
import tratamento_entrada
import pontuacao


dicionario_pontuacao = {"a" : 1, "b" : 3, "c" : 3, "d" : 2, "e" : 1, "f" : 5, "g" : 2, "h" : 5, "i" : 1, "j" : 8, "l" : 1,
"m" : 3, "n" : 1, "o" : 1, "p" : 3, "q" : 13, "r" : 1, "s" : 1, "t" : 1, "u" : 1, "v" : 5, "x" : 8, "z" : 13} 
#Associa as letras a suas respectivas pontuações

banco_palavras = ['abacaxi', 'manada', 'mandar', 'porta', 'mesa', 'dado', 'mangas', 'ja', 'coisas', 'radiografia', 
'matematica', 'drogas', 'predios', 'implementacao', 'computador', 'balao', 'xicara', 'tedio', 'faixa', 'livro', 
'deixar', 'superior', 'profissao', 'reuniao', 'predios', 'montanha', 'botanica', 'banheiro', 'caixas', 'xingamento', 
'infestacao', 'cupim', 'premiada', 'empanada', 'ratos', 'ruido', 'antecedente', 'empresa', 'emissario', 'folga', 'fratura', 
'goiaba', 'gratuito', 'hidrico', 'homem', 'jantar', 'jogos', 'montagem', 'manual', 'nuvem', 'neve', 'operacao', 'ontem', 
'pato', 'pe', 'viagem', 'queijo', 'quarto', 'quintal', 'solto', 'rota', 'selva', 'tatuagem', 'tigre', 'uva', 'ultimo', 
'vituperio', 'voltagem', 'zangado', 'zombaria', 'dor']

letras_rodada = str.lower(input("Digite as letras disponíveis nesta jogada: "))
letras_rodada, letras_nao_usadas = tratamento_entrada.freq_letra(letras_rodada, dicionario_pontuacao)
freq_ocorrencia_letras = dict(collections.Counter(letras_rodada)) #quantas vezes cada letra válida aparece na entrada

pontuacao = pontuacao.calcula_pontuacao_palavra("abacaxi", dicionario_pontuacao)




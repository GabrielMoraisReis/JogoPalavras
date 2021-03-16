import collections


class ValorBancoPalavras:
    def __init__(self, palavra, dicionario_pontuacao):
        self.pontuacao = self.calcula_pontuacao_palavra(palavra, dicionario_pontuacao)
        self.contagem_letras = dict(collections.Counter(palavra)) #quantas vezes cada letra aparece em uma palavra
    
    def calcula_pontuacao_palavra(self, palavra, dicionario_pontuacao):
        pontuacao = 0
        for letra in palavra:
            pontuacao += dicionario_pontuacao[letra]
        return pontuacao

def tratamento_banco_palavras(banco_palavras, dicionario_pontuacao):
    banco_palavras_modificado = dict()
    for palavra in banco_palavras:
        banco_palavras_modificado[palavra] = ValorBancoPalavras(palavra, dicionario_pontuacao)
    return banco_palavras_modificado
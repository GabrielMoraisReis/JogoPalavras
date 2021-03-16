import collections


class ValorBancoPalavras:
    def __init__(self, palavra, dicionario_pontuacao):
        self.pontuacao_base = self.calcula_pontuacao_base(palavra, dicionario_pontuacao)
        self.pontuacao = self.pontuacao_base
        self.contagem_letras = dict(collections.Counter(palavra)) #quantas vezes cada letra aparece em uma palavra
    
    def calcula_pontuacao_base(self, palavra, dicionario_pontuacao):
        pontuacao = 0
        for letra in palavra:
            pontuacao += dicionario_pontuacao[letra]
        return pontuacao

    def set_pontuacao_bonus(self, palavra, dicionario_pontuacao, index):
        if index == 0:
            self.pontuacao = self.pontuacao_base
        elif index <= len(palavra):
            self.pontuacao = self.pontuacao_base + dicionario_pontuacao[palavra[index - 1]]

def tratamento_banco_palavras(banco_palavras, dicionario_pontuacao):
    banco_palavras_modificado = dict()
    for palavra in banco_palavras:
        banco_palavras_modificado[palavra] = ValorBancoPalavras(palavra, dicionario_pontuacao)
    return banco_palavras_modificado

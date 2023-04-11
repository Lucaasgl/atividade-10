def calcular_media(lista):
    """
    Função para calcular a média dos números em uma lista.
    Recebe como parâmetro uma lista de números.
    Retorna o valor da média.
    """
    soma = sum(lista)
    media = soma / len(lista)
    return media


# Função para ler os valores
def ler_numeros():
    """
    Função para ler uma lista de números fornecidos pelo usuário.
    Retorna a lista de números.
    """
    numeros = input("Digite os números separados por espaço: ").split()
    numeros = [int(numero) for numero in numeros]
    return numeros


# Chamada da função para ler os números
numeros = ler_numeros()

# Chamada da função para calcular a média
media = calcular_media(numeros)

# Apresentação do resultado
print("Lista de números: {}".format(numeros))
print("Média dos números: {}".format(media))
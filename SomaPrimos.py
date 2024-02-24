def primo(numero):
    '''
    Função para saber se um número é primo
    '''

    if numero <=1:
        return False
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            return False
    return True

soma = 0

for numero in range(2,1000):
    if primo(numero):
        soma += numero

print(f'A soma de todos os nº menores que 1000 é {soma}')

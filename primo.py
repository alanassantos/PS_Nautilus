def primo(numero):
    '''
    Programa que diz o maior divisor primo de um número dado como input
    '''
    divisor = 2
    fatorado = []

    while numero > 1:
        if numero % divisor == 0:
            fatorado.append(divisor)
            numero = numero // divisor
        else:
            divisor += 1
    
    return max(fatorado) if fatorado else 1

while True:
    numero = int(input('Digite o número p/ saber seu maior divisor primo:  '))
    if numero <= 0:
        print('O número deve ser um inteiro positivo!')
        continue

    resultado = primo(numero)
    print(f'P/ {numero} o maior divisor primo é {resultado}')
    break
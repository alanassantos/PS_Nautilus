def palindromo(numero):
    '''
    Função que diz se um número qualquer é palíndromo
    '''
    
    STRNumero = str(numero)
    INumero = STRNumero[::-1]

    return STRNumero == INumero 

if __name__ == '__main__':
    while True:
        numeros = input('Digite o número que deseja verificar ou a letra S p/ Sair:   ')

        if numeros.upper() == 'S':
            break
        
        if numeros.isdigit():
            if palindromo(numeros):
                print(f'{numeros} é um palíndromo!')
            else:
                print(f'{numeros} não é um palíndromo!')
                
        else:
            print('Digite apenas nº ou a letra S p/ sair!')

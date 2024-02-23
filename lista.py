def vrlista(lista):
    '''
    Programa que diz se o primeiro e o último itens de uma lista são iguais.
    '''
    if len(lista) < 2:
        print('A lista precisa ter pelo menos dois elementos para fazer a comparação!')

    elif lista[0] == lista[-1]:
        print('O primeiro e último itens da lista são iguais!')
    
    else:
        print('O primeiro e último itens da lista são diferentes!')

if __name__ == '__main__':
    lista = input('Digite os elementos da lista separado por espaço apenas: ')
    lista = lista.split()
    verifica = vrlista(lista)


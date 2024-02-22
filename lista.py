#1- Faça um programa que diga se o primeiro e o último ítens de uma lista são iguais(deve funcionar para qualquer lista, ou seja, a quantidade de ítens não é fixa)

def vrlista(lista):
    if len(lista) < 2:
        print('A lista precisa ter pelo menos dois elementos para fazer a comparação!')
        return False

    elif lista[0] == lista[-1]:
        print('O primeiro e último itens da lista são iguais!')
        return True
    
    else:
        print('O primeiro e último itens da lista são diferentes!')
        return False

if __name__ == '__main__':
    lista = input('Digite os elementos da lista separado por espaço apenas: ')
    lista = lista.split()
    verifica = vrlista(lista)


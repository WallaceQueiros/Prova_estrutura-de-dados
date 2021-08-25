from random import shuffle
from os import path
from time import sleep
from sys import exit


# Wallace dos Santos Queiros-201810251 #
# Davy Braga-202011038 #
# Gabriel Gomes Flôr Frederico-202011021 #

def bubble_sort(lista):
    # primeiro laço para manter controle
    # de quantos elementos ja estao ordenados
    for pointer in range(len(lista)):
        # segundo laço para fazer as comparações ate o pointer
        # os elementos depois do pointer ja estao ordenados
        for j in range(len(lista) - pointer - 1):
            # fazendo a comparação
            if lista[j] > lista[j + 1]:
                # fazendo o swap
                tmp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = tmp
    return lista


def insertion_sort(lista):
    # iterando por todos os elementos da lista
    # a partir do segundo.
    for i in range(1, len(lista)):
        # jogando o elemento da lista para uma var temporaria
        tmp = lista.pop(i)
        # compara com todos os elementos anteriores
        # ate encontrar algum que seja menor
        # ou chegar no primeiro indice
        while i > 0 and lista[i - 1] > tmp:
            i -= 1
        # inserindo o valor na lista em seu devido indice
        lista.insert(i, tmp)
    return lista


def selection_sort(lista):
    # topo da stack
    if len(lista) == 1:
        return lista
    # encontrando o menor valor da lista
    min_idx = 0
    for idx, vlr in enumerate(lista[1:]):
        if vlr < lista[min_idx]:
            min_idx = idx + 1
    minimo = lista.pop(min_idx)
    # chamada recursiva passando como parametro a msma
    # lista porem sem o menor valor
    return [minimo] + selection_sort(lista)


def quick_sort(lista):
    # topo da stack
    if len(lista) <= 1:
        return lista
    # escolhendo o pivo
    pivo = lista[0]
    menores = []
    maiores = []
    # separa os elementos em 2 vetores: maiores e menores que o pivo
    for i in lista[1:]:
        if i > pivo:
            maiores.append(i)
        else:
            menores.append(i)
    # chamada recursiva para ordenar os dois grupos
    return quick_sort(menores) + [pivo] + quick_sort(maiores)


def merge_sort(lista):
    # topo da stack
    if len(lista) <= 1:
        return lista
    # chamada recursiva que divide a lista em 2 partes ate chegar no topo da stack
    # onde teremos cada valor em um vetor de 1 elemento
    #               lhs -> left hand side       ||    rhs -> right hand side
    lhs, rhs = merge_sort(lista[:len(lista) // 2]), merge_sort(lista[len(lista) // 2:])
    # agora que ja temos todos os valores individuais distribuidos pela stack
    # podemos limpar a lista para que ela possa receber os valores ordenados
    lista.clear()
    while len(lhs) > 0 and len(rhs) > 0:
        # compara o primeiro elemento de cada lado e adiciona o menor
        # valor na lista ate que lhs ou rhs fique vazia
        vlr = lhs.pop(0) if lhs[0] <= rhs[0] else rhs.pop(0)
        lista.append(vlr)
    # concatena o que restar
    return lista + lhs + rhs


# OBS: nao comentei esses metodos do menu pq presumi que nao houvesse necessidade

def join_string(lista):
    return '\n'.join(lista)


def lista_to_str(lista):
    return '; '.join([f'[{i}]=>{vlr}' for i, vlr in enumerate(lista)]) + '\n'


def clear():
    print('\n' * 123)


def get_input(msg):
    clear()
    return input(msg + '\n')


def print_output(msg):
    clear()
    print(msg + '\n')
    sleep(1)


def le_arquivo(nome):
    with open(nome) as arquivo:
        lista = arquivo.read().split(',')
    return lista


def get_nome():
    nome = get_input('Digite o nome do arquivo:')
    while not path.exists(nome):
        if path.exists(nome + '.csv'):
            nome = nome + '.csv'
        else:
            print_output('Arquivo não encontrado.')
            nome = get_input('Digite o nome do arquivo:')
    return nome


def sort(funcao):
    nome = get_nome()
    lista = le_arquivo(nome)
    ordenada = funcao([int(i) for i in lista])
    return lista_to_str([str(i) for i in ordenada])


def imprimir_arquivo_de_dados():
    nome = get_nome()
    lista = le_arquivo(nome)
    return lista_to_str(lista)


def alterar_arquivo_de_dados():
    menu = join_string([
        '1- Incluir',
        '2- Alterar',
        '3- Excluir',
        '4- Voltar ao menu principal'
    ])
    nome = get_nome()
    lista = le_arquivo(nome)

    opcao = 0
    while opcao != 4:
        show_menu = lambda: '\n' + lista_to_str(lista) + '\n' + menu + '\n'
        msg = show_menu() + '\nDigite a opção desejada:'
        opcao = int(get_input(msg))
        if opcao == 1:
            vlr = get_input(show_menu() + '\nDigite o valor a ser adicionado:')
            lista.append(vlr)
        elif opcao == 2:
            indice = int(get_input(show_menu() + '\nDigite o indice a ser alterado:'))
            vlr = get_input(show_menu() + f'\nDigite o novo valor do indice {indice}')
            lista[indice] = vlr
        elif opcao == 3:
            indice = int(get_input(show_menu() + '\nDigite o indice a ser removido:'))
            del lista[indice]
        elif opcao == 4:
            with open(nome, 'w') as arquivo:
                arquivo.write(','.join(lista))
        else:
            print_output('\nOpção Inválida')


def criar_arquivo_de_dados():
    nome = get_input('Digite o nome do arquivo:')
    n = int(get_input('Digite o tamanho da lista:'))
    lista = list(range(n if n > 0 else -n))
    lista = [str(i) for i in lista]
    shuffle(lista)

    with open(f'{nome}.csv', 'w') as arquivo:
        arquivo.write(','.join(lista))
    print_output('Arquivo salvo.')


def menu0():
    menu = join_string([
        PAINEL,
        '1- Criar arquivo de dados',
        '2- Alterar arquivo de dados',
        '3- Imprimir arquivo de dados',
        '4- Bubble Sort',
        '5- Insertion Sort',
        '6- Selection Sort',
        '7- Quick Sort',
        '8- Merge Sort',
        '9- Finalizar o programa.\n\n'
    ])
    opt = {
        '1': criar_arquivo_de_dados,
        '2': alterar_arquivo_de_dados,
        '3': imprimir_arquivo_de_dados,
        '4': lambda: sort(bubble_sort),
        '5': lambda: sort(insertion_sort),
        '6': lambda: sort(selection_sort),
        '7': lambda: sort(quick_sort),
        '8': lambda: sort(merge_sort),
        '9': lambda: exit(0),
    }
    lista = None
    while True:
        msg = '\n' if lista is None else lista
        opcao = get_input(menu + msg + '\nDigite a opção desejada:')
        '\n'
        if opcao not in opt.keys():
            print('Opção inválida.')
            sleep(1)

        lista = opt[opcao]()


if __name__ == '__main__':
    LINHA = '-' * 35
    TITULO = ' ' * 3 + 'Algoritmos de Ordenação'

    PAINEL = join_string([LINHA, TITULO, LINHA])

    menu0()

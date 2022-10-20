from Torre import Torre

def mover_disco(origem,destino):
    if origem != 0 and destino != 0:
        origem = torres[int(origem)-1]
        destino = torres[int(destino)-1]

        if origem.get_tamanho() != 0:
            destino_last = destino.last_disco()
            disco = origem.last_disco()

            if destino_last > disco or destino_last == 0:
                origem.desempilha()
                destino.empilha(disco)
            else:
                print('Operação invalida.')
        else:
            print('Não tem nenhum disco nessa torre.')
    else:
        print('Origem ou Destino não podem ser 0.')

def color(color, text): 
    text = '\033[1;{color};40m' + str(text) +'\033[0;0m'
    return text.format(color=int(color))

if __name__ == '__main__':
    qntd = int(input('Digite a quantidade de discos para ser inserido na torre 1: '))
    discos = []
    for i in range(-qntd, 0):
        discos.append(-i)

    torres = [Torre(discos),Torre([]),Torre([])]
    i = len(torres)
    while torres[i-1].get_tamanho() != qntd:
        print(color(33, '\n Torre 1:'))
        torres[0].to_string()
        print(color(34, '\n Torre 2:'))
        torres[1].to_string()
        print(color(35, '\n Torre 3:'))
        torres[2].to_string()

        print('\n Mover disco: ')
        mover_disco(int(input('Digite a origem: ')), int(input('Digite o destino: ')))

print(color(33, '\n Torre 1:'))
torres[0].to_string()
print(color(34, '\n Torre 2:'))
torres[1].to_string()
print(color(35, '\n Torre 3:'))
torres[2].to_string()

print('\n Parabéns Você terminou a Torre de Hanoi!')        

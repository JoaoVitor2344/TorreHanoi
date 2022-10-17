from Torre import Torre

def mover_disco(origem,destino):
    origem = torres[int(origem)-1]
    destino = torres[int(destino)-1]

    if origem.get_tamanho() != 0:
        disco = int(origem.last_disco())

        if destino.last_disco() > disco or destino.get_tamanho() == 0:
            origem.desempilha()
            destino.empilha(disco)
        else:
            print('Operação invalida.')
    else:
        print('Não tem nenhum disco nessa torre.')

def color(color,text): 
    text = '\033[1;{color};40m' + str(text) +'\033[0;0m'
    print(text.format(color=int(color)))

if __name__ == '__main__':
    qntd = int(input('Digite a quantidade de discos para ser inserido na torre 1: '))
    discos = []
    for i in range(-qntd, 0):
        discos.append(-i)

    torres = [Torre(discos),Torre([]),Torre([])]
    while torres[2].get_tamanho() != qntd:
        color(33, 'Torre 1:')
        torres[0].to_string()
        color(34, 'Torre 2:')
        torres[1].to_string()
        color(35, 'Torre 3:')
        torres[2].to_string()

        print('\nMover disco: ')
        mover_disco(int(input('Digite a origem: ')), int(input('Digite o destino: ')))

color(32, 'Torre 1:')
torres[0].to_string()
color(33, 'Torre 2:')
torres[1].to_string()
color(34, 'Torre 3:')
torres[2].to_string()

print('Parabéns Você terminou a Torre de Hanoi!')        

from Torre import Torre

def mover_disco(disco,origem,destino):
    origem = torres[int(origem)-1]
    destino = torres[int(destino)-1]

    if origem.last_disco() == int(disco):
        origem.desempilha()
        destino.empilha(disco)
    else:
        print('Este disco não esta nessa torre')

if __name__ == '__main__':
    qntd = int(input('Digite a quantidade de discos: '))
    discos = []
    for i in range(-qntd, 0):
        discos.append(-i)

    pronto = True
    
    torres = [Torre(discos),Torre([]),Torre([])]
    while pronto:
        mover_disco(int(input('Digite o disco: ')), int(input('Digite a origem: ')), int(input('Digite o destino: ')))

        print('')

        torres[0].to_string()
        torres[1].to_string()
        torres[2].to_string()

        if torres[2].get_tamanho() == 5:
            pronto = False

print('Parabéns Você terminou a Torre de Hanoi!')        

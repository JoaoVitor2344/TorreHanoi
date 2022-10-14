class Torre:
    def __init__(self,discos):
        self._discos = discos
    
    def empilha(self,disco):
        if self.get_tamanho() == 0:
            self._discos.append(disco)
        else:
            if int(self.last_disco()) > disco:
                self._discos.append(disco)
            else:
                print('Não é possivel inserir esse disco')
    
    def desempilha(self):
        return self._discos.pop()

    def get_tamanho(self):
        return len(self._discos)

    def last_disco(self):
        return self._discos[len(self._discos)-1]

    def to_string(self):
        print('Quantidade de discos: ' + str(self.get_tamanho()))

        for disco in self._discos:
            print(disco)

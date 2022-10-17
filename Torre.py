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
        if self.get_tamanho() == 0:
            return 0
        else:
            return self._discos[len(self._discos)-1]

    def find_disco(self, disco):
        for i in self._discos:
            if int(disco) == i:
                return True
        
        return False

    def to_string(self):
        print('Quantidade de discos: ' + str(self.get_tamanho()))

        color = 30
        i = 0
        for disco in self._discos:
            color += i
            i += 1
            text = '\033[1;{color};40m' + str(disco) +'\033[0;0m'
            print(text.format(color=int(color)))
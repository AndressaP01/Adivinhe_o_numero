
class Sorteio():
    def __init__(self):
        self.numeroSistema=89

    def sortear(self,numeroEscolhido):
        self.numeroEscolhido=numeroEscolhido
        if self.numeroEscolhido>self.numeroSistema:
            sorteio=0;
            print("Errou!! Tente um número menor")
        elif self.numeroEscolhido<self.numeroSistema:
            sorteio=0;
            print("Errou!!! Tente um número maior")
        else:
            sorteio=1
            print("Parabéns!!!! Você acertou")
        return sorteio;

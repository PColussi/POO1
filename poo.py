class Elevador:
    def __init__(self,total_capacidade,total_andar) -> None:
        self.total_capacidade = total_capacidade
        self.atual_capacidade = 0
        self.total_andar = total_andar
        self.atual_andar = 0
        pass

    def subir(self):
        if self.atual_andar < self.total_andar:
            self.atual_andar += 1
            print("Subindo.")
        else:
            print("VOCÊ ESTÁ NO ANDAR MAIS ALTO!")
    

    def descer(self):
        if self.atual_andar > 0:
            self.atual_andar -= 1
            print("Descendo.")
        else:
            print("VOCÊ JÁ ESTÁ NO TÉRREO!")

    def entrar(self):
        if self.atual_capacidade < self.total_capacidade:
            self.atual_capacidade += 1
            print("Entrando uma pessoa.")
        else:
            print("O ELEVADOR ESTÁ CHEIO!")
    
    def sair(self):
        if self.atual_capacidade > 0:
            self.atual_capacidade -= 1
            print("Saindo uma pessoa.")
        else:
            print("NÃO TEM NINGUÉM")


elevador = Elevador(9, 15)

elevador.subir()
elevador.entrar()
elevador.subir()
elevador.subir()
elevador.entrar()
elevador.descer()
elevador.sair()
elevador.descer()
elevador.sair()
elevador.sair()

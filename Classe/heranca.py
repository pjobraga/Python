
class Pai:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso


class Filha(Pai):
    def __init__(self, nome, peso, cabelo):
        super().__init__(nome, peso)
        self.cabelo = cabelo


pessoa1 = Pai('Pedro', 95)

filha1 = Filha('Inded ', 13, 'moreno')

print(filha1.nome)
print(filha1.peso)
print(filha1.cabelo)

import random
from decimal import Decimal
from math import floor
#Decorators
def nada(funcao):
    def wrapper(*args):
        return funcao(*args)
    return wrapper

def dano_critico(funcao):
    def wrapper(*args):
        chance = random.random()  
        argumentos = list(args)
        if chance < 0.3:
            argumentos[1] = floor(argumentos[1] * 1.2)
            print(f"\033[1;32m{argumentos[0].nome} sofreu dano crítico\033m")
        return funcao(*argumentos)
    return wrapper

def escudo(funcao):
    def wrapper(*args):
        argumentos = list(args)
        chance = random.random()
        if 0 < chance < 0.2: # O dano vai ser zerado
            print(f"\033[1;32m{argumentos[0].nome} bloqueou o ataque!\033m")
            argumentos[1] = 0 # Anula o dano
        elif 0.2 < chance < 0.7: # O dano vai ser apenas de 50%
            print(f"\033[1;32m{argumentos[0].nome} reduziu o dano em 50%\033[m")
            argumentos[1] /= 2  #Metade do dano
        else:
            print(f"\033[1;32mO escudo de {argumentos[0].nome} falhou\033[m")
            # O dano vai ser completo

        return funcao(*argumentos)
    return wrapper

def regeneracao(funcao):
    def wrapper(*args):
        argumentos = list(args)
        argumentos[0].vida += 10
        print(funcao(*argumentos))
        return f"\033[1;32m{argumentos[0].nome} usou regenerou 10 pontos de vida\033[m"
    return wrapper

class ContadorFuncao:
    def __init__(self,funcao):
        self.contador = 0
        self.funcao = funcao
    
    def __call__(self, *args, **kwds):
        self.contador += 1
        print(self.contador)
        return self.funcao(*args, **kwds)

decoradores = {
    "dano_critico": dano_critico,
    "escudo": escudo,
    "regeneracao": regeneracao,
    "nada": nada
}

#escolha = random.choices(list(decoradores.keys()), weights=(2,2,1,5))[0]
class Personagem:
    
    def __init__(self,nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.vida_original = self.vida
    
    def atacar_base(self,oponente, dano):
        Escudo_Ativado = False
        if dano < oponente.defesa:
            return f"\033[1;31mO ataque de {self.nome} não foi efetivo para a defesa de {oponente.nome}\033[m"
        if Escudo_Ativado:
            dano *= oponente.escudo()
        oponente.receber_ataque(dano)
        return f"\033[1;33m{self.nome} causou {dano} de dano em {oponente.nome}\033[m"
    
    def atacar(self, oponente, dano):
        escolha = random.choices(list(decoradores.keys()), weights=(2,2,1,5))[0]
        func = decoradores[escolha](self.atacar_base)
        return func(oponente,dano)
    
    def calcular_dano(self, oponente):
        dano = abs((self.ataque - oponente.defesa ))
        return dano 

    def receber_ataque(self, dano):
        self.vida -= dano #REVER

    def exibir_vida(self):
        coracao_cheio = int((Decimal(self.vida/self.vida_original) * 10).quantize(Decimal("1")))
        mensagem = f"{" ❤️​" * coracao_cheio} {"​🖤​" * (10 - coracao_cheio)}"
        return mensagem

    def exibir_vida2(self):
        return f"{int(self.vida)}/{self.vida_original}"


import classes
import exibir
from time import sleep
from os import system


player1 = player2 = None
for i in range(2):
    while True:
        nome = str(input("Nome do Personagem: ")).strip()
        if nome.isnumeric():
            print("ERRO! Não é permitido números.")
            continue
        while True:
            try:
                vida = int(input("Qual será a vida do personagem: "))
                if vida <= 0:
                    print("ERRO! Não é aceito números negativos")
                    continue
            except ValueError:
                print("ERRO! Somente é aceito números")
                continue
            break
        while True:
            try:
                ataque = int(input("Qual será o ataque do personagem: "))
                if ataque <= 0:
                    print("ERRO! Não é aceito números negativos")
                    continue
            except ValueError:
                print("ERRO! Somente é aceito números")
                continue
            break
        while True:
            try:
                defesa = int(input("Qual será a defesa do personagem: "))
                if defesa <= 0:
                    print("ERRO! Não é aceito números negativos")
                    continue
            except ValueError:
                print("ERRO! Somente é aceito números")
                continue
            break 
        break
    if i == 1:
        player1 = classes.Personagem(nome, vida, ataque, defesa)
    else:
        player2 = classes.Personagem(nome, vida, ataque, defesa)
    print(f"Personagem {nome} cadastrado com sucesso!")

system("cls")

rounds = 1
acabar = False
while not acabar:
    print(f"\033[4;35m#round{rounds}\033[m")
    sleep(4)
    exibir.cabeçalho("LISTA DE MENSAGENS")

    print(f'\033[1;33m{player1.atacar(player2, player1.calcular_dano(player2))}\033[m')
    print(f'\033[1;33m{player2.atacar(player1, player2.calcular_dano(player1))}\033[m')

    exibir.cabeçalho("VIDA")
    print(f"{player1.nome}{player1.exibir_vida()}  VS{player2.exibir_vida()}  {player2.nome}")
    print(f"\033[4;36m{player1.exibir_vida2()}\033[m".center(45), f"\033[4;36m{player2.exibir_vida2()}\033[m".center(25))
    exibir.escrever_linha()
    rounds += 1
    if player1.vida <= 0 or player2.vida <= 0:
        acabar = True


def escrever_linha():
    print(f'\033[97m{"--"* 33}\033[m')

def cabeçalho(nome):
    escrever_linha()
    print(f"\033[1;97m{nome}\033[m".center(75))
    escrever_linha()


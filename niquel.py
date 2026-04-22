import random
import time
import os

SIMBOLOS = [ '🚀', '⭐', '💎', '🪙', '🍀', '🎁' ]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_maquina(colunas, status):
    limpar_tela()
    print("=" * 25)
    print(" TESTE ")
    print("=" * 25)
    print(f" {colunas[0]} | {colunas[1]} | {colunas[2]} ")
    print("=" * 25)
    print(f" STATUS: {status}")

def girar():
    input("\n[ ENTER PARA JOGAR ]")

    # Estado inicial (tudo girando)
    resultado = [random.choice(SIMBOLOS) for _ in range(3)]

    # Fases: 0 = tudo girando, 1 = coluna 1 parou, 2 = coluna 2 parou, 3 = tudo parou
    for fase in range(4):
        # Quantidade de giros em cada fase
        giros_na_fase = 10 if fase < 3 else 1

        for i in range(giros_na_fase):
            # Atualiza apenas as colunas que ainda não "travaram"
            if fase == 0: # Gira as 3
                resultado[0] = random.choice(SIMBOLOS)
                resultado[1] = random.choice(SIMBOLOS)
                resultado[2] = random.choice(SIMBOLOS)
            elif fase == 1: # Gira apenas 2 e 3
                resultado[1] = random.choice(SIMBOLOS)
                resultado[2] = random.choice(SIMBOLOS)
            elif fase == 2: # Gira apenas a última
                resultado[2] = random.choice(SIMBOLOS)
            
            exibir_maquina(resultado, "GIRANDO..." if fase < 3 else "PAROU!")

            # Controle de velocidade: acelera no início e desacelera no fim de cada fase
            delay = 0.05 + (i * 0.01)
            time.sleep(delay)

# Para rodar o código, você precisaria chamar a função girar() ao final:
if __name__ == "__main__":
    while True:
        girar()


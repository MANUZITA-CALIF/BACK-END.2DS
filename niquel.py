import random
import time
import os

SIMBOLOS = ['🚀', '⭐', '💎', '🪙', '🍀', '🎁']

def limpar_tela():
    # Tenta limpar a tela; se falhar (em alguns IDEs), apenas pula linhas
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_maquina(colunas, status):
    limpar_tela()
    print("=" * 25)
    print("      SLOT MACHINE")
    print("=" * 25)
    print(f"  {colunas[0]}  |  {colunas[1]}  |  {colunas[2]}  ")
    print("=" * 25)
    print(f" STATUS: {status}")

def girar():
    input("\n[ PRESSIONE ENTER PARA JOGAR ]")

    resultado = [random.choice(SIMBOLOS) for _ in range(3)]

    # Fases: 0=tudo, 1=para a primeira, 2=para a segunda, 3=para tudo
    for fase in range(4):
        giros_na_fase = 8 if fase < 3 else 1

        for i in range(giros_na_fase):
            if fase == 0:
                resultado[0] = random.choice(SIMBOLOS)
                resultado[1] = random.choice(SIMBOLOS)
                resultado[2] = random.choice(SIMBOLOS)
            elif fase == 1:
                resultado[1] = random.choice(SIMBOLOS)
                resultado[2] = random.choice(SIMBOLOS)
            elif fase == 2:
                resultado[2] = random.choice(SIMBOLOS)
            
            exibir_maquina(resultado, "GIRANDO..." if fase < 3 else "PAROU!")
            
            # Ajuste de delay para fluidez
            delay = 0.05 + (i * 0.02)
            time.sleep(delay)

    # Checa vitória simples
    if resultado[0] == resultado[1] == resultado[2]:
        print("\n💰 JACKPOT! VOCÊ VENCEU! 💰")
    else:
        print("\n❌ Não foi dessa vez!")

if __name__ == "__main__":
    try:
        while True:
            girar()
    except KeyboardInterrupt:
        print("\nAté a próxima!")

    

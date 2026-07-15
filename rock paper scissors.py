import random


opcoes = ["pedra", "papel", "tesoura"]
print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    
while True:
        jogador = input("Escolha pedra, papel ou tesoura (ou 'sair' para sair): ").lower()
        
        if jogador == "sair":
            print("Saindo do jogo.")
            break
        if jogador not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue

        computador = random.choice(opcoes)
        print(f"Computador escolheu: {computador}")

        if jogador == computador:
            print("Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or \
             (jogador == "papel" and computador == "pedra") or \
             (jogador == "tesoura" and computador == "papel"):
            print("Você venceu!")
        else:
            print("Você perdeu!")
import random


palavras = ["python", "programacao", "desenvolvimento", "computador", "algoritmo", "espeto", "escola", "prisão", "capitalismo", "navio", "tempo", "ferias", "iguana", "empresa"]
palavra_secreta = random.choice(palavras)
letras_corretas = ["_"] * len(palavra_secreta)
tentativas = 6
letras_erradas = []

print("Bem-vindo ao jogo da Forca!")

play_again = True

while tentativas > 0:
        print("Palavra:", " ".join(letras_corretas))
        print("Letras erradas:", ", ".join(letras_erradas))
        letra = input(f"Tente uma letra (tentativas restantes: {tentativas}): ").lower()

        if letra in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    letras_corretas[i] = letra
            if "_" not in letras_corretas:
                print("Parabéns! Você acertou a palavra:", palavra_secreta)
                break
        else:
            letras_erradas.append(letra)
            tentativas -= 1

        if tentativas == 0:
            print("Você perdeu! A palavra era:", palavra_secreta)

answer = input("Do you want to play again? (y/n): ").strip().lower()
if answer != "y":
    play_again = False
    print("Thanks for playing!")        
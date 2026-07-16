
perguntas = {
        "Qual é a capital do Brasil?": "brasília",
        "Quem é o criador do Python?": "guido van rossum",
        "Qual é o maior planeta do sistema solar?": "júpiter",
        "Em que ano o homem pisou na lua pela primeira vez?": "1969"
    }

pontos = 0
print("Bem-vindo ao jogo de Quiz!")

play_again = True

while play_again:
    for pergunta, resposta_correta in perguntas.items():
        resposta = input(pergunta + " ").lower()
        if resposta == resposta_correta:
            pontos += 1
            print("Resposta correta!")
        else:
            print(f"Resposta errada! A resposta correta era: {resposta_correta}")

    print(f"Você acertou {pontos} de {len(perguntas)} perguntas!")

    answer = input("Jogar novamente? (s/n): ").strip().lower()
    if answer != "s":
        play_again = False
        print("Obrigado por jogar!")            
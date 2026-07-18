import random
import pygame    

pygame.init()

# Definir as cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Definir as dimensões da tela
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

# Definir o relógio
relogio = pygame.time.Clock()

# Definir o tamanho da cobrinha e a velocidade
tamanho_celula = 10
velocidade = 15

#Boas vindas
print("Bem-vinde ao jogo da cobrinha XD")

# Fonte do texto
fonte = pygame.font.SysFont("bahnschrift", 25)
fonte_pontuacao = pygame.font.SysFont("comicsansms", 35)

# Função para exibir a pontuação
def mostrar_pontuacao(pontos):
        valor = fonte_pontuacao.render("Pontuação: " + str(pontos), True, branco)
        tela.blit(valor, [0, 0])

# Função para desenhar a cobrinha
def desenhar_cobrinha(tamanho_celula, lista_corpo):
        for x in lista_corpo:
            pygame.draw.rect(tela, verde, [x[0], x[1], tamanho_celula, tamanho_celula])

# Função principal do jogo
def jogo():
        fim_de_jogo = False
        perdeu = False

        # Posições iniciais da cobrinha
        x1 = largura / 2
        y1 = altura / 2

        x1_mudanca = 0
        y1_mudanca = 0

        # Corpo da cobrinha
        corpo_cobrinha = []
        comprimento_cobrinha = 1

        # Posições da comida
        comida_x = round(random.randrange(0, largura - tamanho_celula) / 10.0) * 10.0
        comida_y = round(random.randrange(0, altura - tamanho_celula) / 10.0) * 10.0

        # Pontuação
        pontos = 0

        while not fim_de_jogo:

            # Verificar eventos do teclado
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_de_jogo = True
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        x1_mudanca = -tamanho_celula
                        y1_mudanca = 0
                    elif evento.key == pygame.K_RIGHT:
                        x1_mudanca = tamanho_celula
                        y1_mudanca = 0
                    elif evento.key == pygame.K_UP:
                        y1_mudanca = -tamanho_celula
                        x1_mudanca = 0
                    elif evento.key == pygame.K_DOWN:
                        y1_mudanca = tamanho_celula
                        x1_mudanca = 0

            # Verificar se a cobrinha bateu nas bordas
            if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
                perdeu = True

            # Atualizar a posição da cobrinha
            x1 += x1_mudanca
            y1 += y1_mudanca
            tela.fill(azul)

            # Desenhar a comida
            pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_celula, tamanho_celula])

            # Atualizar o corpo da cobrinha
            corpo_cobrinha.append([x1, y1])
            if len(corpo_cobrinha) > comprimento_cobrinha:
                del corpo_cobrinha[0]

            # Verificar colisão com o próprio corpo
            for segmento in corpo_cobrinha[:-1]:
                if segmento == [x1, y1]:
                    perdeu = True

            desenhar_cobrinha(tamanho_celula, corpo_cobrinha)
            mostrar_pontuacao(pontos)

            # Atualizar a tela
            pygame.display.update()

            # Verificar se a cobrinha comeu a comida
            if x1 == comida_x and y1 == comida_y:
                comida_x = round(random.randrange(0, largura - tamanho_celula) / 10.0) * 10.0
                comida_y = round(random.randrange(0, altura - tamanho_celula) / 10.0) * 10.0
                comprimento_cobrinha += 1
                pontos += 10

            # Verificar se o jogo acabou
            while perdeu:
                tela.fill(azul)

                linha1 = fonte.render("Você Perdeu!", True, vermelho)
                linha2 = fonte.render("Pressione Q para Sair", True, vermelho)
                linha3 = fonte.render("ou C para Jogar Novamente", True, vermelho)

                tela.blit(linha1, [largura / 6, altura / 3])
                tela.blit(linha2, [largura / 6, altura / 3 + 30])
                tela.blit(linha3, [largura / 6, altura / 3 + 60])
                
                mostrar_pontuacao(pontos)
                pygame.display.update()

                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        perdeu = False
                        fim_de_jogo = True
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_q:
                            perdeu = False
                            fim_de_jogo = True
                        if evento.key == pygame.K_c:
                            jogo()

            relogio.tick(velocidade)

        # Fechar o pygame
        pygame.quit()
        quit()

    # Iniciar o jogo
jogo()

# Chama o menu principal
main()
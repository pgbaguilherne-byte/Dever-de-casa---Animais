import pygame
import random

pygame.init()

# --- CONFIGURAÇÃO DA TELA ---
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Noite de Natal")

clock = pygame.time.Clock()

# --- CORES ---
BRANCO = (255,255,255)
PRETO = (0,0,0)
VERMELHO = (255,0,0)

# --- JOGADOR ---
larg_jogador = 200
alt_jogador = 200
y_jogador = ALTURA // 2 - alt_jogador
x_jogador = LARGURA - larg_jogador - 600
vel_jogador = 7

# --- CARREGAR IMAGEM DO PAPAI NOEL ---
# Ajuste o caminho ABAIXO:
jogador_img = pygame.image.load("treno_papai_noel.png").convert_alpha()
jogador_img = pygame.transform.scale(jogador_img, (larg_jogador, alt_jogador))


# Inimigos 
larg_obstaculo = 50
alt_obstaculo = 50

def criar_obstaculos():
    """Cria um inimigo em posição X aleatória, acima da tela."""
    x = random.randint(LARGURA, LARGURA + 200)
    y = random.randint(0, 350)  # começa fora da tela
    return [x, y]  # usamos [x, y] para poder alterar depois

obstaculos = [criar_obstaculos()]  # começamos com 1 inimigo

# --- CARREGAR IMAGEM DOS OBSTACULOS---
# Ajuste o caminho ABAIXO:
obstaculo_img = pygame.image.load("estrela.png").convert_alpha()
obstaculo_img = pygame.transform.scale(obstaculo_img, (alt_obstaculo, larg_obstaculo))


# --- LOOP PRINCIPAL DO JOGO ---
rodando = True
while rodando:

    clock.tick(60)

    # EVENTOS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # MOVIMENTAÇÃO
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_DOWN]:
        y_jogador += vel_jogador
    if teclas[pygame.K_UP]:
        y_jogador -= vel_jogador

        # Limitar o jogador à tela
    if y_jogador < 0:
        y_jogador = 0 
    if y_jogador > 250:
        y_jogador = 250 



    # --- DESENHO ---
    tela.fill(PRETO)

    # Desenha o Papai Noel
    tela.blit(jogador_img, (x_jogador, y_jogador))

    # Desenha os obstaculos
    for obstaculo in obstaculos:
        
        # mover para a direita
        obstaculo[0] -= 5

        # se sair da tela, voltar
        if obstaculo[0] < - larg_obstaculo:
            obstaculo[0] = random.randint(LARGURA, LARGURA +200)
            obstaculo[1] = random.randint(0, 350)

        tela.blit(obstaculo_img, (obstaculo[0],obstaculo[1]))
 

    pygame.display.update()

pygame.quit()

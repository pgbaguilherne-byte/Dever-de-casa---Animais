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
larg_jogador = 70
alt_jogador = 70
# posicionamento inicial (coloque onde desejar; aqui fica perto da esquerda)
x_jogador = 50
y_jogador = ALTURA // 2 - alt_jogador // 2
vel_jogador = 7

# limites verticais do jogador: topo = 0, baixo = 2/3 da tela
limite_topo = 0
limite_baixo = ALTURA * 2 // 3  # 2/3 da altura

# --- CARREGAR IMAGEM DO PAPAI NOEL ---
# coloque a imagem na mesma pasta do .py ou ajuste o caminho ("assets/treno_papai_noel.png")
jogador_img = pygame.image.load("treno_papai_noel.png").convert_alpha()
# O transform.scale recebe (width, height)
jogador_img = pygame.transform.scale(jogador_img, (larg_jogador, alt_jogador))

# --- OBSTÁCULOS ---
larg_obstaculo = 35
alt_obstaculo = 35

def criar_obstaculo():
    # surge à direita, entre LARGURA e LARGURA+200
    x = random.randint(LARGURA, LARGURA + 200)
    # faixa vertical entre 0 e 250 (ou altere conforme quiser)
    y = random.randint(0, 250)
    return [x, y]

obstaculos = [criar_obstaculo()]

# --- CARREGAR IMAGEM DOS OBSTACULOS ---
obstaculo_img = pygame.image.load("estrela.png").convert_alpha()
obstaculo_img = pygame.transform.scale(obstaculo_img, (larg_obstaculo, alt_obstaculo))

# --- PONTUAÇÃO E FONTE ---
pontuacao = 0
fonte = pygame.font.SysFont("arial", 24)

rodando = True
game_over = False

while rodando:
    clock.tick(60)

    # --- EVENTOS ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if game_over and evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                # reiniciar
                game_over = False
                pontuacao = 0
                x_jogador = 50
                y_jogador = ALTURA // 2 - alt_jogador // 2
                obstaculos = [criar_obstaculo()]

    if not game_over:
        # --- MOVIMENTO DO JOGADOR (captura por frame) ---
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            y_jogador += vel_jogador
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            y_jogador -= vel_jogador
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            x_jogador -= vel_jogador
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            x_jogador += vel_jogador

        # limitar jogador na tela (horizontais)
        if x_jogador < 0:
            x_jogador = 0
        if x_jogador > LARGURA - larg_jogador:
            x_jogador = LARGURA - larg_jogador

        # limitar vertical conforme pedido (topo até 2/3 da tela)
        if y_jogador < limite_topo:
            y_jogador = limite_topo
        if y_jogador > limite_baixo:
            y_jogador = limite_baixo

        # --- DIFICULDADE / VELOCIDADE DOS OBSTÁCULOS ---
        vel_obstaculo = 5 + pontuacao // 5
        qtd_obstaculos_desejada = 1 + pontuacao // 10
        while len(obstaculos) < qtd_obstaculos_desejada:
            obstaculos.append(criar_obstaculo())

        # --- MOVER OBSTÁCULOS (da direita para a esquerda) ---
        for obst in obstaculos:
            obst[0] -= vel_obstaculo  # x -= velocidade (vai para a esquerda)

            # se saiu totalmente pela esquerda, reposiciona à direita e soma ponto
            if obst[0] < -larg_obstaculo:
                obst[0] = random.randint(LARGURA, LARGURA + 200)
                obst[1] = random.randint(0, 250)
                pontuacao += 1

        # --- COLISÃO ---
        rect_jogador = pygame.Rect(x_jogador, y_jogador, larg_jogador, alt_jogador)
        for obst in obstaculos:
            rect_obst = pygame.Rect(obst[0], obst[1], larg_obstaculo, alt_obstaculo)
            if rect_jogador.colliderect(rect_obst):
                game_over = True
                break

    # --- DESENHO ---
    tela.fill(PRETO)

    # --- CARREGAR IMAGEM DO FUNDO ---
    fundo = pygame.image.load("fundo_noite.png").convert()
    fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

    # Posições iniciais dos dois fundos (efeito de loop infinito)
    fundo_x1 = 0
    fundo_x2 = LARGURA

    vel_fundo = 2   # velocidade do efeito de voo

        # --- MOVIMENTO DO FUNDO ---
    fundo_x1 -= vel_fundo
    fundo_x2 -= vel_fundo

    # Quando sair da tela, reinicia
    if fundo_x1 <= -LARGURA:
        fundo_x1 = LARGURA

    if fundo_x2 <= -LARGURA:
        fundo_x2 = LARGURA

    # --- DESENHA OS FUNDOS ---
    tela.blit(fundo, (fundo_x1, 0))
    tela.blit(fundo, (fundo_x2, 0))


    tela.blit(jogador_img, (x_jogador, y_jogador))

    for obst in obstaculos:
        tela.blit(obstaculo_img, (obst[0], obst[1]))

    # pontuação
    texto_pontos = fonte.render(f"Pontuação: {pontuacao}", True, BRANCO)
    tela.blit(texto_pontos, (10, 10))

    if game_over:
        texto_go = fonte.render("GAME OVER! Aperte ESPAÇO para reiniciar.", True, BRANCO)
        tela.blit(texto_go, (150, ALTURA // 2))

    pygame.display.update()

pygame.quit()

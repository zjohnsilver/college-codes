#######################################
## Jogo da Forca
##
## Criado por Lancelot
##
## 19.05.2017
#######################################

import pygame, modulo, random, time, telas

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

WINDOW_WIDTH = 600 # size <--> pixels
WINDOW_HEIGHT = 400 # size I pixels

#            R    G    B
GRAY      = (100, 100, 100)
DARK_GRAY = ( 49,  79,  79)
NAVYBLUE  = ( 60,  60, 100)
WHITE     = (255, 255, 255)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 255)
YELLOW    = (255, 255,   0)
ORANGE    = (255, 128,   0)
PURPLE    = (255,   0, 255)
CYAN      = (  0, 255, 255)
BLACK     = (  0,   0,   0)
FIREBRICK = (178,  34,  34)
GREENBLCK = (  0, 100,   0)
ROSYBROWN = (188, 143, 143)
SEAGREEN  = ( 46, 139,  87)
LIGHT_GRAY = (211, 211, 211)




BACKGROUND_COLOR = NAVYBLUE

dicas_palavras = modulo.ler_arquivo()
dica = modulo.sorteio_dica()
palavra = random.choice(dicas_palavras[dica]) ##Sorteando a palavra

partes = ["cabeca",
          "corpo",
          "braco_esquerdo",
          "braco_direito",
          "perna_esquerda",
          "perna_direita"]

## Sprites do jogo
carregar_partes = {"cabeca": pygame.image.load("sprites/cabeca.png"),
                   "corpo": pygame.image.load("sprites/corpo.png"),
                   "braco_esquerdo": pygame.image.load("sprites/braco_esquerdo.png"),
                   "braco_direito": pygame.image.load("sprites/braco_direito.png"),
                   "perna_esquerda": pygame.image.load("sprites/perna_esquerda.png"),
                   "perna_direita": pygame.image.load("sprites/perna_direita.png")}

coordenadas_partes = {"cabeca":           (120,  60),
                      "corpo":            (164, 132),
                      "braco_esquerdo":   (120, 132),
                      "braco_direito":    (164, 132),
                      "perna_esquerda":   (130, 220),
                      "perna_direita":    (165, 220)}

## CONSTANTES DO RETANGULO DAS LETRAS
POSX_BASE = 278
POSY_BASE = 268
WIDTH_RECT = 20
HEIGHT_RECT = 25

vitoria = 0
derrota = 0

MENU = True



def main():
    global palavra, letras, vitoria, derrota

    gameExit = False


    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepress = pygame.mouse.get_pressed()


                for num in range (65, 91):
                    if vitoria<len(palavra):
                        if letras["%s"%(chr(num))].collidepoint(pygame.mouse.get_pos()) \
                                    and mousepress[0]:
                            number = (num-65) % 10
                            posX = POSX_BASE + number*22
                            number2 = (num-65) // 10
                            posY = POSY_BASE + number2*28

                            letras["%s"%(chr(num))] = \
                                pygame.draw.rect(DISPLAY_SURF, GRAY,
                                             (posX, posY, WIDTH_RECT, HEIGHT_RECT))

                            ## Verifica se tem a letra e se tiver ja coloca na palavra
                            if (verifica_se_tem(chr(num))):
                                print (vitoria, len(palavra))
                            else:
                                parte_do_corpo(carregar_partes[partes[derrota]], coordenadas_partes[partes[derrota]])
                                derrota+=1
                            gerar_letras()
        if vitoria == len(palavra)-1:
            tela_vitoria()
        if derrota == len(partes):
            tela_derrota()


        pygame.display.update()


def message_to_screen(msg, color, posicao, tamanho):
    font = pygame.font.SysFont(None, tamanho, 1)
    screen_text = font.render(msg, True, color)
    DISPLAY_SURF.blit(screen_text, posicao)

def gerar_letras():
    posX = 280
    posY = 270
    for num in range(65, 91):
        if ((num-65) % 10) == 0 and (num-65) != 0:
            posX = 280
            posY += 28
        message_to_screen(chr(num), BLACK, (posX, posY), 30)
        posX+=22

def gerar_interface():
    global letras, dica, palavra
    posX1 = 278
    posX2 = posX1+22
    posGeralY = 240
    cor_line = BLACK
    for line in range(len(palavra)-1):
        pygame.draw.line(DISPLAY_SURF, cor_line, [posX1, posGeralY],
                                                 [posX2,posGeralY], 5)
        posX1 += 27
        posX2 = posX1 + 22


    message_to_screen("DICA: " + dica, WHITE, (270, 40), 30)

    forca = pygame.image.load("sprites/forca.png") #importando forca
    DISPLAY_SURF.blit(forca, (40, 20)) #jogando forca na tela

    letras = {}

    ## GERANDO RETANGULOS DAS LETRAS
    COLOR_RECT = WHITE
    for num in range(65, 91):
        number = (num-65) % 10
        posX = POSX_BASE + number*22
        number2 = (num-65) // 10
        posY = POSY_BASE + number2*28

        letras["%s"%(chr(num))] = \
            pygame.draw.rect(DISPLAY_SURF, COLOR_RECT,
                         (posX, posY, WIDTH_RECT, HEIGHT_RECT))



    gerar_letras()


def verifica_se_tem(tentativa):
    global vitoria
    if tentativa in palavra:
        indices = modulo.busca_indices(palavra, tentativa)

        for indice in indices:
            message_to_screen(tentativa, WHITE, (280 + 27*indice, 220), 30)
            vitoria+=1

        return True

    else:
        return False

def parte_do_corpo(parte, coordenada):
    DISPLAY_SURF.blit(parte, coordenada)


def reset(dica2 = True):
    global DISPLAY_SURF, vitoria, derrota, dica, palavra
    
    pygame.init()
    
    if dica2 == True:
        dica = modulo.sorteio_dica()
    else:
        dica = dica2
    
    DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Jogo da Forca")

    DISPLAY_SURF.fill(BACKGROUND_COLOR)
    
    vitoria, derrota = (0,0)

    palavra = random.choice(dicas_palavras[dica]) ##Sorteando a palavra
    

    return False

def tela_menu():
    DISPLAY_SURF.fill(DARK_GRAY)
        
    COR_RECT = GRAY
    COR_MESSAGE = ORANGE
    
    message_to_screen("MENU", LIGHT_GRAY, (200, 40), 100) 

    
    novo_jogo = pygame.draw.rect(DISPLAY_SURF, COR_RECT, (240, 160, 130, 30))
    message_to_screen("NOVO JOGO", COR_MESSAGE, (254, 167), 24)
    
    categorias = pygame.draw.rect(DISPLAY_SURF, COR_RECT, (240, 210, 130, 30))
    message_to_screen("CATEGORIAS", COR_MESSAGE, (245, 217), 24)
    
    opcoes = pygame.draw.rect(DISPLAY_SURF, COR_RECT, (240, 260, 130, 30))
    message_to_screen("OPCOES", COR_MESSAGE, (268, 267), 24)
    
    creditos = pygame.draw.rect(DISPLAY_SURF, COR_RECT, (240, 310, 130, 30))
    message_to_screen("CREDITOS", COR_MESSAGE, (258, 317), 24)
    
    
    gameExit = False
    

    while not gameExit:
        for event in pygame.event.get():
            print (event)
            if event.type == pygame.QUIT:
                quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepress = pygame.mouse.get_pressed()

                if novo_jogo.collidepoint(pygame.mouse.get_pos()) and mousepress[0]:
                    reset()
                    gerar_interface()
                    main()
                if categorias.collidepoint(pygame.mouse.get_pos()) and mousepress[0]:
                    reset()
                    tela_categorias()
                    main()
                    
        pygame.display.update()
        
def tela_categorias():
    global vitoria, derrota, dica
    
    DISPLAY_SURF.fill(DARK_GRAY)
    
    COR_RECT = GRAY
    COR_CATEGORIAS = BLACK
    
    message_to_screen("CATEGORIAS", LIGHT_GRAY, (40, 30), 100)  ## LIGHT GRAY
    message_to_screen("Selecione a categoria que deseja jogar", SEAGREEN, (50, 130), 25)
    
    
    ## Categoria Animal
    animal = pygame.draw.rect(DISPLAY_SURF, COR_RECT, (70, 185, 120, 40))
    message_to_screen("ANIMAL", COR_CATEGORIAS, (74, 193), 35)
    
    ## Categoria Objeto
    objeto = pygame.draw.rect(DISPLAY_SURF, COR_RECT, (240, 185, 120, 40))
    message_to_screen("OBJETO", COR_CATEGORIAS, (244, 193), 35)
    
    ## League of Legends
    league = pygame.draw.rect(DISPLAY_SURF, COR_RECT, (410, 185, 120, 40))
    message_to_screen("League of", COR_CATEGORIAS, (423, 187), 25)
    message_to_screen("Legends", COR_CATEGORIAS, (431, 207), 25)
    
    
    ## 
    pygame.draw.rect(DISPLAY_SURF, COR_RECT, (70, 255, 120, 40))
    pygame.draw.rect(DISPLAY_SURF, COR_RECT, (240, 255, 120, 40))
    pygame.draw.rect(DISPLAY_SURF, COR_RECT, (410, 255, 120, 40))
    
    pygame.draw.rect(DISPLAY_SURF, YELLOW, (395, 330, 150, 40))
    message_to_screen("PLAY", BLUE, (430, 337), 40)
    
    pygame.draw.rect(DISPLAY_SURF, BLACK, (20, 330, 130, 40))
    message_to_screen("BACK", FIREBRICK, (40, 337), 40)
    
    
    gameExit = False
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepress = pygame.mouse.get_pressed()
                if animal.collidepoint(pygame.mouse.get_pos()) and mousepress[0]:
                    pygame.draw.rect(DISPLAY_SURF, SEAGREEN, (70, 185, 120, 40))
                    message_to_screen("ANIMAL", COR_CATEGORIAS, (74, 193), 35)
                    reset("ANIMAL")
                    gerar_interface()
                    main()
                if objeto.collidepoint(pygame.mouse.get_pos()) and mousepress[0]:
                    pygame.draw.rect(DISPLAY_SURF, SEAGREEN, (240, 185, 120, 40))
                    message_to_screen("OBJETO", COR_CATEGORIAS, (244, 193), 35)
                    reset("OBJETO")
                    gerar_interface()
                    main()
                if league.collidepoint(pygame.mouse.get_pos()) and mousepress[0]:
                    league = pygame.draw.rect(DISPLAY_SURF, SEAGREEN, (410, 185, 120, 40))
                    message_to_screen("League of", COR_CATEGORIAS, (423, 187), 25)
                    message_to_screen("Legends", COR_CATEGORIAS, (431, 207), 25)
                    reset("LEAGUE OF LEGENDS")
                    gerar_interface()
                    main()
                    
                ####
                #
                # Implementacao do botao PLAY, e fazer com que ao se clicar novamente
                # na categoria desejana, ela se descelecione =) 
                    
                
                
            pygame.display.update()

                
    
def tela_vitoria():   
    gameExit = False
    
    DISPLAY_SURF.fill(NAVYBLUE)
    
    # Imagem da tela de vitoria
    vitoria = pygame.image.load("sprites/victory.png")
    DISPLAY_SURF.blit(vitoria, (90, 0))      
    
    #Criando uma superficie com alpha, qualquer draw nessa superficie sera transparente.
    s = pygame.Surface((600, 400), pygame.SRCALPHA)   # per-pixel alpha
    s.fill((255,255,255,0))                           # notice the alpha value in the color
    DISPLAY_SURF.blit(s, (0,0))                       # jogando na superficie PAI

    #retangulo desenhado na superficie alpha que foi criada anteriormente.
    janela = pygame.draw.rect(s, WHITE, (0, 0, 600, 400))

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepress = pygame.mouse.get_pressed()
                if janela.collidepoint(pygame.mouse.get_pos()) and mousepress[0]:
                    reset()
                    tela_menu()
                    
        pygame.display.update()    


def tela_derrota():
    gameExit = False
    
    DISPLAY_SURF.fill(FIREBRICK)
    
    # Imagem da tela de derrota
    derrota = pygame.image.load("sprites/derrota.png")
    DISPLAY_SURF.blit(derrota, (10, -90))       
    
    #Criando uma superficie com alpha, qualquer draw nessa superficie sera transparente.
    s = pygame.Surface((600, 400), pygame.SRCALPHA)   # per-pixel alpha
    s.fill((255,255,255,0))                           # notice the alpha value in the color
    DISPLAY_SURF.blit(s, (0,0))                       # jogando na superficie PAI

    #retangulo desenhado na superficie alpha que foi criada anteriormente.
    janela = pygame.draw.rect(s, WHITE, (0, 0, 600, 400))

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepress = pygame.mouse.get_pressed()
                if janela.collidepoint(pygame.mouse.get_pos()) and mousepress[0]:
                    reset()
                    tela_menu()
                    
        pygame.display.update()

reset()
tela_menu()

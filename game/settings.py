import pygame, math

white = 255, 255, 255
black = 0, 0, 0
brown = 160,82,45

size = width, height = 600, 600

default_host_port = 9009
default_host_ip = "127.0.0.1"
default_client_port = 8001
default_client_ip = "127.0.0.1"

pawn_icon_1 = pygame.transform.scale( pygame.image.load("images/pawn1.png"), (math.floor(width/8), math.floor(width/8)))
pawn_icon_2 = pygame.transform.scale(pygame.image.load("images/pawn2.png"), (math.floor(width/8), math.floor(width/8)))

rook_icon_1 = pygame.transform.scale(pygame.image.load("images/rook1.png"), (math.floor(width/8), math.floor(width/8)))
rook_icon_2 = pygame.transform.scale(pygame.image.load("images/rook2.png"), (math.floor(width/8), math.floor(width/8)))

knight_icon_1 = pygame.transform.scale(pygame.image.load("images/knight1.png"), (math.floor(width/8), math.floor(width/8)))
knight_icon_2 = pygame.transform.scale(pygame.image.load("images/knight2.png"), (math.floor(width/8), math.floor(width/8)))

bishop_icon_1 = pygame.transform.scale(pygame.image.load("images/bishop1.png"), (math.floor(width/8), math.floor(width/8)))
bishop_icon_2 = pygame.transform.scale( pygame.image.load("images/bishop2.png"), (math.floor(width/8), math.floor(width/8)))

queen_icon_1 = pygame.transform.scale(pygame.image.load("images/queen1.png"), (math.floor(width/8), math.floor(width/8)))
queen_icon_2 = pygame.transform.scale(pygame.image.load("images/queen2.png"), (math.floor(width/8), math.floor(width/8)))

king_icon_1 = pygame.transform.scale(pygame.image.load("images/king1.png"), (math.floor(width/8), math.floor(width/8)))
king_icon_2 = pygame.transform.scale(pygame.image.load("images/king2.png"), (math.floor(width/8), math.floor(width/8)))

game_types = ["human-v-human", "human-v-computer", "computer-v-computer"]
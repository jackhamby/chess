import sys, math, pygame
from game import Player, Board
from network import Client, Server
from time import sleep
import threading

class Game():

    def __init__(self, screen, team=None):
        self.player1 = Player(self, 1)
        self.player2 = Player(self, 2)
        self.running = False

        self.going_player = self.player2
        self.board = Board(screen, self)
                

    def start(self):
        self.running = True
        self.board.setup()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_down(event.pos)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:     
                        self.handle_mouse_up(event.pos)
            
                elif event.type == pygame.MOUSEMOTION:
                    self.handle_mouse_motion(event.pos)
            self.render()
            pygame.display.flip()


    def stop(self):
        self.running = False
        sys.exit()

    def handle_mouse_down(self, pos):
        tile = self.board.get_tile(pos[0], pos[1])
        # Check if is players turn
        if (tile.piece and tile.piece.player.team == self.going_player.team):
            self.going_player.selected_piece = tile.piece
            self.going_player.selected_piece.dragging = True
    
    def handle_mouse_up(self, pos):
        if (not self.going_player.selected_piece):
            return       
        self.going_player.selected_piece.dragging = False
        mouse_x, mouse_y = pos
        tile = self.board.get_tile(mouse_x, mouse_y)
        if (self.going_player.selected_piece.check_move(tile)):
            self.going_player.move_piece(tile)
            self.going_player = self.player1 if self.going_player.team == 2 else self.player2
        else:
            self.going_player.reset_current_piece()

    def handle_mouse_motion(self, pos):
        if (self.going_player.selected_piece and self.going_player.selected_piece.dragging):
            mouse_x, mouse_y = pos
            self.going_player.selected_piece.x_pos = mouse_x - math.floor(self.board.tile_length / 2)
            self.going_player.selected_piece.y_pos = mouse_y - math.floor(self.board.tile_length / 2)

    def render(self):
        self.board.render()
        for piece in self.player1.pieces:
            piece.render()
        for piece in self.player2.pieces:
            piece.render()

    
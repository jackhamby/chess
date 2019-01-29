import sys, math
from .settings import game_types
from game import Player, Board

class Game():

    def __init__(self, screen):
        self.player1 = Player(self, 1)
        self.player2 = Player(self, 2)
        self.running = False

        self.going_player = self.player2

        self.board = Board(screen, self)
        

    def start(self):
        self.running = True
        self.board.setup()

    def stop(self):
        self.running = False
        sys.exit()

    def handle_mouse_down(self, pos):
        tile = self.board.get_tile(pos[0], pos[1])
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

import pygame, math
from .settings import white, black, brown, width, height
from pieces import Pawn, Rook, Knight, Bishop, Queen, King

class Board():

    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.tile_length = math.floor(width/8)
        self.board = self.generate_tiles()
        # self.selected_piece = None
        # self.pieces = []
        # self.player_turn = self.game.player2


    def render(self):
        self.screen.fill(white)
        for row in self.board:
            for tile in row:
                tile.render()
        # Draw lines
        x, y = 0, 0
        while( x <= width ):
            pygame.draw.line(self.screen, black, (x, 0) , (x, height))
            pygame.draw.line(self.screen, black, (0, y) , (width, y))
            x += self.tile_length
            y += self.tile_length

    def generate_tiles(self):
        # Fill in colored tiles
        tiles = []
        y_pos = 0
        # For each row
        for i in range(8):
            tiles.append([])
            x_pos = 0
            color = white if not i % 2 else brown
            # For each column
            for k in range(8):
                tiles[i].append(Tile(self, x_pos, y_pos, k, i, f'{chr(ord("a") + k)}{8 - i}', color))
                x_pos += self.tile_length
                color = brown if color == white else white
            y_pos += self.tile_length
        return tiles

    def get_tile(self, x_pos, y_pos):
        for row in self.board:
            for tile in row:
                if (x_pos >= tile.x_pos and
                    x_pos <= (tile.x_pos + self.tile_length) and
                    y_pos >= tile.y_pos and
                    y_pos <= (tile.y_pos + self.tile_length)):
                    return tile
        return None

    def get_tile_by_id(self, tile_id):
        for row in self.board:
            for tile in row:
                if (tile.id == tile_id):
                    return tile
        return None


    def setup(self):
        # print('setting up')
        self.game.player1.setup()
        self.game.player2.setup()




class Tile():
    
    def __init__(self, board, x_pos, y_pos, x, y, id, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.board = board
        self.x, self.y = x, y
        self.id = id
        self.color = color
        self.piece = None

    def render(self):
        pygame.draw.rect(self.board.screen, self.color, (self.x_pos, self.y_pos, self.board.tile_length, self.board.tile_length))







class Piece():

   def __init__(self, tile, player):
        self.current_tile = tile
        self.current_tile.piece = self
        self.x_pos = self.current_tile.x_pos
        self.y_pos = self.current_tile.y_pos
        self.x, self.y = tile.x, tile.y
        self.player = player
        self.dragging = False
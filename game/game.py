import sys, math, pygame
from game import Player, Board
from network import Client, Server
from time import sleep
import threading

class Game():

    def __init__(self, screen):
        # if (game_type == "hotseat"):
        self.player1 = Player(self, 1)
        self.player2 = Player(self, 2)
        self.running = False

        self.going_player = self.player2
        self.board = Board(screen, self)

        # self.game_type = game_type
        # self.running_player = None
        # self.opponent = None

        # self.client = None
        # self.server = None
        

    def start(self):
        self.running = True
        self.board.setup()
        # if (self.game_type == "client"):
        #     self.running_player = self.player1
        #     self.opponent = self.player2
        #     self.start_as_client()
        # elif (self.game_type == "server"):
        #     self.running_player = self.player2
        #     self.opponent = self.player1
        #     self.start_as_server()
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



    # Commands
    # c       - connect
    # w       - waiting
    # t       - thinking
    # m<x><y> - move
    # q       - quite

    # def start_as_client(self):
    #     self.client = Client()
    #     print('starting as client')

    #     # Intialize connection
    #     try:
    #         # print(f'sending connect to player1 at {client.addr}:{client.server_port} ' )
    #         self.client.conn.sendto(b'c', (self.client.addr, self.client.server_port))
    #     except:
    #         print('couldnt connect')
    #         return

    #     while self.running:

    #         # Recieve command from server
    #         data = self.client.conn.recvfrom(32)   
    #         if (len(data[0]) > 0):
    #             cmd, addr = data[0].decode('ascii'), data[1]
    #             if (cmd == 'w'):
    #                 print('opponent waiting...')
    #             elif (cmd == 't'):
    #                 print('opponent thinking...')
    #             elif (cmd[0] == 'm'):
    #                 self.handle_move(int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4]))
    #                 self.going_player = self.running_player
    #                 print('opponent moved!!!!')
    #             else:
    #                 pass

    #         # Send command to server
    #         if (self.going_player != self.running_player):
    #             self.client.conn.sendto(b'w', (self.client.addr, self.client.server_port))
    #         else:
    #             self.client.conn.sendto(b't', (self.client.addr, self.client.server_port))

            

    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 self.stop()
                    
    #             if event.type == pygame.MOUSEBUTTONDOWN:
    #                 self.handle_mouse_down(event.pos)

    #             elif event.type == pygame.MOUSEBUTTONUP:
    #                 if event.button == 1:     
    #                     self.handle_mouse_up(event.pos)
            
    #             elif event.type == pygame.MOUSEMOTION:
    #                 self.handle_mouse_motion(event.pos)
    #         self.render()
    #         pygame.display.flip()
    


        # Commands
    # w       - waiting
    # t       - thinking
    # m       - move
    # q       - quite

    # def start_as_server(self):
    #     self.server = Server()
    #     print('starting as server')
    #     while self.running:

    #         # Revieve command from client
    #         data = self.server.listener.recvfrom(32)   
    #         if (len(data[0]) > 0):
    #             cmd, addr = data[0].decode('ascii'), data[1]
    #             if (cmd == 'w'):
    #                 print('opponent waiting...')
    #             elif (cmd == 't'):
    #                 print('opponent thinking...')
    #             elif (cmd[0] == 'm'):
    #                 self.handle_move(int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4]))
    #                 self.going_player = self.running_player
    #                 print('opponent moved!!!!')
    #             else:
    #                 pass

    #         # Send command to client
    #         if (self.going_player != self.running_player):
    #             self.server.listener.sendto(b'w', (self.server.host_ip, 8001))
    #         else:
    #             self.server.listener.sendto(b't', (self.server.host_ip, 8001))


    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 self.stop()
                    
    #             if event.type == pygame.MOUSEBUTTONDOWN:
    #                 self.handle_mouse_down(event.pos)

    #             elif event.type == pygame.MOUSEBUTTONUP:
    #                 if event.button == 1:     
    #                     self.handle_mouse_up(event.pos)
            
    #             elif event.type == pygame.MOUSEMOTION:
    #                 self.handle_mouse_motion(event.pos)
    #         self.render()
    #         pygame.display.flip()


    def handle_move(self, from_x, from_y, to_x, to_y):
        self.opponent.selected_piece = self.board.board[from_y][from_x].piece
        tile = self.board.board[to_y][to_x]
        self.opponent.move_piece(tile)


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

    
import pygame, socket
from .game import Game
from .settings import default_host_port, default_client_port, default_host_ip, default_client_ip

class NetworkGame(Game):


    def __init__(self, screen, is_host=False):
        Game.__init__(self, screen)
        self.is_host = is_host
        self.host_ip = default_host_ip
        self.host_port = default_host_port
        self.client_ip = default_client_ip
        self.client_port = default_client_port

        self.conn = None
        self.running_player = None
        self.opponent = None
        
        # Is host
        if (self.is_host):
            self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print(f'waiting for connection at {self.host_ip}:{self.host_port}')
            self.conn.bind((self.host_ip,  self.host_port))
            self.opponent = self.player1
            self.running_player = self.player2

        # Is client   
        else:
            self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.conn.bind((self.client_ip,  self.client_port))
            self.opponent = self.player2
            self.running_player = self.player1



    #         Commands
    # c       - connect
    # w       - waiting
    # t       - thinking
    # m<x><y> - move
    # q       - quite

    def start(self):
        self.running = True
        # print('started')
        self.board.setup()


        # Intialize connection
        if (not self.is_host):
            self.conn.sendto(b'c', (self.host_ip, self.host_port))

        while self.running:

            # Recieve command from server/cient
            data = self.conn.recvfrom(32)   
            if (len(data[0]) > 0):
                cmd, addr = data[0].decode('ascii'), data[1]
                if (cmd == 'w'):
                    print('opponent waiting...')
                elif (cmd == 't'):
                    print('opponent thinking...')
                elif (cmd[0] == 'm'):
                    self.handle_move(int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4]))
                    self.going_player = self.running_player
                    print('opponent moved!!!!')
                else:
                    pass

            # Send command to server/client
            if (self.is_host):
                if (self.going_player != self.running_player):
                    self.conn.sendto(b'w', (self.client_ip, self.client_port))
                else:
                    self.conn.sendto(b't', (self.client_ip, self.client_port))

            else:
                if (self.going_player != self.running_player):
                    self.conn.sendto(b'w', (self.host_ip, self.host_port))
                else:
                    self.conn.sendto(b't', (self.host_ip, self.host_port))

            # Handle game events
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


    def handle_mouse_down(self, pos):
        tile = self.board.get_tile(pos[0], pos[1])
        # Check if is players turn
        if (tile.piece and tile.piece.player.team == self.going_player.team):

            # If network game, make sure going_player is running_player
            if (not self.running_player or (self.running_player == self.going_player)):
                self.going_player.selected_piece = tile.piece
                self.going_player.selected_piece.dragging = True
    
    def handle_mouse_up(self, pos):
        if (not self.going_player.selected_piece):
            return       
        self.going_player.selected_piece.dragging = False
        mouse_x, mouse_y = pos
        tile = self.board.get_tile(mouse_x, mouse_y)
        if (self.going_player.selected_piece.check_move(tile)):

            # Send move to client/server
            if( self.is_host):
                message = f'm{self.going_player.selected_piece.x}{self.going_player.selected_piece.y}{tile.x}{tile.y}'.encode('ascii')
                self.conn.sendto(message, (self.client_ip, self.client_port))
            else:
                message = f'm{self.going_player.selected_piece.x}{self.going_player.selected_piece.y}{tile.x}{tile.y}'.encode('ascii')
                self.conn.sendto(message, (self.host_ip, self.host_port))

            self.going_player.move_piece(tile)
            self.going_player = self.player1 if self.going_player.team == 2 else self.player2

        else:
            self.going_player.reset_current_piece()
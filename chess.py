
import sys, pygame, math
from game import Board, Game, NetworkGame
from game.settings import size

### TODO
# - Castleing
# - Win condition

game_types = ["client", "server"]
# game_type = "network"

def run(is_network=False, is_host=False):
    pygame.init()
    screen = pygame.display.set_mode(size)
    if (is_network):
        game = NetworkGame(screen, is_host)
        # game.start()
    else:
        game = Game(screen)
    game.start()

if __name__ == "__main__":
    # game_type = sys.argv[2]
    # print(sys.argv[1])
    if (len(sys.argv) >= 2):
        if (sys.argv[1] == "host"):
            # print('hosting')
            run(True, True)
        elif (sys.argv[1] == "join"):
            # print('jpining')
            run(True)
        else:
            print('invalid input, please try one of the following:')
            print('$ python3 chess.py')
            print('$ python3 chess.py host')
            print('$ python3 chess.py join')
    else:
        run()
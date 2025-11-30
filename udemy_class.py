class Game(object):

    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("help message: make zoo into the door")

    @classmethod
    def show_top_score(cls):
        print("history score " +f'{cls.top_score}')

    def start_game(self):
        print(f'{self.player_name}'+" begin of game")


Game.show_help()
Game.show_top_score()
game = Game("xiaoming")
game.start_game()
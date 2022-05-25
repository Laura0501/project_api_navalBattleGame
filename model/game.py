from model.list_de import ListDe
from .user import User
from .board import Board


class Game:
    def __init__(self, id:int, player1:User, player2:User, ship_list:ListDe):
        self.id=id
        self.player1=player1
        self.player2=player2
        self.num_ships=ship_list.count
        self.turn=0
        self.hits_player_1=0
        self.hits_player_2=0
        self.board_player1=None
        self.board_player2=None
        self.__create_boards()


    def __create_boards(self, ship_list:ListDe):
        size=0
        if self.num_ships < 10:
            size=10
        elif self.num_ships >10 and self.num_ships < 20:
            size:20
        else:
            size=30

        self.board_player1=Board(1, size, size,self.player1,ship_list)
        self.board_player2=Board(2, size, size, self.player2, ship_list.clone_list())

    def __validate_winner(self):
        if self.hits_player_1 == self.num_ships:
            return {"message": 'Ha ganado jugador 1'}
        elif self.hits_player_2 == self.num_ships:
            return {"message": 'Ha ganado jugador 2'}

    def validate_shoot(self, x: int, y: int, player: User):
        if player == self.player1:
            board = self.board_player2
            board.validate_shot_table(x,y)
        else:
            board = self.board_player1
            board.validate_shot_table(x,y)




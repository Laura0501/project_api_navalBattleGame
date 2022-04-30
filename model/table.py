from model.user import User
from model.list_de import ListDe

class Table:
    def __init__(self, id:int, cols:int, rows: int, player:User, list_ship:ListDe, state_table:bool, shots_received:[]):
        self.id=id
        self.cols=cols
        self.rows=rows
        self.player=player
        self.list_ship=list_ship
        self.state_table=state_table
        self.shots_received=shots_received

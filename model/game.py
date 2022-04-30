from model.table import Table

class Game:
    def __init__(self, id:int, table_player_1:Table, table_player_2:Table, num_ships:int, shift:int,
                 hits_player_1:int, hits_player_2: int):
        self.id=id
        self.table_player_1=table_player_1
        self.table_player_2=table_player_2
        self.num_ships=num_ships
        self.shift=shift
        self.hits_player_1=hits_player_1
        self.hits_player_2=hits_player_2


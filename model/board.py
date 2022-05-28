from model.user import User
from model.list_de import ListDe
from model.ship_distribution import ShipDistribution
from model.coordinate import Coordinate

class Board:
    def __init__(self, id:int, cols:int, rows: int, player:User, ship_list:ListDe):
        self.id = id
        self.cols = cols
        self.rows = rows
        self.player = player
        self.ship_list = ship_list
        self.board_state = False
        self.received_shots = []

    def define_location(self, coordinates:[]):
        self.ship_list.validate_coordinate_list_de(coordinates)
        return {"Message": "El barco ha sido ubicado"}



    def validate_shot_table(self, x:int, y:int):
        if x < self.rows and y < self.cols:
            for shots_received in self.received_shots:
                if x == shots_received.x and y == shots_received.y:
                    raise Exception("Ya se ha disparado en la coordenada ")
                else:
                    temp = self.ship_list.head
                    coordinate=Coordinate(x,y,False)
                    while temp != None:
                        try:
                            if coordinate in temp.data.places:
                                ShipDistribution(temp).validate_shoot(x, y)
                            temp = temp.next
                        except:
                            raise Exception({"Message": "Toco agua"})

                    self.received_shots.append(Coordinate(x, y, True))
        else:
            raise Exception("Coodernada fuera de dimensiones")



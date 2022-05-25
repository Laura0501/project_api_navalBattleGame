from .ship import Ship
from .coordinate import Coordinate

class ShipDistribution:
    def __init__(self, ship:Ship):
        self.places=[]
        self.ship=ship
        self.orientation=0         #Para decir que el barco no se ha posicionado
        self.state= "Free"


    def define_location(self, x: int, y: int, orientation: int):
        if orientation == 0:
            raise Exception("La orientacion no ha sido definida")
        elif orientation ==1:
            num_ships_places=self.ship.num_places
            num_validations=y+num_ships_places
            for coord_y in range(y,num_validations):
                new_coordinate=Coordinate(x,coord_y,False)
                if self.validate_coordinate(new_coordinate) is False:
                    self.places.append(new_coordinate)
                    continue
                else:
                    raise Exception({"Message":"La coordenada no es valida"})
            self.state="Positioned"

        elif orientation == 2:
            num_ships_places = self.ship.num_places
            num_validations = x + num_ships_places
            for coord_x in range(x, num_validations) :
                new_coordinate = Coordinate(coord_x,y,False)
                if self.validate_coordinate(new_coordinate) is False:
                    self.places.append(new_coordinate)
                    continue
                else:
                    raise Exception({"Message":"La coordenada no es valida"})
            self.state="Positioned"

    def validate_coordinate(self, coordinate):
                for coord in self.places:
                    if coord.x == coordinate.x and coord.y == coordinate.y:
                        return True
                return False

    def validate_shoot(self, x:int, y:int):
        count=0
        count_sunken=0
        num_ships_places=self.ship.num_places

        for coordinate in self.places:
            if x == coordinate.x and y == coordinate.y:
                coordinate.state = True
                return {"Messagge":"Toco un barco"}

            if coordinate.state == True:
                count += 1
                if count == num_ships_places and x == coordinate.x and y == coordinate.y:
                    count_sunken +=1
                    return {"Messagge": "Ha hundido un barco"}













from .user_service import UserService
from .list_de_service import ListDeService
from model.list_de import ListDe
from model.game import Game


class gameService:
    def __init__(self):
        ships=ListDeService.get_all_ships_distribution()

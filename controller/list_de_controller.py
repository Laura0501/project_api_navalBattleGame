from flask import Response, Blueprint, jsonify, json, request
from service.list_de_service import ListDeService
from util.util_enconder import UtilEncoder
from model.ship import Ship
from model.ship_distribution import ShipDistribution

app_list_de=Blueprint("app_list_de", __name__)

list_de_service=ListDeService()
ship=ShipDistribution

@app_list_de.route('/list_de/all')
def get_all_students_de():
    return Response(status=200, response=json.dumps(list_de_service.get_all_ships_distribution(), cls=UtilEncoder),
                    mimetype='aplication/json')

@app_list_de.route('/list_de/add_ship', methods=['POST'])
def add_de():
    data = request.json
    list_de_service.add_ship_distribution(Ship(data, list_de_service.list_de.count+1))
    return Response(status=200, response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype='aplication/json')

@app_list_de.route('/ship/define_ubication', methods=['POST'])
def define_location():
    data = request.json
    ship.define_location()
    return Response(status=200, response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype='aplication/json')

@app_list_de.route('/list_de/add_to_start_ship_distribution', methods=['POST'])
def add_to_start_de():
    data = request.json
    list_de_service.add_to_start_ship_distribution(Ship(data, list_de_service.list_de.count+1))
    return Response(status=200,response=json.dumps({"message": "Adicionado exitosamente"}),
                    mimetype="application/json")

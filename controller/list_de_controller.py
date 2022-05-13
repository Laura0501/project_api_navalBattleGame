from flask import Response, Blueprint, jsonify, json, request
from service.list_de_service import ListDe
from util.util_enconder import Util_encoder

app_list_de=Blueprint("app_list_ship", __name__)

list_de_service=ListDe()

@app_list_de.route('/list_de/all')
def get_all_students_de():
    return Response(status=200, response=json.dumps(list_de_service.get_all_ships(), cls=Util_encoder),
                    mimetype='aplication/json')

@app_list_de.route('/list_de/add_ship', methods=['POST'])
def add_de():
    data = request.json
    list_de_service.add_ship(data)
    return Response(status=200, response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype='aplication/json')

@app_list_de.route('/list_de/add_to_start_ship', methods=['POST'])
def add_to_start_de():
    data = request.json
    list_de_service.add_to_start_ship(data)
    return Response(status=200,response=json.dumps({"message": "Adicionado exitosamente"}),
                    mimetype="application/json")

"""from flask import Blueprint, request, jsonify
from service.user_service import create_token, validate_token

app_user=Blueprint("app_user", __name__)


@app_user.route('/user/login', methods=["POST"])
def login():
    data=request.get_json()
    if data ['TypeUser'] == "Administrador" or data ['TypeUser'] == "Jugador":
        return create_token(data=request.get_json())

    else:
        response= jsonify({"Message": "Usuario no aceptado"})
        response.status_code =404
        return response

@app_user.route('/user/verify_token')
def verify_token():
    token=(request.headers['Authorization'].split(" ")[1])
    return validate_token(token,output=True)"""


from flask import Response, Blueprint, jsonify, json, request
from util.util_enconder import UtilEncoder
from service.user_service import UserService
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

app_user=Blueprint("app_user", __name__)
user_service=UserService()

@app_user.route('/user/login', methods=['POST'])
def login():
    try:
        email=request.json.get('email')
        password=request.json.get('password')
        user=user_service.login(email, password)
        acces_token=create_access_token(identity={'user':user})
        return jsonify({'token':acces_token})
    except Exception as error:
        return jsonify({'Message': str(error)})


@app_user.route("/user/list")
@jwt_required()
def get_users():
    return Response(status=200, response=json.dumps(user_service.get_users(),
                    cls=UtilEncoder), mimetype='aplication/json')



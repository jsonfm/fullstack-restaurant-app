from sanic import Blueprint, text, json


users = Blueprint("users", url_prefix="/users")
 

@users.route('/')
async def list_users(request):
    return text("Listing users...")


@users.route('/message', methods=['GET'])
async def create_user(request):
    return json({"message": "hola"})
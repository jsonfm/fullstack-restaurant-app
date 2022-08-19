from sanic import Blueprint
from .users import users

apiv1 = Blueprint.group(users, url_prefix="/api/v1")
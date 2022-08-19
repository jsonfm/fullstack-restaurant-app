# sanic
from sanic import Sanic

# settings
from config import config

# API
from api import apiv1

app = Sanic("RestaurantAPP")
 
app.blueprint(apiv1)

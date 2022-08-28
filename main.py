from starlite import Starlite

from my_app.controllers.user import UserController

app = Starlite(route_handlers=[UserController])

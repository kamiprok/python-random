from aiohttp import web
from random import randrange
from datetime import datetime

routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    x = randrange(1, 101)
    now = datetime.now()
    hello = 'Hello World!'
    return web.Response(text=f'{hello}\n'
                             f'{now}\n'
                             f'{x}')

app = web.Application()
app.add_routes(routes)
web.run_app(app)

# basically flask app but async

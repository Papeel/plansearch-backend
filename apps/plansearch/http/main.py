"""Main App. """

import uvicorn
from starlette.applications import Starlette

from apps.shared.http.exceptions import EXCEPTIONS_APP_HANDLERS
from apps.shared.http.middlewares import Middlewares
from apps.plansearch.http.boot import Bootstrap
from apps.plansearch.http.routes.routes import Routes
from apps.plansearch.http.settings import DEBUG, HOST, PORT, WORKERS


def create_app():
    boot = Bootstrap()
    routes = Routes.setup()
    middlewares = Middlewares.setup()
    app = Starlette(debug=DEBUG, middleware=middlewares, routes=routes, exception_handlers=EXCEPTIONS_APP_HANDLERS)
    app.command_bus = boot.command_bus
    app.query_bus = boot.query_bus
    return app


if __name__ == '__main__':
    uvicorn.run("main:create_app", host=HOST, port=PORT, reload=DEBUG, workers=WORKERS if not DEBUG else 1)
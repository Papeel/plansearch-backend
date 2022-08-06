"""App Middlewares. """
from enum import Enum

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware


class ALLOWED_HTTP_METHODS(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    PATCH = 'PATCH'
    HEAD = 'HEAD'
    OPTIONS = 'OPTIONS'


class Middlewares:
    @staticmethod
    def setup() -> list[Middleware]:
        return [
            Middleware(CORSMiddleware, allow_origins=['*'],
                       allow_methods=[method.value for method in ALLOWED_HTTP_METHODS],
                       allow_headers=['*']),
            Middleware(TrustedHostMiddleware, allowed_hosts=['*'])
        ]

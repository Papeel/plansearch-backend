"""HealthGetView. """
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request

from apps.shared.http.response import Response


class HealthGetView(HTTPEndpoint):
    @staticmethod
    async def get(_request: Request):
        return Response(app='202',
                        type='app.info',
                        detail='server_status_ok')
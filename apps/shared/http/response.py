"""Response. """

from typing import Union

from starlette.status import HTTP_200_OK
from starlette.responses import JSONResponse


class Response:
    def __new__(cls, app: str = None, type: str = None, status: int = None, code: str = None,
                detail: str = None, payload: Union[dict, list] = None, content_location: str = None):
        response = dict()
        response['app'] = app if app else '202'
        response['type'] = type if type else ('app.error' if code else 'app.result')
        response['status'] = status if status else HTTP_200_OK
        response['code'] = code if code else '0'
        response['detail'] = detail if detail else ''
        headers = dict()
        headers['Content-Location'] = content_location if content_location else ''
        if payload or isinstance(payload, list) or isinstance(payload, dict):
            response['payload'] = payload

        return JSONResponse(response, status_code=response['status'], headers=headers)
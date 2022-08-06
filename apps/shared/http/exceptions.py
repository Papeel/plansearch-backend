from starlette.status import HTTP_403_FORBIDDEN
from apps.shared.http.response import Response

EXCEPTIONS_APP_HANDLERS = {
    403: lambda request, exc: Response(app='auth',
                                       status=HTTP_403_FORBIDDEN,
                                       code='-1',
                                       detail='Forbidden',
                                       payload=dict(error='Unauthorized to access this resource'))
}

"""Utils. """

from typing import Any

from starlette.exceptions import HTTPException
from starlette.types import ASGIApp

from apps.shared.http.logger import Logger
from apps.shared.http.response import Response
from apps.plansearch.http.settings import DEBUG
from src.shared.domain.exceptions import DomainException

logger = Logger()


def error_handler(app):
    def function(view):
        async def wrapper(*args: Any, **kwargs: Any) -> ASGIApp:
            try:
                return await view(*args, **kwargs)
            except DomainException as e:
                logger.error(app=app,
                             type='app.error',
                             status=e.status,
                             code=e.code,
                             detail=e.detail,
                             payload=dict(error=e.message))
                return Response(app=e.app,
                                status=e.status,
                                code=e.code,
                                detail=e.detail,
                                payload=dict(error=e.message))
            except HTTPException:
                return await view(*args, **kwargs)
            except Exception as e:
                if not DEBUG:
                    return Response(code='-1',
                                    detail='uncaught_exception',
                                    status=500,
                                    payload=dict(error=repr(e)))
        return wrapper
    return function
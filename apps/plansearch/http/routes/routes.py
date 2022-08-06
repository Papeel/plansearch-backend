
"""App Routes. """

from typing import Sequence

from starlette.routing import Route, BaseRoute, Mount
from starlette.staticfiles import StaticFiles


from apps.plansearch.http.views.health.get import HealthGetView


class Routes:
    @staticmethod
    def setup() -> Sequence[BaseRoute]:
        return [
            Mount('/api/v1', routes=[
                Route('/health', HealthGetView, methods=['GET']),
            ]),
        ]

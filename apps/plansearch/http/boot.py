"""Application Boot. """
import asyncio

import aioboto3
from motor.motor_asyncio import AsyncIOMotorClient

from apps.plansearch.http.settings import MONGODB_URI
from src.shared.infrastructure.bus.command.command_bus import InMemoryCommandBus
from src.shared.infrastructure.bus.query.query_bus import InMemoryQueryBus


class Bootstrap:

    def __init__(self):
        self.mongo_client = AsyncIOMotorClient(MONGODB_URI, uuidRepresentation='standard')
        # Repositories
        # Buses
        self.command_bus = InMemoryCommandBus()
        self.query_bus = InMemoryQueryBus()

        self.query_bus = InMemoryQueryBus()
        self.query_bus_add_handlers()
        self.command_bus_add_handlers()

        self.add_subscribers()

    def add_subscribers(self):
        pass

    def command_bus_add_handlers(self):
        bus = self.command_bus
        # Actions historical

    def query_bus_add_handlers(self):
        bus = self.query_bus

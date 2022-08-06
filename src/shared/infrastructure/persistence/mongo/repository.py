"""MongoRepository. """
from typing import Awaitable, List, TypeVar, Tuple
from uuid import UUID

from motor.motor_asyncio import AsyncIOMotorClient

from apps.plansearch.http.settings import MONGODB_NAME
from src.shared.domain.criteria.criteria import Criteria
from src.shared.domain.value_objects.id import Uuid
from src.shared.infrastructure.persistence.mongo.criteria_converter import MongoCriteriaConverter

T = TypeVar("T")


class MongoRepository:

    def __init__(self, client: AsyncIOMotorClient, collection=None):
        self.client = client[MONGODB_NAME][collection if collection else None]
        self.sequences = client[MONGODB_NAME]['sequences']

    async def insert_one(self, doc: T) -> None:
        await self.client.insert_one(doc)

    async def find_one(self, filter: dict) -> Awaitable[T]:
        return await self.client.find_one(filter)

    async def find_criteria(self, criteria: Criteria) -> Tuple[List[T], int]:
        query = MongoCriteriaConverter(criteria)
        results = await self.client.find(query.filters) \
            .limit(query.limit) \
            .skip(query.offset) \
            .sort(query.order_by, query.order_type).to_list(None)
        counter = await self.client.count_documents(query.filters)
        return results, counter

    async def update_one(self, filter: dict, doc: T) -> None:
        await self.client.update_one(filter,
                                     {'$set': {k: v for k, v in doc.items() if v is not None},
                                      '$unset': {k: v for k, v in doc.items() if v is None}})

    async def delete_one(self, id: Uuid):
        return await self.client.delete_one({'_id': UUID(id.value)})

    async def delete_many(self, filters: dict) -> None:
        return await self.client.delete_many(filters)

    async def find_sequence(self, id: str) -> int:
        sequence = await self.sequences.find_one_and_update(
            {"_id": id}, {"$inc": {"value": 1}}, upsert=True, return_document=True)
        return sequence['value']
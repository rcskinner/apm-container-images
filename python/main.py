import json

from fastapi import FastAPI
from redis import ConnectionPool, Redis
from pydantic import BaseModel

# Create the Redis Connection
pool = ConnectionPool(host="localhost", port=6379, db=0)
r = Redis(connection_pool=pool)


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float


@app.post("/create_item")
async def create_item(item: Item):
    r.set(item.name, item.model_dump_json())
    return item


@app.get("/retrieve_item/{item_name}")
async def retrieve_item(item_name):
    item = r.get(item_name)
    item = json.loads(item)
    return item

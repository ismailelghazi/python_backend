from fastapi import APIRouter
from config.database import collection_name
from schema.schemas import list_serial
from Module.client import Clients
from bson import objectid

router = APIRouter()

# GET Request Method
@router.get("/")
async def get_client():
    client = list_serial(collection_name.find())
    return client

# Post Request
@router.post('/')
async def create_user(client: Clients):
    collection_name.insert_one(dict(client))

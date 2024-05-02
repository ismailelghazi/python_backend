from pydantic import BaseModel

class Clients(BaseModel):
    Cin: str
    Assure: str
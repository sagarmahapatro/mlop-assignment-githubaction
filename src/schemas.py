from pydantic import BaseModel, conlist
class HousingInput(BaseModel):
    features: list
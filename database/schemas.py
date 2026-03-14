from pydantic import BaseModel


class Resposta(BaseModel):
    categoria: str
    resposta_ia: str
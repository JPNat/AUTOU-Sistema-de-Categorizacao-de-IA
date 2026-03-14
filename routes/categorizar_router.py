from typing import Annotated
from fastapi import APIRouter, File, Form, HTTPException, UploadFile, status
from database.schemas import (
    Resposta
)

categorizar_router = APIRouter(
    tags=['Categorizar'],
)

@categorizar_router.post('/')
def categorizar_email(

    arquivo: Annotated[UploadFile | None, File()] = None,
    corpo_email: Annotated[str | None, Form()] = None,

) -> Resposta:
    """Devolve a categoria e a resposta do Gemini.

    Args:
    ----
        arquivo: arquivo em .txt ou PDF com as informações do email
        corpo: Corpo email enviado

    Returns:
    -------
        Resposta: Categoria e resposta

    """

    if not arquivo and not corpo_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Envie pelo menos 1 tipo de dado',
        )

    categoria = 'Muito Bem'
    resposta_ia = 'Boua'

    resposta = Resposta(
        categoria=categoria,
        resposta_ia=resposta_ia
    )
    
    return resposta


import json
from typing import Annotated
from dotenv import load_dotenv
from fastapi import APIRouter, File, Form, HTTPException, UploadFile, status
from database.schemas import (
    Resposta
)

import fitz


from google import genai
from google.genai import types
import os

categorizar_router = APIRouter(
    tags=['Categorizar'],
)

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=GEMINI_API_KEY)

@categorizar_router.post('/')
async def categorizar_email(

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

    conteudo = ''

    if corpo_email:
        conteudo = corpo_email

    else:
        
        if arquivo.content_type == "text/plain":
            conteudo_arquivo = await arquivo.read()
            conteudo = conteudo_arquivo.decode("utf-8")
        
        if arquivo.content_type == 'application/pdf':

            conteudo_arquivo = await arquivo.read()

            doc = fitz.open(stream=conteudo_arquivo, filetype='pdf')
            for page in doc:
                text = page.get_text()
                conteudo += text


                  
    response = client.models.generate_content(
                model="gemini-2.5-flash",
                config=types.GenerateContentConfig(
                    system_instruction = ("Responda estritamente em formato JSON. 1. 'categoria': 'Produtivo' ou 'Improdutivo'. 2. 'resposta': Sugerir respostas automáticas baseadas na classificação realizada. Produtivo: Emails que requerem uma ação ou resposta específica. Não precisa ser imediata para não ser produtiva. Se precisar de invetervenção humana e tirar dúvidas, é produtiva. ex.: solicitações de suporte técnico, atualização sobre casos em aberto, dúvidas sobre o sistema. Improdutivo: Emails a nível baixo de importância, ou seja, que não vai atrapalhar a empresa ex.: mensagens de felicitações, agradecimentos."),
                    response_mime_type="application/json",
                ),

                contents=[conteudo],
    )

    resultado_dict = json.loads(response.text)

    categoria = resultado_dict['categoria']

    resposta_ia = resultado_dict['resposta']

    resposta = Resposta(
        categoria=categoria,
        resposta_ia=resposta_ia
    )
    
    return resposta
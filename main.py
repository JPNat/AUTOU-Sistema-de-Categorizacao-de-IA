import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from routes.categorizar_router import categorizar_router

app = FastAPI()

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5500/FrontEnd/index.html", #Para testes
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_index():
    caminho_html = os.path.join(os.getcwd(), "FrontEnd", "index.html")
    if os.path.exists(caminho_html):
        return FileResponse(caminho_html)
    return {"erro": "Arquivo index.html não encontrado no servidor", "path": caminho_html}

@app.get('/developers')
def read_developers() -> dict[str, list[str]]:
    return {'developers': ['João Pedro Natividade']}

app.include_router(categorizar_router, prefix='/categorizar')



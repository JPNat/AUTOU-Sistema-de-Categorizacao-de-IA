from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.categorizar_router import categorizar_router

app = FastAPI()

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5500/FrontEnd/index.html",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/developers')
def read_developers() -> dict[str, list[str]]:
    return {'developers': ['João Pedro']}

app.include_router(categorizar_router, prefix='/categorizar')



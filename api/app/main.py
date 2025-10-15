
from fastapi import FastAPI
from app.routers.health import router as health_router

app = FastAPI(title="TrebolSoft API")
app.include_router(health_router)

@app.get("/")
def root():
    return {"name": "TrebolSoft API", "status": "ok"}

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.routers.health import router as health_router

app = FastAPI(title="TrebolSoft API")
app.include_router(health_router)

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("bienvenida_trebolsoft.html", "r", encoding="utf-8") as f:
        return f.read()

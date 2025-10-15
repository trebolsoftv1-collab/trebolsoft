
from fastapi import FastAPI
from app.routers.health import router as health_router

app = FastAPI(title="TrebolSoft API")
app.include_router(health_router)

@app.get("/")
def root():
    return {"name": "TrebolSoft API", "status": "ok"}

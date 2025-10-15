from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.routers.health import router as health_router
import os

app = FastAPI(title="TrebolSoft API")
app.include_router(health_router)

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("bienvenida_trebolsoft.html", "r", encoding="utf-8") as f:
        return f.read()

# Solo necesario si ejecutas directamente este archivo
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

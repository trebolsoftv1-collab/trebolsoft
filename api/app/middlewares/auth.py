
from starlette.requests import Request

async def auth_middleware(request: Request, call_next):
    # Allow health and docs for now (MVP)
    return await call_next(request)

async def current_user():
    return type("User", (), {"id": None, "role": "cobrador"})()

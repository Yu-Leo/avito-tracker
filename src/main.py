import threading

import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

import crud
from core.db import SessionLocal
from handlers import router

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(router)

if __name__ == "__main__":
    thr = threading.Thread(target=crud.regular_parse, args=(10,), name='thr-1', daemon=True)
    thr.start()
    uvicorn.run(app, host="127.0.0.1", port=8000)

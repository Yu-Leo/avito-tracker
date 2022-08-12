"""
File with FastAPI application
"""
from fastapi import FastAPI

from tracker.api import router

app = FastAPI()

app.include_router(router)

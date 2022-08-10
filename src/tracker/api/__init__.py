from fastapi import APIRouter

from .avito_queries import router as queries_router

router = APIRouter()
router.include_router(queries_router)

from fastapi import FastAPI
from app.api.version1 import authen

app = FastAPI()

app.include_router(authen.router, prefix="/api/version1/authen", tags=["authen"])

from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

from app.core.config.seed_db import seed_database
from app.core.router import get_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await seed_database()
    
    yield
    
app = FastAPI(description="Swagger для дэм экзамена", version='1', openapi_url='/openapi.json', lifespan=lifespan)

static_path = Path(__file__).parent / "static"

app.mount("/static", StaticFiles(directory=static_path), name="static")

app.include_router(get_router())


if __name__ == '__main__':
    uvicorn.run(
        app=app,
        host='0.0.0.0',
        port=8005,
        use_colors=True
    )
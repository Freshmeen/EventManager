import os
import traceback

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

from example.backend.app.api.v1 import api_router
from example.backend.app.api.v1.exceptions import setup_exception_handlers
from example.backend.app.database.session import engine, Base


@asynccontextmanager
async def lifespan(_: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Database initialized")

    yield

    await engine.dispose()
    print("🛑 Engine disposed")


app = FastAPI(title="Books API", lifespan=lifespan, servers=[
    {"url": "http://localhost:8000/"}
])

setup_exception_handlers(app)

app.include_router(api_router, prefix="/api/v1")

dist_dir = "example/frontend/dist"
index_file = os.path.join(dist_dir, "index.html")
public_dir = "example/frontend/static"

app.mount("/static", StaticFiles(directory=public_dir), name="static")

try:
    app.mount("/assets", StaticFiles(directory=os.path.join(dist_dir, "assets")), name="assets")
except BaseException as e:
    traceback.print_exc()


@app.get("/{full_path:path}", include_in_schema=False)
async def serve_frontend(full_path: str):
    if full_path.startswith("api"):
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="API route not found")
    return FileResponse(index_file)

import os
import traceback

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

from backend.app.database.session import engine, Base
from backend.app.api.v1 import api_v1_router

@asynccontextmanager
async def lifespan(_: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Database initialized")

    yield

    await engine.dispose()
    print("Engine disposed")


app = FastAPI(title="Books API", lifespan=lifespan, servers=[
    {"url": "http://localhost:8000/"}
])

app.include_router(api_v1_router)

dist_dir = "frontend/dist"
index_file = os.path.join(dist_dir, "index.html")
public_dir = "frontend/public"

app.mount("/public", StaticFiles(directory=public_dir), name="public")

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

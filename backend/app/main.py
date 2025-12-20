import os
import traceback
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from backend.app.api.v1 import api_v1_router
from backend.app.api.v1.exceptions.base import APIException
from backend.app.database.session import engine, Base


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


@app.exception_handler(APIException)
async def custom_http_exception_handler(request: Request, exc: APIException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.detail,
            "error_code": exc.error_code,
        },
    )


app.include_router(api_v1_router)

dist_dir = "frontend/dist"
public_dir = "frontend/public"
index_file = os.path.join(dist_dir, "index.html")

if os.path.exists(public_dir):
    app.mount("/public", StaticFiles(directory=public_dir), name="public")
else:
    print(f"⚠️ Warning: Public directory '{public_dir}' not found. Static files disabled.")

assets_dir = os.path.join(dist_dir, "assets")
if os.path.exists(assets_dir):
    try:
        app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")
    except Exception:
        traceback.print_exc()
else:
    print(f"⚠️ Warning: Assets directory '{assets_dir}' not found.")

@app.get("/{full_path:path}", include_in_schema=False)
async def serve_frontend(full_path: str):
    if full_path.startswith("api"):
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="API route not found")

    if not os.path.exists(index_file):
        return JSONResponse(
            status_code=404,
            content={"detail": "Frontend not build or index.html not found"}
        )

    return FileResponse(index_file)

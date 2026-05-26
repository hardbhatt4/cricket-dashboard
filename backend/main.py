from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
from services.data_loader import get_data
from services.meta_service import get_metadata
from services.kpi_service import get_kpi
from services.batting_service import get_batting_stats
from services.bowling_service import get_bowling_stats
from schemas import KPIResponse, BattingRow, BowlingRow, MetaResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    get_data()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/api/meta", response_model=MetaResponse)
def meta():
    return get_metadata()


@app.get("/api/kpi", response_model=KPIResponse)
def kpi(season: str | None = None, team: str | None = None):
    return get_kpi(season, team)


@app.get("/api/batting", response_model=list[BattingRow])
def batting(season: str | None = None, team: str | None = None):
    return get_batting_stats(season, team)


@app.get("/api/bowling", response_model=list[BowlingRow])
def bowling(season: str | None = None, team: str | None = None):
    return get_bowling_stats(season, team)


app.mount("/assets", StaticFiles(directory="../frontend/dist/assets"), name="assets")


@app.get("/{full_path:path}")
async def serve_frontend(full_path: str):
    return FileResponse("../frontend/dist/index.html")

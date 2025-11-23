from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .exceptions.handlers import create_exception_handlers
from .routers import battlelog, club, player, rankings, static
from .services.bs_service import shutdown_client, startup_client

load_dotenv()

app = FastAPI(title="BrawlDogg API", version="0.0.1")

app = FastAPI(
    title="BrawlDogg API",
    version="0.0.1",
    exception_handlers=create_exception_handlers(),
)

# --- CORS Configuration  ---
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# -----------------------------------------------

app.add_event_handler("startup", startup_client)
app.add_event_handler("shutdown", shutdown_client)

app.include_router(player.router, prefix="/api/v1", tags=["Player"])
app.include_router(club.router, prefix="/api/v1", tags=["Club"])
app.include_router(battlelog.router, prefix="/api/v1", tags=["Battle Log"])
app.include_router(rankings.router, prefix="/api/v1", tags=["Ranking"])
app.include_router(static.router, prefix="/api/v1", tags=["Static Data"])


@app.get("/")
async def root():
    return {"message": "BrawlDogg API is running"}

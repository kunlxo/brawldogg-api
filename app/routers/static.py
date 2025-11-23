from brawldogg.client import BrawlStarsClient
from brawldogg.models import Brawler, EventEntry, GameMode, PagingResponse
from fastapi import APIRouter, Depends, Path, Query

from ..services.bs_service import get_brawlstars_client

router = APIRouter(
    prefix="/static",
)


@router.get("/brawlers", response_model=PagingResponse[Brawler])
async def get_brawlers(
    limit: int = Query(
        100, ge=1, le=100, description="Max number of entries to return."
    ),
    after: str | None = Query(None, description="Marker for the next page of results."),
    before: str | None = Query(
        None, description="Marker for the previous page of results."
    ),
    bs_client: BrawlStarsClient = Depends(get_brawlstars_client),
):
    """
    Retrieves a list of all Brawlers and their details.
    """
    brawlers = await bs_client.get_brawlers(
        limit=limit,
        after=after,
        before=before,
    )
    return brawlers


@router.get("/brawlers/{brawler_id}", response_model=Brawler)
async def get_brawler(
    brawler_id: int = Path(description="Unique ID of the brawler (e.g., 16000000)"),
    bs_client: BrawlStarsClient = Depends(get_brawlstars_client),
):
    """
    Retrieves detailed information for a specific Brawler by ID.
    """

    brawler_data = await bs_client.get_brawler(brawler_id)
    return brawler_data


@router.get("/events/rotation", response_model=list[EventEntry])
async def get_current_events(
    bs_client: BrawlStarsClient = Depends(get_brawlstars_client),
):
    """
    Retrieves the currently active and upcoming game events.
    """
    events = await bs_client.get_current_events()
    return events


@router.get("/gamemodes", response_model=PagingResponse[GameMode])
async def get_gamemodes(
    limit: int = Query(
        100, ge=1, le=100, description="Max number of entries to return."
    ),
    after: str | None = Query(None, description="Marker for the next page of results."),
    before: str | None = Query(
        None, description="Marker for the previous page of results."
    ),
    bs_client: BrawlStarsClient = Depends(get_brawlstars_client),
):
    """
    Retrieves a list of all game modes.
    """
    gamemodes = await bs_client.get_gamemodes(
        limit=limit,
        after=after,
        before=before,
    )
    return gamemodes

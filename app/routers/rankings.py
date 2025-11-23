from brawldogg.client import BrawlStarsClient
from brawldogg.models import ClubRanking, PagingResponse, PlayerRanking
from fastapi import APIRouter, Depends, Path, Query

from ..services.bs_service import get_brawlstars_client

router = APIRouter(prefix="/rankings")


@router.get("/{country_code}/players", response_model=PagingResponse[PlayerRanking])
async def get_player_rankings(
    country_code: str = Path(description="Country code (e.g., 'RU') or 'global'"),
    limit: int = Query(
        20, ge=1, le=200, description="Max number of entries to return."
    ),
    after: str | None = Query(None, description="Marker for the next page of results."),
    before: str | None = Query(
        None, description="Marker for the previous page of results."
    ),
    bs_client: BrawlStarsClient = Depends(get_brawlstars_client),
):
    """
    Retrieves the top player rankings for a specific country or global.
    """

    rankings = await bs_client.get_player_rankings(
        country_code,
        limit=limit,
        after=after,
        before=before,
    )
    return rankings


@router.get("/{country_code}/clubs", response_model=PagingResponse[ClubRanking])
async def get_club_rankings(
    country_code: str = Path(description="Country code (e.g., 'RU') or 'global'"),
    limit: int = Query(
        200, ge=1, le=200, description="Max number of entries to return."
    ),
    after: str | None = Query(None, description="Marker for the next page of results."),
    before: str | None = Query(
        None, description="Marker for the previous page of results."
    ),
    bs_client: BrawlStarsClient = Depends(get_brawlstars_client),
):
    """
    Retrieves the top club rankings for a specific country or global.
    """

    rankings = await bs_client.get_club_rankings(
        country_code,
        limit=limit,
        after=after,
        before=before,
    )
    return rankings


@router.get(
    "/{country_code}/brawlers/{brawler_id}",
    response_model=PagingResponse[PlayerRanking],
)
async def get_brawler_rankings(
    country_code: str = Path(description="Country code (e.g., 'RU') or 'global'"),
    brawler_id: int = Path(description="Unique ID of the brawler (e.g., 16000000)"),
    limit: int = Query(
        200, ge=1, le=200, description="Max number of entries to return."
    ),
    after: str | None = Query(None, description="Marker for the next page of results."),
    before: str | None = Query(
        None, description="Marker for the previous page of results."
    ),
    bs_client: BrawlStarsClient = Depends(get_brawlstars_client),
):
    """
    Retrieves the top brawler rankings for a specific country or global.
    """

    rankings = await bs_client.get_brawler_rankings(
        brawler_id=brawler_id,
        country=country_code,
        limit=limit,
        after=after,
        before=before,
    )
    return rankings

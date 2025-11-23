from brawldogg.client import BrawlStarsClient
from brawldogg.models.player import Player
from fastapi import APIRouter, Depends

from ..services.bs_service import get_brawlstars_client

router = APIRouter(
    prefix="/players",
)


@router.get("/{player_tag}", response_model=Player)
async def get_player_data(
    player_tag: str,
    bs_client: BrawlStarsClient = Depends(get_brawlstars_client),
):
    """
    Retrieves detailed information for a specific player tag.
    """
    player_data = await bs_client.get_player(player_tag)
    return player_data

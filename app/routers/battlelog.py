from brawldogg.client import BrawlStarsClient
from brawldogg.models import BattleLogEntry, PagingResponse
from fastapi import APIRouter, Depends

from ..services.bs_service import get_brawlstars_client

router = APIRouter(
    prefix="/battlelogs",
)


@router.get("/{player_tag}", response_model=PagingResponse[BattleLogEntry])
async def get_player_battlelog(
    player_tag: str,
    bs_client: BrawlStarsClient = Depends(get_brawlstars_client),
):
    """
    Retrieves the recent battle log entries for a player.
    """
    battle_log = await bs_client.get_player_battlelog(player_tag)
    return battle_log

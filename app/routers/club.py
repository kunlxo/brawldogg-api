from brawldogg.client import BrawlStarsClient
from brawldogg.models import Club, ClubMember, PagingResponse
from fastapi import APIRouter, Depends, Query

from ..services.bs_service import get_brawlstars_client

router = APIRouter(
    prefix="/clubs",
)


@router.get("/{club_tag}", response_model=Club)
async def get_club_data(
    club_tag: str,
    bs_client: BrawlStarsClient = Depends(get_brawlstars_client),
):
    """
    Retrieves detailed information for a specific club tag.
    """
    club_data = await bs_client.get_club(club_tag)
    return club_data


@router.get("/{club_tag}/members", response_model=PagingResponse[ClubMember])
async def get_club_members_list(
    club_tag: str,
    limit: int = Query(30, ge=1, le=30, description="Max number of entries to return."),
    after: str | None = Query(None, description="Marker for the next page of results."),
    before: str | None = Query(
        None, description="Marker for the previous page of results."
    ),
    bs_client: BrawlStarsClient = Depends(get_brawlstars_client),
):
    """
    Retrieves the list of members for a specific club tag.
    """

    members = await bs_client.get_club_members(
        club_tag,
        limit=limit,
        after=after,
        before=before,
    )
    return members

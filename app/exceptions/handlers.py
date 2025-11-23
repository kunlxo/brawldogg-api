# from fastapi.responses import JSONResponse
# def create_exception_handlers():
#     """Returns a dictionary of custom exception types mapped to their handlers."""
#     async def http_exception_handler(request: Request, exc: BrawlDoggHTTPException):
#         """Handler for all specific BrawlDogg HTTP exceptions."""
#         return JSONResponse(
#             status_code=exc.status,
#             content={
#                 "detail": exc.reason,
#                 "message": exc.message,
#             },
#         )
#     return {
#         # 4xx Client Errors
#         NotFound: http_exception_handler,
#         BadRequest: http_exception_handler,
#         AccessDenied: http_exception_handler,  # 403
#         RateLimited: http_exception_handler,  # 429
#         # 5xx Server Errors
#         InternalServerError: http_exception_handler,  # 500
#         Unavailable: http_exception_handler,  # 503
#     }
from typing import Any, Callable, Coroutine, Type

from brawldogg.exceptions import (
    AccessDenied,
    BadRequest,
    InternalServerError,
    NotFound,
    RateLimited,
    Unavailable,
)
from brawldogg.exceptions import HTTPException as BrawlDoggHTTPException
from fastapi import Request
from fastapi.responses import JSONResponse, Response


def create_exception_handlers() -> dict[
    int | Type[Exception],
    Callable[[Request, Any], Coroutine[Any, Any, Response]],
]:
    """Returns a dictionary of custom exception types mapped to their handlers."""

    async def http_exception_handler(
        request: Request, exc: BrawlDoggHTTPException
    ) -> JSONResponse:
        """Handler for all specific BrawlDogg HTTP exceptions."""

        return JSONResponse(
            status_code=exc.status,
            content={
                "detail": exc.reason,
                "message": exc.message,
            },
        )

    return {
        NotFound: http_exception_handler,
        BadRequest: http_exception_handler,
        AccessDenied: http_exception_handler,
        RateLimited: http_exception_handler,
        InternalServerError: http_exception_handler,
        Unavailable: http_exception_handler,
    }

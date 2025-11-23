import os

from brawldogg.client import BrawlStarsClient

client_instance: BrawlStarsClient | None = None


# 1. Function to get the client (used as a dependency in routes)
async def get_brawlstars_client() -> BrawlStarsClient:
    """Returns the single, initialized BrawlStarsClient instance."""
    if client_instance is None:
        # In a real app, you'd load the token from environment variables (.env)
        raise RuntimeError("BrawlStarsClient not initialized.")
    return client_instance


# 2. Startup Function (runs once when the server starts)
async def startup_client():
    """Initializes the BrawlStarsClient, connecting to the external API."""
    global client_instance
    API_TOKEN = os.environ.get("BRAWL_STARS_TOKEN", "YOUR_FALLBACK_TOKEN")

    # Initialize your client with the token and recommended settings
    client_instance = BrawlStarsClient(token=API_TOKEN)
    print("BrawlStarsClient initialized.")


# 3. Shutdown Function (runs once when the server stops)
async def shutdown_client():
    """Closes the underlying HTTP session."""
    if client_instance:
        await client_instance.close()
        print("BrawlStarsClient session closed.")

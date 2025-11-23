# BrawlDogg API Wrapper

Containerized API service built with FastAPI on top of the brawldogg wrapper for Brawl Stars.

## Features

- **API Versioning:** Uses the `/api/v1` prefix for future scalability.  
- **Integrated Client:** Utilizes the custom `brawldogg` Python client for clean API interactions.  
- **Containerized:** Can be built and run using a standard `Dockerfile`.   
- **CORS Enabled:** Middleware configured to allow access from development frontend.

## Installation

### Option A: Local Development
```bash
# git clone <repo-url> && cd brawldogg-api
poetry install
export BRAWL_STARS_TOKEN="YOUR_API_KEY_HERE"
poetry run uvicorn server:app --reload --host 0.0.0.0 --port 8000
````

### Option B: Build & Run Using Dockerfile
```bash
docker build -t brawldogg-api .
docker run -d \
  -p 8000:8000 \
  -e BRAWL_STARS_TOKEN="YOUR_API_KEY_HERE" \
  brawldogg-api
```

## Configuration

The wrapper requires your Brawl Stars API key.

| Variable     | Description                                    | Required? |
| ------------ | ---------------------------------------------- | --------- |
| `BRAWL_STARS_TOKEN` | Your personal API key for the Brawl Stars API. | Yes       |


## API Endpoints

All routes are prefixed with `/api/v1`.

### Root
| Method | Route | Description | Query Params |
|--------|-------|-------------|--------------|
| GET    | `/`   | Check | - |

### Player
| Method | Route | Description | Query Params |
|--------|-------|-------------|--------------|
| GET    | `/players/{player_tag}` | Get player details | - |

### Battle Log
| Method | Route | Description | Query Params |
|--------|-------|-------------|--------------|
| GET    | `/battlelogs/{player_tag}` | Get recent battle logs | - |

### Club
| Method | Route | Description | Query Params |
|--------|-------|-------------|--------------|
| GET    | `/clubs/{club_tag}` | Get club details | - |
| GET    | `/clubs/{club_tag}/members` | Get club members | `limit`, `after`, `before` |

### Rankings
| Method | Route | Description | Query Params |
|--------|-------|-------------|--------------|
| GET    | `/rankings/{country_code}/players` | Top player rankings | `limit`, `after`, `before` |
| GET    | `/rankings/{country_code}/clubs` | Top club rankings | `limit`, `after`, `before` |
| GET    | `/rankings/{country_code}/brawlers/{brawler_id}` | Top brawler rankings | `limit`, `after`, `before` |

### Static Data
| Method | Route | Description | Query Params |
|--------|-------|-------------|--------------|
| GET    | `/static/brawlers` | List all brawlers | `limit`, `after`, `before` |
| GET    | `/static/brawlers/{brawler_id}` | Get brawler details | - |
| GET    | `/static/events/rotation` | Current/upcoming events | - |
| GET    | `/static/gamemodes` | List all game modes | `limit`, `after`, `before` |

### Example Request

```bash
curl -X 'GET' \
  'http://localhost:8000/api/v1/players/2GCJ0UR02' \
  -H 'accept: application/json'
```

### Example Usage in Frontend

```javascript
const playerTag = "2GCJ0UR02";
const response = await fetch(`http://localhost:8000/api/v1/players/${playerTag}`);
```

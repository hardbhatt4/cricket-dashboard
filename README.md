# IPL Cricket Dashboard
 
A single-page analytics dashboard for IPL ball-by-ball match data. Built with Vue (Vanilla CSS) on the frontend and FastAPI + Pandas on the backend.
 
---
 
## Features
 
- Season and team filters applied across the entire page
- KPI strip: matches played, runs scored, total sixes, total wickets
- Batting leaderboard: runs, average, strike rate, sixes
- Bowling leaderboard: wickets, economy, average, runs conceded
- Sortable tables with client-side column sorting
---
 
## Tech stack
 
| Layer    | Technology                        |
|----------|-----------------------------------|
| Frontend | Vue, Vanilla CSS                  |
| Backend  | FastAPI, Pandas, Uvicorn          |
| Data     | Ball-by-ball CSV                  |

## Local setup

The Vue frontend is built as a static HTML and served by FastAPI

### Backend
 
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
 
The Dashboard will be available at `http://localhost:8000`.
Interactive docs at `http://localhost:8000/docs`.


from pydantic import BaseModel


class MetaResponse(BaseModel):
    seasons: list[str]
    teams: list[str]


class BattingRow(BaseModel):
    player: str
    runs: int
    average: float | None
    strike_rate: float | None
    sixes: int


class BowlingRow(BaseModel):
    player: str
    wickets: int
    runs_conceded: int
    average: float | None
    economy: float | None


class KPIResponse(BaseModel):
    matches_played: int
    runs_scored: int
    total_sixes: int
    total_wickets: int

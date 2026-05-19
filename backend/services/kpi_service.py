from data_loader import get_data


def _apply_filters(df, season, team):
    """Filter the data for indicated season and team"""
    filtered_df = df.copy()
    if season is not None:
        filtered_df = filtered_df[filtered_df["season"] == season]
    if team is not None:
        # Entire matches where team played
        filtered_df = filtered_df[
            (filtered_df["batting_team"] == team)
            | (filtered_df["bowling_team"] == team)
        ]

    return filtered_df


def get_kpi(season: str | None, team: str | None) -> dict:
    """Return KPIs for selected season and team"""
    df = get_data()
    filtered_df = _apply_filters(df, season, team)
    matches_played = filtered_df["match_id"].nunique()
    runs_scored = filtered_df["runs_off_bat"].sum() + filtered_df["extras"].sum()
    total_sixes = len(filtered_df[filtered_df["runs_off_bat"] == 6])
    total_wickets = filtered_df["is_wicket"].sum()
    return {
        "matches_played": matches_played,
        "runs_scored": runs_scored,
        "total_sixes": total_sixes,
        "total_wickets": total_wickets,
    }

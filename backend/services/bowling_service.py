from .data_loader import get_data


def _apply_filters(df, season, team):
    """Filter the data for indicated season and team"""
    filtered_df = df.copy()
    if season is not None:
        filtered_df = filtered_df[filtered_df["season"] == season]
    if team is not None:
        # Entire matches where team played
        filtered_df = filtered_df[filtered_df["bowling_team"] == team]

    return filtered_df


def get_bowling_stats(season: str | None, team: str | None) -> list:
    """Return bowling stats for all players for selected season and team"""
    df = get_data()
    filtered_df = _apply_filters(df, season, team)
    bowling_df = filtered_df.groupby("bowler")[
        [
            "ball",
            "is_wicket",
            "wicket_type",
            "runs_off_bat",
            "wides",
            "noballs",
        ]
    ]
    bowling_stats = []
    for bowler, group in bowling_df:
        wickets = group[group["wicket_type"] != "run out"]["is_wicket"].sum()
        runs_conceded = (
            group["runs_off_bat"].sum() + group["wides"].sum() + group["noballs"].sum()
        )
        legal_balls = group[(group["wides"] == 0) & (group["noballs"] == 0)][
            "ball"
        ].count()
        if wickets != 0:
            average = round(runs_conceded / wickets, 2)
        else:
            average = None
        if legal_balls != 0:
            economy = round((runs_conceded / legal_balls) * 6, 2)
        else:
            economy = None
        bowling_stats.append(
            {
                "player": bowler,
                "wickets": wickets,
                "runs_conceded": runs_conceded,
                "average": average,
                "economy": economy,
            }
        )
    return bowling_stats

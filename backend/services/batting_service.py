from .data_loader import get_data


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


def get_batting_stats(season: str | None, team: str | None) -> list:
    """Return batting stats for all players for selected season and team"""
    df = get_data()
    filtered_df = _apply_filters(df, season, team)
    batting_df = filtered_df.groupby("striker")[
        ["runs_off_bat", "ball", "is_wicket", "player_dismissed", "wides"]
    ]
    batting_stats = []

    for batsman, group in batting_df:
        runs = group["runs_off_bat"].sum()
        dismissals = group[group["player_dismissed"] == batsman][
            "player_dismissed"
        ].count()
        if dismissals != 0:
            average = round(runs / dismissals, 2)
        else:
            average = None
        balls = group[group["wides"] == 0]["ball"].count()
        if balls != 0:
            strike_rate = round((runs / balls) * 100, 2)
        else:
            strike_rate = None
        sixes = group[group["runs_off_bat"] == 6]["runs_off_bat"].count()
        batting_stats.append(
            {
                "player": batsman,
                "runs": runs,
                "average": average,
                "strike_rate": strike_rate,
                "sixes": sixes,
            }
        )
    return batting_stats

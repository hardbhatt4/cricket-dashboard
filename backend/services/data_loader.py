import pandas as pd
from pathlib import Path

_df = None


def get_data() -> pd.DataFrame:
    """Load all files in data folder and combine into a dataframe"""
    global _df
    if _df is None:
        folder = Path(__file__).parent.parent.parent / "data"
        dfs = []
        for file in folder.iterdir():
            season_df = pd.read_csv(file, parse_dates=["start_date"])
            dfs.append(season_df)

        _df = pd.concat(dfs)
        _df.drop(["other_wicket_type", "other_player_dismissed"], axis=1, inplace=True)
        extras_cols = ["wides", "noballs", "byes", "legbyes", "penalty", "extras"]
        _df[extras_cols] = _df[extras_cols].fillna(0).astype(int)
        _df["is_wicket"] = _df["wicket_type"].notna().astype(int)

    return _df

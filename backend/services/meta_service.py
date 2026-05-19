from data_loader import get_data


def get_metadata() -> dict:
    """Return information about seasons and teams present in data"""
    df = get_data()
    metadata = {}
    metadata["seasons"] = list(df["season"].unique())
    metadata["teams"] = list(
        set(df["batting_team"].unique()) | set(df["bowling_team"].unique())
    )
    return metadata

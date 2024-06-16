import pandas as pd
from datetime import datetime, timedelta


def get_five_games(data, teamA, teamB=None):
    if teamB is None:
        filtered_games = data[
            ((data["home_team"] == teamA)) | ((data["away_team"] == teamA))
        ]
    else:
        filtered_games = data[
            ((data["home_team"] == teamA) & (data["away_team"] == teamB))
            | ((data["home_team"] == teamB) & (data["away_team"] == teamA))
        ]

    # Explicitly state that modyfing all rows is intentional
    filtered_games.loc[:, "date"] = pd.to_datetime(filtered_games["date"])

    filtered_games = filtered_games.sort_values(by="date", ascending=False)

    recent_10_games = filtered_games.head(10)

    current_date = datetime.now()
    twenty_years_ago = current_date - timedelta(days=365 * 20)

    # Filter out games without scores
    games_with_scores = recent_10_games.dropna(subset=["home_score", "away_score"])

    recent_games_with_scores = games_with_scores[
        games_with_scores["date"] > twenty_years_ago
    ].head(5)

    return recent_games_with_scores

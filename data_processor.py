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

    # Explicitly modify data row to datetime
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


def get_qualification_games(data, team):
    filtered_games = data[
        ((data["home_team"] == team) | (data["away_team"] == team))
        & (data["tournament"] == "UEFA Euro qualification")
    ]

    # Explicitly modify data row to datetime
    filtered_games.loc[:, "date"] = pd.to_datetime(filtered_games["date"])

    filtered_games = filtered_games.sort_values(by="date", ascending=False)
    two_years_ago = datetime.now() - timedelta(days=2 * 365)
    filtered_games = filtered_games[filtered_games["date"] > two_years_ago]

    return filtered_games


def get_top_goal_scorers(goals_data, team):
    goals_data.loc[:, "date"] = pd.to_datetime(goals_data["date"])

    two_years_ago = datetime.now() - timedelta(days=2 * 365)

    team_goals = goals_data[
        (goals_data["team"] == team)
        & (goals_data["date"] > two_years_ago)
    ]

    # Filter out own goals
    team_goals = team_goals[~team_goals['own_goal']]

    top_scorers = team_goals['scorer'].value_counts().head(5)

    return top_scorers

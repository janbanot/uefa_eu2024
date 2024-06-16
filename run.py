import pandas as pd
from data_processor import get_five_games

if __name__ == "__main__":
    file_path = "source/results.csv"
    data = pd.read_csv(file_path)

    PL = "Poland"
    NL = "Netherlands"

    poland_games = get_five_games(data, PL)
    netherlands_games = get_five_games(data, NL)
    together_games = get_five_games(data, PL, NL)

    print(together_games)

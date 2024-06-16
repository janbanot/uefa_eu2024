import os
from openai import OpenAI
import pandas as pd
from dotenv import load_dotenv
from data_processor import get_five_games, get_top_goal_scorers, get_qualification_games
from build_prompt import build_prompt


def send_query_to_openai(client, prompt, model="gpt-4o"):
    response = client.chat.completions.create(
        model=model, messages=[{"role": "system", "content": prompt}]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    load_dotenv()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    results_file_path = "source/results.csv"
    results_data = pd.read_csv(results_file_path)

    goals_file_path = "source/goalscorers.csv"
    goals_data = pd.read_csv(goals_file_path)

    teamA = "Poland"
    teamB = "Netherlands"

    teamA_games = get_five_games(results_data, teamA)
    teamA_quali_games = get_qualification_games(results_data, teamA)
    teamA_top_scorers = get_top_goal_scorers(goals_data, teamA)

    teamB_games = get_five_games(results_data, teamB)
    teamB_quali_games = get_qualification_games(results_data, teamB)
    teamB_top_scorers = get_top_goal_scorers(goals_data, teamB)

    head_to_head_games = get_five_games(results_data, teamA, teamB)

    prompt = build_prompt(
        teamA,
        teamA_games,
        teamA_quali_games,
        teamA_top_scorers,
        teamB,
        teamB_games,
        teamB_quali_games,
        teamB_top_scorers,
        head_to_head_games,
    )

    # print(prompt)

    response_text = send_query_to_openai(client, prompt)
    print(response_text)

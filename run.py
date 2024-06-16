import os
from openai import OpenAI
import pandas as pd
from dotenv import load_dotenv
from data_processor import get_five_games, get_qualification_games
from build_prompt import build_prompt


def send_query_to_openai(client, prompt, model="gpt-4-turbo"):
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

    additional_context = "That is teams first match of the Euro 2024 tournament. Lewandowski is injured"

    teamA_games = get_five_games(results_data, teamA)
    teamA_quali_games = get_qualification_games(results_data, teamA)

    teamB_games = get_five_games(results_data, teamB)
    teamB_quali_games = get_qualification_games(results_data, teamB)

    head_to_head_games = get_five_games(results_data, teamA, teamB)

    prompt = build_prompt(
        teamA,
        teamA_games,
        teamA_quali_games,
        teamB,
        teamB_games,
        teamB_quali_games,
        head_to_head_games,
        additional_context
    )

    response_text = send_query_to_openai(client, prompt)
    print(response_text)

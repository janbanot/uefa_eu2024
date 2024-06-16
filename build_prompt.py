def build_prompt(
    teamA,
    teamA_latest_games,
    teamA_quali_games,
    teamA_top_scorers,
    teamB,
    teamB_latest_games,
    teamB_quali_games,
    teamB_top_scorers,
    head_to_head_games,
):
    prompt = f"""
    Act as a footbal expert analyst. Provide analysis on the match between {teamA} and {teamB}.
    Carefully analyze the historical achievements of both teams. Take into consideration the following:

    {teamA} 5 recent games:
    {teamA_latest_games}

    {teamA} qualification games:
    {teamA_quali_games}

    {teamA} top goal scorers:
    {teamA_top_scorers}

    {teamB} 5 recent games:
    {teamB_latest_games}

    {teamB} qualification games:
    {teamB_quali_games}

    {teamB} top goal scorers:
    {teamB_top_scorers}

    Last 5 head-to-head games:
    {head_to_head_games}

    Analyze the data and provide the 3 most likely exact results with the probability level in percentage.
    Add information who will be likely to score the first goal.
    """
    return prompt

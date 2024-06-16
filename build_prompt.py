def build_prompt(
    teamA,
    teamA_latest_games,
    teamA_quali_games,
    teamB,
    teamB_latest_games,
    teamB_quali_games,
    head_to_head_games,
    additional_context=None,
):
    prompt = f"""
    Act as a footbal expert analyst. Provide analysis on the match between {teamA} and {teamB}.
    Carefully analyze the historical achievements of both teams.
    Take into consideration the following:

    {teamA} 5 recent games:
    {teamA_latest_games}

    {teamA} qualification games:
    {teamA_quali_games}

    {teamB} 5 recent games:
    {teamB_latest_games}

    {teamB} qualification games:
    {teamB_quali_games}

    Last 5 head-to-head games:
    {head_to_head_games}

    Additional context:
    {additional_context}

    Analyze the data and provide the 3 most likely exact results with the probability level in percentage.
    Be specific and provide short reasoning for each prediction.
    """
    return prompt

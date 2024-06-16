# Data source
https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017

## results.csv
results.csv includes the following columns:
- date - date of the match
- home_team - the name of the home team
- away_team - the name of the away team
- home_score - full-time home team score including extra time, not including penalty-shootouts
- away_score - full-time away team score including extra time, not including penalty-shootouts
- tournament - the name of the tournament
- city - the name of the city/town/administrative unit where the match was played
- country - the name of the country where the match was played
- neutral - TRUE/FALSE column indicating whether the match was played at a neutral venue

## shootouts.csv
shootouts.csv includes the following columns:
- date - date of the match
- home_team - the name of the home team
- away_team - the name of the away team
- winner - winner of the penalty-shootout
- first_shooter - the team that went first in the shootout

## goalscorers.csv
goalscorers.csv includes the following columns:
- date - date of the match
- home_team - the name of the home team
- away_team - the name of the away team
- team - name of the team scoring the goal
- scorer - name of the player scoring the goal
- own_goal - whether the goal was an own-goal
- penalty - whether the goal was a penalty

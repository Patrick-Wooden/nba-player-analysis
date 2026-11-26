from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import pandas as pd



def get_player_stats(name):
    """Lookup a player by name and return their per game stats by season"""
    results = players.find_players_by_full_name(name)

    if not results:
        raise ValueError(f"No player found named '{name}'")

    player_id = results[0]["id"]

    career = playercareerstats.PlayerCareerStats(player_id=player_id, timeout=60)

    df = career.get_data_frames()[0]

    per_game = {"PPG": "PTS", "APG": "AST", "RPG": "REB"}

    for new_col, source_col in per_game.items():
        df[new_col] = (df[source_col] / df["GP"]).round(1)

    columns = ["SEASON_ID", "TEAM_ABBREVIATION", "GP"] + list(per_game.keys())

    return df[columns]


if __name__ == "__main__":
    print(get_player_stats("LeBron James"))
    print(get_player_stats("Stephen Curry"))
    

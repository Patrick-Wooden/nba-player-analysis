from fastapi import FastAPI, HTTPException
from stats import get_player_stats


app = FastAPI()

@app.get("/players/{name}")
def player_stats(name: str):
    try:
        df = get_player_stats(name)
        
    except ValueError:
        raise HTTPException(status_code=404, detail=f"Player '{name}' does not exist")
    return df.to_dict(orient="records")
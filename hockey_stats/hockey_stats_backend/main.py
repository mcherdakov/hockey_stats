from fastapi import FastAPI, HTTPException
from playhouse.shortcuts import model_to_dict
from player import Player

app = FastAPI()


@app.get("/api/players")
def get_players(page: int = 0):
    all_players = Player.select(Player.id, Player.name).paginate(page, 100)
    all_players = [t.to_json() for t in all_players]
    return all_players


@app.get("/api/player")
def get_players(id: int = 0):
    player_by_id = Player.get_or_none(Player.id == id)
    if not player_by_id:
        raise HTTPException(status_code=400, detail="No player with such ID")
    return player_by_id.to_json()


@app.get("/api/search/players")
def get_players(s: str = None):
    if s is None:
        return []
    s = s.lower()
    s = s.split()
    result_query = Player.unicode_name.contains(s[0])
    for word in s:
        result_query = result_query & Player.unicode_name.contains(word)
    players = Player.select().where(result_query).limit(40)
    if not players:
        return []
    players = [t.to_json() for t in players]
    return players

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models import Player, Team, Prediction

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
    player_by_id = player_by_id.to_json()
    if not Prediction.get_or_none((Prediction.player_id == id)):
        player_by_id["has_prediction"] = False
    else:
        player_by_id["has_prediction"] = True
    return player_by_id


@app.get("/api/search/players")
def get_players(s: str = None):
    if s is None:
        return []
    s = s.lower()
    s = s.split()
    result_query = Player.unicode_name.contains(s[0])
    for word in s:
        result_query = result_query & Player.unicode_name.contains(word)
    players = Player.select().where(result_query).limit(50)
    if not players:
        return []
    json_players = []
    for t in players:
        player = t.to_json()
        if not Prediction.get_or_none((Prediction.player_id == t.id)):
            player["has_prediction"] = False
        else:
            player["has_prediction"] = True
        json_players.append(player)
    return json_players


@app.get("/api/teams")
def get_teams(page: int = 0):
    all_teams = Team.select(Team.id, Team.team_name).paginate(page, 100)
    all_teams = [t.to_json() for t in all_teams]
    return all_teams


@app.get("/api/team")
def get_teams(id: int = 0):
    team_by_id = Team.get_or_none(Team.id == id)
    if not team_by_id:
        raise HTTPException(status_code=400, detail="No team with such ID")
    return team_by_id.to_json()


@app.get("/api/search/teams")
def get_teams(s: str = None):
    if s is None:
        return []
    s = s.lower()
    s = s.split()
    result_query = Team.team_name.contains(s[0])
    for word in s:
        result_query = result_query & Team.team_name.contains(word)
    teams = Team.select().where(result_query).limit(40)
    if not teams:
        return []
    teams = [t.to_json() for t in teams]
    return teams


@app.get("/api/predict")
def get_predict(player_id: int = None, team_id: int = None):
    if player_id is None:
        raise HTTPException(status_code=400, detail="No player_id field")
    if team_id is None:
        raise HTTPException(status_code=400, detail="No team_id field")
    prediction = Prediction.get_or_none((Prediction.player_id == player_id) & (Prediction.team_id == team_id))
    if not prediction:
        raise HTTPException(status_code=404, detail="No prediction for such player_id and team_id")
    return prediction.to_json()

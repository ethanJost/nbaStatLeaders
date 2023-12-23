class Player:
    def __init__(self, name, position, age, team, games, min_played, per, ts, usg, ws, vorp):
        self.name = name
        self.position = position
        self.age = age
        self.team = team
        self.games = games
        self.min_played = min_played
        self.per = per
        self.ts = ts
        self.usg = usg
        self.ws = ws
        self.vorp = vorp
    
    def __repr__(self):
        return f"{self.name}\nPosition: {self.position}\nAge: {self.age}\nTeam: {self.team}\nGames Played: {self.games}\nMinutes Played: {self.min_played}\nAdvanced Statistics:\nPlayer Efficiency Rating = {self.per}\nTrue Shooting Percentage = {self.ts}\nUsage Percentage = {self.usg}\nWin Shares = {self.ws}\nVORP = {self.vorp}\n"
        
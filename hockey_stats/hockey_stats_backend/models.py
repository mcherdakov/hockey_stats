from peewee import (
    Model, PostgresqlDatabase, CharField, IntegerField
)
from playhouse.shortcuts import model_to_dict

db = PostgresqlDatabase('postgres', user='postgres', password='hockey',
                        host='db', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Player(BaseModel):
    name = CharField()
    unicode_name = CharField()
    nationality = CharField()
    youth_team = CharField()
    position = CharField()
    shoots = CharField()
    height = IntegerField()
    weight = IntegerField()
    age = IntegerField()

    def to_json(self):
        return model_to_dict(self)

    class Meta:
        db_table = 'player'


class Team(BaseModel):
    league_name = CharField()
    team_name = CharField()
    full_name = CharField()
    league_link = CharField()
    youth_team = CharField()
    position = CharField()
    shoots = CharField()
    year_founded = IntegerField()
    weight = IntegerField()
    age = IntegerField()

    def to_json(self):
        return model_to_dict(self)

    class Meta:
        db_table = 'team'

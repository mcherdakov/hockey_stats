from peewee import *
from playhouse.shortcuts import model_to_dict

db = PostgresqlDatabase('hockey', user='doadmin', password='rdxo4w05qb3vq10l',
                        host='db-postgresql-fra1-36671-do-user-4768937-0.db.ondigitalocean.com', port=25060)


class BaseModel(Model):
    class Meta:
        database = db


class Player(BaseModel):
    name = CharField()
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

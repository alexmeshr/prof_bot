from peewee import *
from config import DATABASE

db = SqliteDatabase(DATABASE)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField()
    join_date = DateTimeField()
    score = IntegerField()


class Point(BaseModel):
    question = CharField()
    wr_answ = CharField()
    r_answ = CharField()
    score = IntegerField()

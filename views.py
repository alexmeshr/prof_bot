from models import *

db = SqliteDatabase(DATABASE)


def create_tables():
    with db:
        db.create_tables([User, Point])


def register(name, date):
    new_user = User(username=name, join_date=date, score=0)
    new_user.save()
    return new_user


def get_points():
    query = (Point.select().order_by(Point.score))
    # query = (User.select().order_by(User.score))
    return query


def setpoint(this_score, quest, wrong, right):
    new_point = Point(question=quest, wr_answ=wrong, r_answ=right, score=this_score)
    new_point.save()


def clear_users():
    for usr in User.select():
        usr.delete_instance()

# setpoint(10,"Сколько лет длилась столетняя война?","96,100,106","116")
# setpoint(10,"Сколько ног у сороконожки?","40","не 40")
# setpoint(10,"Какой вид додзюцу получил Боруто?","риннеган,бьякуган,шариган","джооган")
# setpoint(10,"Джинчурики какого зверя является Наруто?","однохвостый, шестихвостый, десятихвостый","девятихвостый")

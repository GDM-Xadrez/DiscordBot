# Commands to read data from user_db.json
import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'user_db.json')) as f:
    db = json.load(f)

def is_user(user):
    try:
        db["users"][user]
        return True
    except:
        return False

def get_user(user):
    if not is_user(user): return False

    return db["users"][user]

def get_xp(user):
    if not is_user(user): return False

    return db["users"][user]["xp"]

def get_tournaments(user):
    if not is_user(user): return False

    return db["users"][user]["tournaments"]

def get_lichess_acc(user):
    if not is_user(user): return False

    return db["users"][user]["lichess_acc"]


def save_data(db):
    with open(os.path.join(__location__, 'user_db.json'), 'w') as outfile:
        json.dump(db, outfile)


def create_user(username):
    db["user"].append({
        username:{
            "xp": 0,
            "tournaments":{
            },
            "lichess_acc": ""           
            }
        })

    save_data(db)

def change_lichess_account(user, account):
    if not is_user(user): return False

    else:
        db["user"]["lichess_acc"] = account

        save_data(db)


def change_xp(user, amount):
    if not is_user(user): return False

    else:
        db["user"]["xp"] = amount

        save_data(db)


def add_tournament(user, date, pos):
    if not is_user(user): return False

    else:
        db["user"]["tournaments"].append({
            date: pos
        })

        save_data(db)



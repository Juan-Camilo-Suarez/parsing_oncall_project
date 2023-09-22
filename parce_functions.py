import json
from datetime import datetime, timedelta


def team_parse_json(team):
    team_data = {
        "name": team['name'],
        "scheduling_timezone": team['scheduling_timezone'],
        "email": team['email'],
        "slack_channel": team['slack_channel'],
    }
    team_json = json.dumps(team_data)
    return team_json


def user_parse_json(user):
    user_data = {
        "name": user['name']
    }
    user_json = json.dumps(user_data)
    return user_json


def user_update_parse_json(user):
    user_data = {
        "contacts": {
            "call": user['phone_number'],
            "email": user['email'],
        },
        "name": user['name'],
        "full_name": user['full_name'],
    }

    user_json = json.dumps(user_data)
    return user_json


def convertion_start_end(fecha_str):
    try:
        fecha_obj = datetime.strptime(fecha_str, "%d/%m/%Y")
        marca_tiempo_unix = fecha_obj.timestamp()
        marca_tiempo_unix_aumentado = (fecha_obj + timedelta(minutes=30)).timestamp()
        return int(marca_tiempo_unix), int(marca_tiempo_unix_aumentado)
    except ValueError:
        return None, None

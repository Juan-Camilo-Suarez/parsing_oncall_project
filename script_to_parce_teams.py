import json

import yaml

from endpoints_conecctions import RequesOncall
from parce_functions import team_parse_json, user_parse_json, convertion_start_end, user_update_parse_json

session_oncall = RequesOncall('root', 'admin')

with open('teams.yaml', 'r') as file:
    data = yaml.safe_load(file)

for team in data['teams']:
    session_oncall.create_teams(team_parse_json(team))

    # # Iterate through the users in the team
    for user in team['users']:

        session_oncall.create_user(user_parse_json(user))
        session_oncall.update_user(user)
        session_oncall.add_user_to_team(team['name'], user_parse_json(user))

        # Iterate through the duty schedule for the user
        # for duty_entry in user['duty']:
        #     start, end = convertion_start_end(str(duty_entry['date']))
        #     duty_data = {
        #         "start": start,
        #         "end": end,
        #         "user": user['name'],
        #         "team": team['name'],
        #         "role": duty_entry['role']
        #     }
        #     duty_json = json.dumps(duty_data)
        #     session_oncall.create_event(duty_json)

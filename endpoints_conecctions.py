import json
import requests

from parce_functions import user_update_parse_json, Response


class RequesOncall:
    PATH_ONCALL = "http://juancamilosuarez3.fvds.ru:8080"

    def __init__(self, username, password):
        self.csrf_token, self.cookies = self.login(username, password)
        self.headers = {
            'content-type': 'application/json',
            'X-Csrf-Token': self.csrf_token
        }

    def login(self, username, password):
        login_url = self.PATH_ONCALL + "/login"
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        session = requests.Session()
        user_data = {
            "username": username,
            "password": password
        }
        try:
            response = session.post(login_url, user_data, head)
            csrf_token = response.json()['csrf_token']
            cookies = session.cookies.get_dict()
            if csrf_token is not None and cookies is not None:
                print("Login Successful I got data")
                return csrf_token, cookies
            else:
                print("status 200, but Login Data Failed")

        except Exception as e:
            print("An error occurred during login:", str(e))

    def create_teams(self, team: json):
        teams_url = self.PATH_ONCALL + "/api/v0/teams"
        try:
            create_team = requests.post(teams_url, data=team, headers=self.headers, cookies=self.cookies)
            if create_team.status_code == 201:
                print("Team Created Success")
            else:
                print("no teams found")
        except Exception as e:
            print("An error occurred during create team:", str(e))

    def create_user(self, user):
        users_url = self.PATH_ONCALL + "/api/v0/users"
        try:
            create_user = requests.post(users_url, data=user, headers=self.headers, cookies=self.cookies)
            if create_user.status_code == 201:
                print("User Created Success")
            else:
                print("no user found")
        except Exception as e:
            print("An error occurred during create user:", str(e))

    def update_user(self, user):
        users_url = self.PATH_ONCALL + f"/api/v0/users/{user['name']}"
        try:
            update_user = requests.put(users_url, data=user_update_parse_json(user), headers=self.headers,
                                       cookies=self.cookies)
            if update_user.status_code == 204:
                print("User Update Success")
            else:
                print("no user found for update")
        except Exception as e:
            print("An error occurred during create user:", str(e))

    def add_user_to_team(self, team, user):
        add_user_team_url = self.PATH_ONCALL + f'/api/v0/teams/{team}/users'
        try:
            add_user_team = requests.post(add_user_team_url, data=user, headers=self.headers, cookies=self.cookies)
            if add_user_team.status_code == 201:
                print("User added to team Success")
            else:
                print("no team found for user")
        except Exception as e:
            print("An error occurred User NOT added to team:", str(e))

    def create_event(self, duty):
        users_url = self.PATH_ONCALL + "/api/v0/events"
        try:
            create_event = requests.post(users_url, data=duty, headers=self.headers, cookies=self.cookies)
            print(create_event.status_code)
            print(create_event.content)
            if create_event.status_code == 201:
                print("Event Created Success")
            else:
                print("no event found")
        except Exception as e:
            print("An error occurred during create event:", str(e))

    def get_teams(self):
        teams_url = self.PATH_ONCALL + "/api/v0/teams"
        try:
            response = requests.get(teams_url, headers=self.headers, cookies=self.cookies)
            if response.status_code == 200:
                teams = response.json()
                print("Teams:")
                for team in teams:
                    print(team)
            else:
                print("No teams found")
        except Exception as e:
            print("An error occurred while getting teams:", str(e))

    def get_summary(self, team):
        endpoint = f"{self.PATH_ONCALL}/api/v0/teams/{team}/summary"
        try:
            response = requests.get(endpoint, headers=self.headers, cookies=self.cookies)
            if response.status_code == 200:
                response_data = response.json()
                current_summary = response_data.get("current", {})
                result = Response(current_summary, response.url, response.elapsed.total_seconds(), response.status_code)
                print(result)
                return result
            else:
                print("Error fetching summary")
        except Exception as e:
            print("An error occurred while getting summary:", str(e))
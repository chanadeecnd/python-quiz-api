import requests


class API:

    def __init__(self, url):
        self.url = url

    def get_json_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            json_data = response.json()
            return json_data
        except requests.exceptions.RequestException as e:
            print("Error", e)
            return None

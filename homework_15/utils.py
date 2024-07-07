import json

import requests


def download_file(file_name: str, file_url: str):
    with open(file_name, mode='bw') as file:
        response = requests.get(file_url)
        file.write(response.content)


def download_json(file_name: str, file_url: str):
    with open(file_name, mode='w') as file:
        response = requests.get(file_url)
        json.dump(response.json(), file, indent=4)

import requests
import src.config as cfg
from src.services.user_info.yandex_user_info import YandexUserInfo


def get_user_yandex_info(token: str):
    headers = {
        "Accept": "application/json",
        "Authorization": "", # TODO Вернуть токен пользователя
    }
    response = requests.get("https://cloud-api.yandex.net/v1/disk", headers=headers)
    print(response.json())
    return YandexUserInfo(response.json())


def get_all_files_from_disk(token: str):
    headers = {
        "Accept": "application/json",
        "Authorization": "", # TODO Вернуть токен пользователя
    }
    response = requests.get(
        "https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2F",
        headers=headers,
    )
    print(response.json())


get_all_files_from_disk("s")

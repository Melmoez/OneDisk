import requests

from src.services.authorization.YandexOAuth import YandexOAuth


class YandexUserInfo(YandexOAuth):
    def __init__(self, app_token, secret_token):
        super().__init__(app_token, secret_token)
        self.app_token = app_token
        # self.max_file_size = yandex_response['max_file_size']
        # self.total_space = yandex_response['total_space']
        # self.used_space = yandex_response['used_space']
        # self.user_name = yandex_response['user']['display_name']

    def get_user_yandex_info(self):
        headers = {"Accept": "application/json", "Authorization": self.get_user_token()}
        response = requests.get("https://cloud-api.yandex.net/v1/disk", headers=headers)

        return YandexUserInfo(response.json())

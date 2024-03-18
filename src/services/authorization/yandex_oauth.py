import webbrowser
import requests

class YandexOAuth:
    def __init__(self, app_token, secret_token):
        self.app_token = app_token
        self.secret_token = secret_token

    def get_authorization_code(self):
        webbrowser.open(f'https://oauth.yandex.ru/authorize?response_type=code&client_id={self.app_token}', new=1)
        return input('Введите код подтверждения: ')

    def get_user_token(self, authorization_code):
        data = {
            'grant_type': 'authorization_code',
            'code': authorization_code,
            'client_id': self.app_token,
            'client_secret': self.secret_token
        }
        response = requests.post('https://oauth.yandex.ru/token', data=data)
        response_data = response.json()
        return response_data
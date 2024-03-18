from src.services.authorization.yandex_oauth import YandexOAuth
from src import config

def get_token():
        app_token = config.app_settings['OAUTH']
        secret_token = config.app_settings['CLIENTSECRET']

        oauth_client = YandexOAuth(app_token, secret_token)
        authorization_code = oauth_client.get_authorization_code()
        user_data = oauth_client.get_user_token(authorization_code)

        config.user_data = user_data
        access_token = user_data['access_token']
        print(f'Полученный токен доступа: {access_token}')
        return access_token
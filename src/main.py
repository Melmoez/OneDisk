from src import config
from src.services.authorization import user_token


if __name__ == "__main__":
    print(config.user_data)
    user_token.get_token()

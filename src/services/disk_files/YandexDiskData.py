from src.services.authorization.YandexOAuth import YandexOAuth
import requests
import threading
import json


class YandexDiskData(YandexOAuth):
    def __init__(self, app_token, secret_token):
        super().__init__(app_token, secret_token)
        self.headers = {
            "Accept": "application/json",
            "Authorization": "",
        }  # не забыть вернуть аксесс токен
        self._data = dict()

    @property
    def data(self):
        return self._data

    def read_all_files(self, path: str = "disk:/"):
        folder_data = dict()
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        data = requests.get(url, headers=self.headers, params={"path": path}).json()
        data = data["_embedded"].get("items", None)
        a = threading.Thread()
        a.start()
        if data == None:
            return folder_data
        for i in data:
            if i["type"] == "dir":
                folder_data[i["name"]] = self.read_all_files(i["path"])
            else:
                folder_data[i["name"]] = i
        a.join()
        self._data = folder_data
        return self.data




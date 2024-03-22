import json
import os
import threading


class SyncFolderData:
    def __init__(self, path:str):
        self.path = path
        self._data = dict()

    @property
    def data(self):
        return self._data

    def get_file_info(self, file_path:str):
        if os.path.isfile(file_path):
            file_info = {
                'file_name': os.path.basename(file_path),
                'file_size_bytes': os.path.getsize(file_path),
                'file_creation_time': os.path.getctime(file_path),
                'file_modification_time': os.path.getmtime(file_path),
                'file_access_time': os.path.getatime(file_path),
                'file_permissions': os.stat(file_path).st_mode
            }
            return file_info


    def read_all_files(self, path:str = None):
        if path == None:
            path = self.path
        folder_data = dict()
        thread = threading.Thread()
        thread.start()
        data = os.listdir(path)
        for i in data:
            file_name = i[:i.rfind('.')]
            file_path = os.path.join(path, i)
            if os.path.isdir(file_path):
                folder_data[file_name] = self.read_all_files(file_path)
            else:
                folder_data[file_name] = self.get_file_info(file_path)
        thread.join()
        self._data = folder_data
        return folder_data

a = SyncFolderData('/home/melmoes/onedrive_sync')
print(json.dumps(a.read_all_files(), indent=4))
import requests


class YaUploader:
    base_host = 'https://cloud-api.yandex.net:443'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Authorization': f'OAuth {self.token}'}

    def _get_upload_link(self, path):
        uri = '/v1/disk/resources/upload'
        request_url = self.base_host + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        print(response.json())
        return response.json()['href']

    def upload(self, file_path: str):
        yandex_path = f'/{file_path.split("/")[-1]}'
        upload_url = self._get_upload_link(yandex_path)
        response = requests.put(upload_url, data=open(file_path, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
            print('Успех')


if __name__ == '__main__':
    path_to_file = 'F:/fuck.txt'
    token = 'y0_AgAAAAAiKjK1AADLWwAAAADWfZKpr-nFuuQFSGCezUy2_d5pJLtaMAQ'
    uploader = YaUploader(token)
    uploader.upload(path_to_file)

import requests


class APIClient:
    session = requests.session()

    def __init__(self, host_endpoint, timeout):
        self.host_endpoint = host_endpoint
        self.timeout = timeout

    def get(self, path, *params):
        params_list = "&".join(params)
        resp = self.session.get(self.host_endpoint + path + params_list, timeout=self.timeout)
        response = {'status_code': resp.status_code, 'body': resp.json()}
        return response

    def post(self, path, **kwargs):
        payload = kwargs.get('payload', None)
        files = kwargs.get('files', None)
        resp = self.session.post(
            self.host_endpoint + path, json=payload, files=files, timeout=self.timeout
        )
        response = {'status_code': resp.status_code, 'body': resp.json()}
        return response

    def put(self, path, **kwargs):
        payload = kwargs.get('payload', None)
        resp = self.session.put(
            self.host_endpoint + path, json=payload, timeout=self.timeout
        )
        response = {'status_code': resp.status_code, 'body': resp.json()}
        return response

    def delete(self, path):
        resp = self.session.delete(self.host_endpoint + path, timeout=self.timeout)
        response = {'status_code': resp.status_code, 'body': resp.json()}
        return response

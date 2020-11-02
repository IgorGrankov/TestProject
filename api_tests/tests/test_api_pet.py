import pytest
import json
import unittest

from api_tests.client.api_client import APIClient

class TestAPIPet(unittest.TestCase):
    host = 'https://petstore.swagger.io/v2/'
    timeout = 60

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.api_client = APIClient(self.host, self.timeout)

    def test_post_new_pet(self):
        payload = open('api_tests/data/create_pet.json', 'rb').read()
        response = self.api_client.post(path="pet/", payload=(json.loads(payload)))
        assert response['body']['category']['name'] == 'doggie'
        assert response['body']['name'] == 'doggie'
        assert response['body']['status'] == 'available'
        assert response['status_code'] == 200

    def test_post_new_pet_invalid(self):
        payload = open('api_tests/data/invalid.json', 'rb').read()
        response = self.api_client.post(path="pet/", payload=(json.loads(payload)))
        assert response['status_code'] == 405

    def test_post_new_pet_without_data(self):
        response = self.api_client.post(path="pet/")
        assert response['status_code'] == 415

    def test_post_update_pet(self):
        self.create_test_pet()

        response = self.api_client.post(path="pet/123?name=doggo&status=pending")
        assert response['status_code'] == 200

        response_updated = self.api_client.get(path="pet/123")
        assert response_updated['status_code'] == 200
        assert response_updated['body']['name'] == 'doggo'
        assert response_updated['body']['status'] == 'pending'

    def test_post_update_pet_invalid(self):
        self.create_test_pet()

        response = self.api_client.post(path="pet/123?status=1$@")
        assert response['status_code'] == 405

    def test_post_update_non_existing_pet(self):
        self.create_test_pet()

        response = self.api_client.post(path="pet/325?name=doggo&status=pending")
        assert response['status_code'] == 404

    def test_post_pet_uploadImage(self):
        self.create_test_pet()

        file = {'file': open('api_tests/data/test.jpg', 'rb')}
        response = self.api_client.post(path="pet/123/uploadImage", files=file)
        assert response['status_code'] == 200

    def test_post_pet_uploadImage_without_file(self):
        self.create_test_pet()

        file = {'file': open('api_tests/data/test.jpg', 'rb')}
        response = self.api_client.post(path="", files=file)
        assert response['status_code'] == 415

    def test_post_pet_uploadImage_wrong_file(self):
        self.create_test_pet()

        file = {'file': open('api_tests/data/update_invalid_id.json', 'rb')}
        response = self.api_client.post(path="pet/123/uploadImage", files=file)
        assert response['status_code'] == 415

    def test_get_pet(self):
        self.create_test_pet()

        response = self.api_client.get(path="pet/123")
        assert response['status_code'] == 200

    def test_get_pet_without_id(self):
        self.create_test_pet()

        response = self.api_client.get(path="pet/")
        assert response['status_code'] == 500

    def test_get_pet_non_existing_id(self):
        self.create_test_pet()

        response = self.api_client.get(path="pet/100")
        assert response['status_code'] == 404

    def test_get_pet_invalid_id(self):
        self.create_test_pet()

        response = self.api_client.get(path="pet/abc")
        assert response['status_code'] == 400

    def test_get_pet_by_status(self):
        self.create_test_pet()

        response = self.api_client.get("pet/findByStatus?", "status=available")
        assert response['status_code'] == 200

    def test_put_pet(self):
        self.create_test_pet()

        payload = open('api_tests/data/update_pet.json', 'rb').read()
        response = self.api_client.put(path="pet/", payload=(json.loads(payload)))
        assert response['body']['category']['name'] == 'doggo'
        assert response['body']['name'] == 'doggo'
        assert response['body']['status'] == 'pending'
        assert response['status_code'] == 200

    def test_put_invalid_id_pet(self):
        payload = open('api_tests/data/update_invalid_id.json', 'rb').read()
        response = self.api_client.put(path="pet/", payload=(json.loads(payload)))
        assert response['status_code'] == 400

    def test_put_invalid_json_pet(self):
        payload = open('api_tests/data/invalid.json', 'rb').read()
        response = self.api_client.put(path="pet/", payload=(json.loads(payload)))
        assert response['status_code'] == 405

    def test_put_non_existing_id_pet(self):
        payload = open('api_tests/data/update_non_existing_pet.json', 'rb').read()
        response = self.api_client.put(path="pet/", payload=(json.loads(payload)))
        assert response['status_code'] == 404

    def test_put_without_body_pet(self):
        response = self.api_client.put(path="pet/")

        assert response['status_code'] == 415

    def test_delete_pet(self):
        self.create_test_pet()

        response = self.api_client.delete(path="pet/123")
        assert response['status_code'] == 200

    def test_delete_non_existing_pet(self):
        self.create_test_pet()

        response = self.api_client.delete(path="pet/100")
        assert response['status_code'] == 404

    def test_delete_without_id_pet(self):
        self.create_test_pet()

        response = self.api_client.delete(path="pet/")
        assert response['status_code'] == 500

    def test_delete_invalid_id_pet(self):
        self.create_test_pet()

        response = self.api_client.delete(path="pet/abc")
        assert response['status_code'] == 400

    def create_test_pet(self):
        payload = open('api_tests/data/create_pet.json', 'rb').read()
        response = self.api_client.post(path="pet/", payload=(json.loads(payload)))
        assert response['status_code'] == 200





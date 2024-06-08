from locust import task, HttpUser, constant
from assertpy import assert_that


class Regres(HttpUser):
    host = "https://reqres.in/"
    

    @task
    def test_put(self):
        payload = {
    "name": "morpheus",
    "job": "zion resident",
    "updatedAt": "2024-06-08T13:03:38.912Z"
    }

        req = self.client.post("api/users", json=payload)
        print(req.json())
       
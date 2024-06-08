from locust import task, HttpUser, constant
from assertpy import assert_that


class Regres(HttpUser):
    host = "https://reqres.in/"
    

    @task
    def test_post(self):
        payload = {
            "name": "morpheus",
            "job": "zion resident",
            "updatedAt": "2024-06-08T13:03:38.912Z"
        }

        req = self.client.put("api/users/2", json=payload)
        print(req.json())
       
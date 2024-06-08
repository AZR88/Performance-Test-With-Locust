from locust import task, HttpUser, constant
from assertpy import assert_that


class Regres(HttpUser):
    host = "https://reqres.in/"
    

    @task
    def test_post(self):
        payload = {
            "name":"azr",
            "job":"SDET"
        }

        req = self.client.post("api/users", json=payload)
        print(req.json())
       
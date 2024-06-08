from locust import task, HttpUser, constant
from assertpy import assert_that


class Regres(HttpUser):
    host = "https://reqres.in/"
    wait_time = constant(1)
    

    @task
    def test_delete(self):
        payload = {
            "name": "morpheus",
            "job": "zion resident",
            "updatedAt": "2024-06-08T13:03:38.912Z"
        }

        req = self.client.delete("api/users/2")
        print(req.status_code)
       
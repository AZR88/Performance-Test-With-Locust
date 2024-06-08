from locust import task, HttpUser, constant
from assertpy import assert_that


class Regres(HttpUser):
    host = "https://reqres.in/"
    

    @task
    def test_get(self):
        response = self.client.get("api/users?page=2")
        assert_that(response.status_code).is_equal_to(200)

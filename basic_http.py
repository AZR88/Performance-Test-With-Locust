from locust import task, HttpUser, constant
from assertpy import assert_that


class Regres(HttpUser):
    host = "https://reqres.in/"
    

    @task
    def test_get(self):
        req = self.client.get("api/users?page=2")

        #assertion status code
        assert_that(req.status_code).is_equal_to(200)

        #assertion Tipe Data
        assert_that(req.json().get("page")).is_type_of(int)

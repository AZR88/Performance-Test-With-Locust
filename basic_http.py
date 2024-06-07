from locust import task, HttpUser, constant

class regres(HttpUser):
    host = "https://reqres.in/"
    self_time = constant(2)

    @task
    def test_get(self):
        self.client.get("api/users?page=2")
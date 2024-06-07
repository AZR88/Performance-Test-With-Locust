from locust import User, task

class MyFirstTest(User):

    @task
    def test1(self):
        print("pengujian ke :1")

    @task
    def test2(self):
        print("pengujian ke :2")
from locust import task,constant, HttpUser, SequentialTaskSet


#def generateToken():
#    token = "token....."
#    return token

class APi_task(SequentialTaskSet):
    
    

    @task
    def test_get(self):
         
         #head = {
         #    "authorization" = generateToken()
         #}

         req = self.client.get("api/users?page=2")
         print("test ke : GET")
    
    
    @task
    def test_post(self):
        payload = {
            "name":"azr",
            "job":"SDET"
        },
        req = self.client.post("api/users", json=payload)
        print("test ke : POST")
        
    
    @task
    def test_patch(self):
        playload = {
        "name": "morpheus",
        "job": "zion resident"
        }
        req = self.client.patch("api/users/2")
        print("test ke : PATCH")

    @task
    def test_put(self):
        payload = {
            "name": "morpheus",
            "job": "zion resident"
        }

        req = self.client.put("api/users/2", json=payload)
        print("test ke : PUT")
    
    @task
    def test_delete(self):
        req = self.client.delete("api/users/2")
        print("test ke : DELETE")
    
    
       

class setUpTest(HttpUser):
    host = "https://reqres.in/"
    wait_time = constant(1)
    tasks = [APi_task]
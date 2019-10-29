import requests
import json 

class PowerMessageClient:
  def __init__(self, host, username, password):
    self.host = host
    self.token = self.login( username, password)["token"]

  def login(self, u, p):
    payload = {
        "username": u,
        "password": p
    }
    payload = json.dumps(payload)
    headers = {'content-type': 'application/json'}

    response = requests.request("POST", 
        self.host + "login", data=payload, headers=headers)

    return json.loads(response.text)
  
  ## USER RELATED
  def get_all_users(self):
    response = requests.request("GET",
       self.host  + "auth/user/all", 
       data="", cookies={"token": self.token})
    return json.loads(response.text)

  def add_new_user(self, input_json):
    payload = json.dumps(input_json)
    headers = {'content-type': 'application/json'}
    response = requests.request("POST", 
        self.host  + "auth/user/create",
        data=payload, headers=headers, cookies={"token": self.token})

  def drop_user(self, idz):
    payload = json.dumps({"ID": idz})
    headers = {'content-type': 'application/json'}
    response = requests.request("POST", 
        self.host  + "auth/user/delete",
        data=payload, headers=headers, cookies={"token": self.token})
    
    
  # SEND MESSAGE
  def send_message(self, uid, text):
    payload = json.dumps({
        "userid": uid,
        "message": text
    })
    headers = {'content-type': 'application/json'}
    response = requests.request("POST", 
        self.host  + "auth/external/message",
        data=payload, headers=headers, cookies={"token": self.token})

    
    return json.loads(response.text)
        
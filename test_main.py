from fastapi.testclient import TestClient #TestClinet is class
# import app object from our exisitng project main.py file
from main import app 
# test route path


## two tests,
## steps tobe takes and assertion to be made
def test_route_path():
    # a simulated client to send req to fastapi
    client = TestClient(app=app)
    # request send from browser client
    # response sends get req to specific endpoint
    response = client.get("/")
    # check if status_code == 200
    assert response.status_code == 200
    # convert reponse into json and match
    assert response.json() == {"Hello":'World'}


def test_piaic_des():
    client = TestClient(app=app)
    # agr ye route ata hai to 
    response = client.get("/piaic/")
    # uska response
    assert response.status_code == 200
    # convert reponse into json and match
    assert response.json() == {"organization":"piaic"}  

from fastapi import FastAPI
# def main():
#     print("Hello from fastapi!")


# if __name__ == "__main__":
#     main()
 
# craeting object of FastAPI class
# this object responsile for everything done from fastapi
# this will be our server , adn right now
app  = FastAPI()

# our decorator function
# decorator "@" is extra 

# user req fro get, it searches for route and execute and return results
@app.get("/")# againt api adres  
def index():
    return {"Hello": "World"}

#anyone who route
@app.get("/piaic/")
def piaic():
    return {"organization":"piaic"}


# this will be our server , adn right now this is providing two servies
# route one which after getting root adress says hellow world
# and after root folder wiritng piaic we get somthing organization

#server adress in bold 127.0.0.1:8000 and paste it in chrome and run: so our app object is responsile for it 
# cleint or computer 1 is our chrome which requested via ip adress and this unvicorn server from vs code 
# is computer 2 which said hello world

# to acess second service 127.0.0.1:8000/piaic

#also we can change client for example chrome to edge.hence we can have million of api
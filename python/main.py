from fastapi import FastAPI

app = FastAPI() 


@app.get("/")
def read_root(): 
    return {"Hello":"World"}

@app.get("/hello")
def return_hello(): 
    return "Hello, world!"

@app.get("/items/{item_id}") 
def read_item(item_id):
    return {"id":item_id}
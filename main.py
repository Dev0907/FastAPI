from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "World"}

@app.post("/")
def create_item(name:str, price:float):
    return {"message": "Item created", "name": name, "price": price}


@app.put("/")
def update_item(name:str, price:float):
    return {"message": "Item updated", "name": name, "price": price}


@app.delete("/")
def delete_item(name:str):
    return {"message": "Item deleted", "name": name}

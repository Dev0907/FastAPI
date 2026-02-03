from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "World"}

# @app.post("/")
# def create_item(name:str, price:float):
#     return {"message": "Item created", "name": name, "price": price}


# @app.put("/")
# def update_item(name:str, price:float):
#     return {"message": "Item updated", "name": name, "price": price}


# @app.delete("/")
# def delete_item(name:str):
#     return {"message": "Item deleted", "name": name}
# @app.get("/items/{id}")
# def get_items(id:int, name:str | None = None):
#     return {"message": "Items retrieved", "id": id, "name": name}



# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     price: float
#     tax: float | None = None

# @app.get("/items/")
# def create_item(item: Item):
#     return item

from fastapi import UploadFile, File, HTTPException

ALLOWED_TYPES = ["image/png", "image/jpeg"]
MAX_SIZE = 2 * 1024 * 1024  # 2MB

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Invalid file type")

    content = await file.read()
    if len(content) > MAX_SIZE:
        raise HTTPException(status_code=400, detail="File too large")

    return {"filename": file.filename, "size": len(content)}
import sql.connect
def get_connection():
    return sql.connecter.connect(
        location="localhost",
        database="test",
        user="root",
        password=""
    )
from fastapi import FastAPI, HTTPException
from db import get_connection

app = FastAPI()

@app.get("/users")
def get_users():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        return {
            "success": True,
            "data": rows
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()


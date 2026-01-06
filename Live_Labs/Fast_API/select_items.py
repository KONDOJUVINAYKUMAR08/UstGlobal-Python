from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/items/")
def get_item(name: str, price: int):
    return {
        "item_name": name,
        "item_price": price
    }
 
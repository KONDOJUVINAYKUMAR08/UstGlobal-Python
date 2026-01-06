from fastapi import FastAPI
from pydantic import BaseModel
 
app = FastAPI()
 
class Sales(BaseModel):
    product: str
    quantity: int
    price: float
 
@app.post("/sales/")
def create_sales(sales: Sales):
    total = sales.quantity * sales.price
    return {
        "product": sales.product,
        "total_amount": total
    }


"""in order run the file:
set this folder to path and type command:  """
# python -m uvicorn {filename}:app --reload
# for this file
# python -m uvicorn f2:app --reload

# http://127.0.0.1:8000/docs
 
 
# Click POST /sales/
 
# Click Try it out
 
# Enter:
 
# {
#   "product": "Laptop",
#   "quantity": 2,
#   "price": 50000
# }
 
 
# Click Execute
 
# ✅ Response:
 
# {
#   "product": "Laptop",
#   "total_amount": 100000
# }
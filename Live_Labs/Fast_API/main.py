from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/sales")
def get_sales():
    return {"total_sales": 50000}

"""in order run the file:
set this folder to path and type command:  """
# python -m uvicorn {filename}:app --reload
# for this file
# python -m uvicorn main:app --reload
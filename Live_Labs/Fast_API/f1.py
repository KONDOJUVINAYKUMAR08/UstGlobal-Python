from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}

"""in order run the file:
set this folder to path and type command:  """
# python -m uvicorn {filename}:app --reload
# for this file
# python -m uvicorn f1:app --reload
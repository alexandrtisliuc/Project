from fastapi import FastAPI

app = FastAPI()

@app.post("/home")
def read_root():
    return {"Hello": "World"}

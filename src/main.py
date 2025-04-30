from fastapi import FastAPI

app = FastAPI()

@app.get('/home')
async def read_root():
    return {'Hello': 'World'}

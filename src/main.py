from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"My Github: https://github.com/Laamhohuy"}
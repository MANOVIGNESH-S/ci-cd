from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/hello")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}

#hello
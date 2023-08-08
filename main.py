import uvicorn
from fastapi import FastAPI

from src.routes import contacts, auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(contacts.router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", reload=True, log_level="info")

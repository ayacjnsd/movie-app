def main():
    print("Hello from server!")


if __name__ == "__main__":
    main()
from fastapi import FastAPI

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
from config import settings


@app.get("/")
def home():
    return {"message": "Hello World!"}

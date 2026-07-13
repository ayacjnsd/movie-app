def main():
    print("Hello from server!")


if __name__ == "__main__":
    main()
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World!"}

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "Hello World"}


@app.get("/echo/{message}")
def echo(message: str, query: str = None):
    return {"message": message, "query": query}

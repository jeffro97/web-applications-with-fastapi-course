import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get("/")
def index():
    content = """

    <h1>Hello - FastAPI Testing </h1>
    <div>Fake app lives here</div>

    """
    response = fastapi.responses.HTMLResponse(content)
    return response


if __name__ == "__main__":
    # noinspection PyTypeChecker
    uvicorn.run(app)

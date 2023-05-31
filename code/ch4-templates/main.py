import fastapi
import fastapi_chameleon
import uvicorn
from fastapi_chameleon import template

app = fastapi.FastAPI()

fastapi_chameleon.global_init("code\\ch4-templates\\templates")


@app.get("/")
@template(template_file="index.html")
def index():
    return {"user_name": "Jeffro"}


if __name__ == "__main__":
    # noinspection PyTypeChecker
    uvicorn.run(app)

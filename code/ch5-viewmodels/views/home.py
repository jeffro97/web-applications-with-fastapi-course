import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get("/")
# Can use HTML, but chameleon reads .pt files if nothing is given.
# Example:  @template(template_file='home/index.html')
@template()
def index():
    return {
        "package_count": 274_999,
        "release_count": 2_945_123,
        "user_count": 3_987,
        "packages": [
            {"id": "fastapi", "summary": "Web framework"},
            {"id": "uvicorn", "summary": "ASGI Server"},
            {"id": "httpx", "summary": "Request for async world"},
        ],
    }


@router.get("/about")
@template()
# If add about.pt into 'templates' directory, chameleon will auto find file.
def about():
    return {}

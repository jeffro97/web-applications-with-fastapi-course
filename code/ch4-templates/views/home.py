import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get("/")
@template()
def index(user: str = "anonyomus"):
    return {
        'package_count': 274_000,
        'release_count':2_234_847,
        'user_count': 73_893,
        'packages': [
            {'id': 'fastapi',  'summary': 'A web framework'},
            {'id':'uvicorn',  'summary': 'ASGI server'},
            {'id':'httpx',  'summary': 'requests for an async world'},
        ]
    }


@router.get("/about")
@template()
def about():
    return {}

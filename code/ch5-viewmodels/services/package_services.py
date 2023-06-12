from typing import List


def release_count() -> int:
    return 2_234_847

def package_count() -> int:
    return 274_000

def latest_packages(limit:int=5) -> List:
    return [
            {'id': 'fastapi',  'summary': 'A web framework'},
            {'id':'uvicorn',  'summary': 'ASGI server'},
            {'id':'httpx',  'summary': 'requests for an async world'},
        ][:limit]
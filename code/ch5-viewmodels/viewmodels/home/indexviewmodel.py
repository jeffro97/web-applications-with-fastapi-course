from starlette.requests import Request
from viewmodels.shared.viewmodel import ViewModelBase


class  IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.package_count: int = 1
        self.release_count: int = 2
        self.user_count: int = 3
        self.packages: List = []
        # {
        # 'package_count': 274_000,
        # 'release_count':2_234_847,
        # 'user_count': 73_893,
        # 'packages': [
        #     {'id': 'fastapi',  'summary': 'A web framework'},
        #     {'id':'uvicorn',  'summary': 'ASGI server'},
        #     {'id':'httpx',  'summary': 'requests for an async world'},
        # ]
        # }
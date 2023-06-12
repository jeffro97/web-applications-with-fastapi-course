from typing import List

from services import package_services, user_service
from starlette.requests import Request
from viewmodels.shared.viewmodel import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.release_count: int = package_services.release_count()
        self.user_count: int = user_service.user_count()
        self.package_count: int = package_services.package_count()
        self.packages: List = package_services.latest_packages(limit=5)
import fastapi
from fastapi_chameleon import template
from requests import Request
from viewmodels.accounts.account_view_model import AccountViewModel
from viewmodels.accounts.login_view_model import LoginViewModel
from viewmodels.accounts.register_view_model import RegisterViewModel

router = fastapi.APIRouter()


@router.get("/account")
def index(request: Request):
    vm = AccountViewModel
    return vm.to_dict


@router.get("/account/register")
def index(request: Request):
    vm = RegisterViewModel
    return vm.to_dict


@router.get("/account/login")
def index(request: Request):
    vm = LoginViewModel
    return vm.to_dict


@router.get("/account/logout")
def index(request: Request):
    return {}

from fastapi_chameleon import template
import fastapi

router = fastapi.APIRouter()
@router.get('/')
# Can use HTML, but chameleon reads .pt files if nothing is given.
# Example:  @template(template_file='home/index.html')
@template()
def index(user: str = 'Anon-O-moose'):
    return {
        'username': user
    }

@router.get('/about')
def about():
    return {}
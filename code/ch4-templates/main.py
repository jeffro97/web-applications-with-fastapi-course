"""
DOC String:
FastAPI Course
"""
import fastapi
import uvicorn
import fastapi_chameleon
from fastapi_chameleon import template

app = fastapi.FastAPI()
fastapi_chameleon.global_init('templates')


@app.get('/')
@template(template_file='index.html')
def index(user: str = 'Anon-O-moose'):
    return {
        'username': user
    }

@app.get('/')
def about():
    return {}

@app.get('/account')
def index():
    return {}

@app.get('/account/login')
def login():
    return {}

@app.get('/account/logout')
def logout():
    return {}


if __name__ == '__main__':
    uvicorn.run(app)
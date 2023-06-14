"""
DOC String:
FastAPI Course
"""
import fastapi
import uvicorn
import fastapi_chameleon
from starlette.staticfiles import StaticFiles

from views import home, account, packages

app = fastapi.FastAPI()


def main():
    """
    Main function to run app. First run configure, then run uvicorn to start up web services.
    """
    configure()
    uvicorn.run(app, host='127.0.0.1', port=8000)


def configure():
    """
    Function to run configuration for  templates and routes
    """
    configure_templates()
    configure_route()


def configure_templates():
    """
    Function to initialize templates directory.
    """
    fastapi_chameleon.global_init('templates')


def configure_route():
    """
    Function to configure routes to various views/templates.
    """
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


if __name__ == '__main__':
    main()
else:
    configure()

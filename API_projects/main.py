from fastapi import FastAPI
from core.config import settings

# app = FastAPI(title= settings.PROJECT_NAME, version=settings.PROJECT_VERSION)


# @app.get("/")
# def home():
#     return {"message":"home"}


# @app.get("/contact")
# def contact():
#     return {"message":"contact page"}


# @app.get("/about")
# def about():
#     return {"message":"about page"}    

# @app.get("/service")
# def service():
#     return {"message":"service page"}

from apis.app_router import page_router
from db.base import Base
from db.session import engine

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title= settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    # crearte table
    create_tables()
    return app

def include_router(app):
    app.include_router(page_router)

app=start_application()
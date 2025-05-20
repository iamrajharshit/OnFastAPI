from fastapi import APIRouter

page_router = APIRouter()

@page_router.get("/")
async def home():
    return {"message":"We are at home page"}

@page_router.get("/about")
async def about():
    return {"message":"We are at about page"}

@page_router.get("/service")
async def service():
    return {"message":"Enjoy the service"}
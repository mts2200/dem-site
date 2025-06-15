from fastapi import APIRouter
from app.site.controller import router as site_controller

def get_router() -> APIRouter:
    app_router = APIRouter(prefix="")
    routers = [site_controller]
    
    for router in routers:
        app_router.include_router(router)
        
    return app_router

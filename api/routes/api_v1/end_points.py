from fastapi import APIRouter

from api.posts.api import router as posts_router

api_router = APIRouter()

include_api = api_router.include_router
routers = (
    (posts_router, "posts", "posts"),
)

for router_item in routers:
    router, prefix, tag = router_item

    if tag:
        include_api(router, prefix=f"/{prefix}", tags=[tag])
    else:
        include_api(router, prefix=f"/{prefix}")

from fastapi import APIRouter, Depends
from fastapi import status as http_status

from api.core.models import StatusMessage
from api.posts.dependencies import get_posts_crud
from api.posts.models import UserPostIn, UserPosts
from api.posts.services import PostsService

router = APIRouter()


@router.post(
    "",
    response_model=UserPosts,
    status_code=http_status.HTTP_201_CREATED
)
async def create_new_posts(
        data: UserPostIn,
        posts_service: PostsService = Depends(get_posts_crud)
):
    post = await posts_service.create(data=data)

    return post


@router.get(
    "/{post_id}",
    response_model=UserPosts,
    status_code=http_status.HTTP_200_OK
)
async def get_post_by_uuid(
        post_id: int,
        posts_service: PostsService = Depends(get_posts_crud)
):
    post = await posts_service.get(post_id=post_id)

    return post


@router.patch(
    "/{post_id}",
    response_model=UserPosts,
    status_code=http_status.HTTP_200_OK
)
async def patch_post_by_uuid(
        post_id: int,
        data: UserPostIn,
        posts_service: PostsService = Depends(get_posts_crud)
):
    post = await posts_service.patch(post_id=post_id, data=data)

    return post


@router.delete(
    "/{post_id}",
    response_model=StatusMessage,
    status_code=http_status.HTTP_200_OK
)
async def delete_post_by_uuid(
        post_id: int,
        posts_service: PostsService = Depends(get_posts_crud)
):
    status = await posts_service.delete(post_id=post_id)

    return {"status": status, "message": "The hero has been deleted!"}

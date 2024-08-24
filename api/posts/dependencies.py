from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.core.db import get_async_session
from api.posts.services import PostsService


async def get_posts_crud(
        session: AsyncSession = Depends(get_async_session)
) -> PostsService:
    return PostsService(session=session)

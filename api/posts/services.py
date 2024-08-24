from fastapi import APIRouter, HTTPException, status as http_status
from sqlalchemy import select, delete
from sqlmodel.ext.asyncio.session import AsyncSession

from api.posts.models import UserPostIn, UserPosts

posts = APIRouter()


class PostsService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: UserPostIn) -> UserPosts:
        values = data.model_dump()
        post = UserPosts(**values)
        self.session.add(post)
        await self.session.commit()
        await self.session.refresh(post)

        return post

    async def get(self, post_id: int) -> UserPosts:
        statement = select(UserPosts).where(UserPosts.id == post_id)
        results = await self.session.execute(statement=statement)
        post = results.scalar_one_or_none()  # type: UserPosts | None

        if post is None:
            raise HTTPException(
                status_code=http_status.HTTP_404_NOT_FOUND,
                detail="The post hasn't been found!"
            )

        return post

    async def patch(self, post_id: int, data: UserPostIn) -> UserPosts:
        post = await self.get(post_id=post_id)
        values = data.dict(exclude_unset=True)

        for k, v in values.items():
            setattr(post, k, v)

        self.session.add(post)
        await self.session.commit()
        await self.session.refresh(post)

        return post

    async def delete(self, post_id: int) -> bool:
        statement = delete(UserPosts).where(UserPosts.id == post_id)
        await self.session.execute(statement=statement)
        await self.session.commit()

        return True

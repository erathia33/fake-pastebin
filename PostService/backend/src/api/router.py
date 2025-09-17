from fastapi import APIRouter

from .dependencies import SessionDep

from typing import Annotated

from schemas import PostSchema

from models import PostModel


router = APIRouter(prefix="/postservice")

@router.get("/")
async def get_main_page():
    pass

@router.post("/posts")
async def create_post(post: PostSchema, session: SessionDep):
    try:
        post = PostModel(
            author = post.author,
            title = post.title,
            content = post.content
        )
        session.add(post)
        await session.commit()
    except:
        await session.rollback()
        raise
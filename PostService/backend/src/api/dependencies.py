from fastapi import Depends

from database import get_db

from sqlalchemy.ext.asyncio import AsyncSession

from typing import Annotated

SessionDep = Annotated[AsyncSession, Depends(get_db)]

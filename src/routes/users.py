from fastapi import APIRouter, Depends, status, UploadFile, File, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import cloudinary
import cloudinary.uploader
from starlette.background import BackgroundTasks

from src.conf import messages
from src.database.db import get_db
from src.database.models import User
from src.repository import users as repository_users
from src.services.auth import auth_service
from src.conf.config import config
from src.schemas import UserResponseSchema, RequestEmail, ResetPasswordSchema
from src.services.email import send_reset_password_email

router = APIRouter(prefix="/users", tags=["users"])

cloudinary.config(
    cloud_name=config.cloudinary_name,
    api_key=config.cloudinary_api_key,
    api_secret=config.cloudinary_api_secret,
    secure=True,
)


@router.get("/me/", response_model=UserResponseSchema)
async def read_users_me(current_user: User = Depends(auth_service.get_current_user)):
    return current_user


@router.patch("/avatar", response_model=UserResponseSchema)
async def update_avatar_user(
    file: UploadFile = File(),
    current_user: User = Depends(auth_service.get_current_user),
    db: AsyncSession = Depends(get_db),
):
    r = cloudinary.uploader.upload(
        file.file, public_id=f"ContactAPP/{current_user.username}", overwrite=True
    )

    src_url = cloudinary.CloudinaryImage(f"NotesApp/{current_user.username}").build_url(
        width=250, height=250, crop="fill", version=r.get("version")
    )
    user = await repository_users.update_avatar(current_user.email, src_url, db)
    return user


@router.post("/reset_password_email")
async def reset_password_email(
    body: RequestEmail,
    background_tasks: BackgroundTasks,
    request: Request,
    db: AsyncSession = Depends(get_db),
):
    user = await repository_users.get_user_by_email(body.email, db)
    background_tasks.add_task(
        send_reset_password_email, user.email, user.username, request.base_url
    )
    return {"message": messages.PASSWORD_RESET_EMAIL_SUCCESS}


@router.post("/reset_password/{token}")
async def reset_password(
    token: str, body: ResetPasswordSchema, db: AsyncSession = Depends(get_db)
):
    email = await auth_service.get_email_from_token(token)
    user = await repository_users.get_user_by_email(email, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=messages.USER_NOT_FOUND)

    hashed_password = auth_service.get_password_hash(body.new_password)
    await repository_users.update_user_password(user, hashed_password, db)

    return {"message": messages.PASSWORD_RESET_SUCCESS}
from typing import List

from fastapi import APIRouter, HTTPException, Depends, status, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.database.models import User
from src.schemas import ContactResponseSchema, ContactSchema

from src.repository import contacts as repository_contacts
from src.services.auth import auth_service

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/", response_model=List[ContactResponseSchema])
async def get_contacts(
    limit: int = Query(10, ge=10, le=500),
    offset: int = Query(0, ge=0, le=200),
    db: AsyncSession = Depends(get_db),
    user: User = Depends(auth_service.get_current_user),
):
    contacts = await repository_contacts.get_contacts(limit, offset, user, db)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponseSchema)
async def get_contact(
    contact_id: int = Path(ge=1),
    db: AsyncSession = Depends(get_db),
    user: User = Depends(auth_service.get_current_user),
):
    contact = await repository_contacts.get_contact(contact_id, user, db)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="NOT FOUND",
        )
    return contact


@router.post(
    "/", response_model=ContactResponseSchema, status_code=status.HTTP_201_CREATED
)
async def create_contact(
    body: ContactSchema,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(auth_service.get_current_user),
):
    contact = await repository_contacts.create_contact(body, user, db)
    return contact


@router.put("/{contact_id}", response_model=ContactResponseSchema)
async def update_contact(
    body: ContactSchema,
    contact_id: int = Path(ge=1),
    db: AsyncSession = Depends(get_db),
    user: User = Depends(auth_service.get_current_user),
):
    contact = await repository_contacts.update_contact(contact_id, body, user, db)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="NOT FOUND",
        )
    return contact


@router.delete("/{contact_id}", response_model=ContactResponseSchema)
async def delete_contact(
    contact_id: int = Path(ge=1),
    db: AsyncSession = Depends(get_db),
    user: User = Depends(auth_service.get_current_user),
):
    contact = await repository_contacts.remove_contact(contact_id, user, db)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="NOT FOUND",
        )
    return contact


@router.get("/search/{contact_value}", response_model=List[ContactResponseSchema])
async def get_contacts_by_field(
    contact_value: str,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(auth_service.get_current_user),
):
    contacts = await repository_contacts.get_by_field(contact_value, user, db)
    return contacts


@router.get("/birthday/next-week", response_model=List[ContactResponseSchema])
async def get_birthday_next_week(
    db: AsyncSession = Depends(get_db),
    user: User = Depends(auth_service.get_current_user),
):
    contacts = await repository_contacts.birthday_week_contacts(user, db)
    return contacts

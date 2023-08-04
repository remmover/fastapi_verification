from datetime import datetime, timedelta

from sqlalchemy import select, extract, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Contact
from src.schemas import ContactSchema


async def get_contacts(limit: int, offset: int, db: AsyncSession):
    sq = select(Contact).offset(offset).limit(limit)
    contacts = await db.execute(sq)
    return contacts.scalars().all()


async def get_contact(contact_id: int, db: AsyncSession):
    sq = select(Contact).filter_by(id=contact_id)
    contact = await db.execute(sq)
    return contact.scalar_one_or_none()


async def create_contact(body: ContactSchema, db: AsyncSession):
    contact = Contact(name=body.name, surname=body.surname, email=body.email, number=body.number, bd_date=body.bd_date,
                      additional_data=body.additional_data)
    db.add(contact)
    await db.commit()
    await db.refresh(contact)
    return contact


async def update_contact(contact_id: int, body: ContactSchema, db: AsyncSession):
    sq = select(Contact).filter_by(id=contact_id)
    result = await db.execute(sq)
    contact = result.scalar_one_or_none()
    if contact:
        contact.name = body.name
        contact.surname = body.surname
        contact.email = body.email
        contact.number = body.number
        contact.bd_date = body.bd_date
        contact.additional_data = body.additional_data
        await db.commit()
        await db.refresh(contact)
    return contact


async def remove_contact(contact_id: int, db: AsyncSession):
    sq = select(Contact).filter_by(id=contact_id)
    result = await db.execute(sq)
    contact = result.scalar_one_or_none()
    if contact:
        await db.delete(contact)
        await db.commit()
    return contact


async def get_by_field(contact_value: str, db: AsyncSession):
    sq = select(Contact).filter(
        (func.lower(Contact.name) == contact_value.lower()) | (func.lower(Contact.surname) == contact_value.lower()) | (
                    Contact.email == contact_value)
    )
    contact = await db.execute(sq)
    return contact.scalars()


async def birthday_week_contacts(db: AsyncSession):
    today = datetime.today()
    next_week = today + timedelta(days=7)

    sq = select(Contact).filter(
        extract('month', Contact.bd_date).between(today.month, next_week.month),
        extract('day', Contact.bd_date).between(today.day, next_week.day)
    )

    contacts = await db.execute(sq)

    return contacts.scalars().all()

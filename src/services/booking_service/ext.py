async def get_available_staff(db_session, repository):
    return await repository.get_available_staff(db_session)

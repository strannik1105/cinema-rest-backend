class UserService:

    @staticmethod
    async def get_all_users(repository, session):
        return await repository.get_all(session)

    @staticmethod
    async def get_user_by_name(repository, name, session):
        pass

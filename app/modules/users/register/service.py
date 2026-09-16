from app.modules.users.register.repository import UserRepository


class UserService:
    def __init__(self,repo:UserRepository):
        self.repo=repo
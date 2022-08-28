from typing import List, NoReturn

from pydantic import UUID4
from starlite import Controller, Partial, get, post, put, patch, delete

from my_app.models.user import User


class UserController(Controller):
    path = "/users"

    @post()
    async def create_user(self, data: User) -> User:
        return {"error": "implementation in progress"}

    @get()
    async def list_users(self) -> List[User]:
        return {"error": "implementation in progress"}

    @patch(path="/{user_id:uuid}")
    async def partial_update_user(self, user_id: UUID4, data: Partial[User]) -> User:
        return {"error": "implementation in progress"}

    @put(path="/{user_id:uuid}")
    async def update_user(self, user_id: UUID4, data: User) -> User:
        return {"error": "implementation in progress"}

    @get(path="/{user_id:uuid}")
    async def get_user(self, user_id: UUID4) -> User:
        return {"error": "implementation in progress"}

    @delete(path="/{user_id:uuid}")
    async def delete_user(self, user_id: UUID4) -> None:
        return {"error": "implementation in progress"}

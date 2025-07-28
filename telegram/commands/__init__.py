from .add_user import AddUser
from .del_user import DelUser


class Commands(
    AddUser,
    DelUser
):
    ...
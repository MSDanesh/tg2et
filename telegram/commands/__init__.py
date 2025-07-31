from .add_user import AddUser
from .del_user import DelUser
from .add_channel import AddChannel
from .del_channel import DelChannel


class Commands(
    AddUser,
    DelUser,
    AddChannel,
    DelChannel,
):
    ...
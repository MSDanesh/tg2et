from .user import UserMethods
from .post import PostMethods
from .channel import ChannelMethods


class Methods(
    UserMethods,
    PostMethods,
    ChannelMethods,
):
    pass
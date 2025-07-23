from typing import Generator

from pyeitaa.raw.types.updates_t import Updates
from pyeitaa.raw.types.update_message_id import UpdateMessageID


class ParseMessage:
    def get_message_id(self, updates: Updates) -> Generator[int, None, None]:
        for update in updates.updates:
            if isinstance(update, UpdateMessageID):
                yield update.id
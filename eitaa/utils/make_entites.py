from pyrogram.enums.message_entity_type import MessageEntityType
from pyrogram.types.messages_and_media.message_entity import MessageEntity

from pyeitaa.raw.types import (
    MessageEntityBankCard,
    MessageEntityBlockquote,
    MessageEntityBold,
    MessageEntityBotCommand,
    MessageEntityCashtag,
    MessageEntityCode,
    MessageEntityEmail,
    MessageEntityHashtag,
    MessageEntityItalic,
    MessageEntityMention,
    MessageEntityMentionName,
    MessageEntityPhone,
    MessageEntityPre,
    MessageEntityStrike,
    MessageEntityTextUrl,
    MessageEntityUnderline,
    MessageEntityUnknown,
    MessageEntityUrl
)


normal_types_table = {
    MessageEntityType.MENTION: MessageEntityMention,
    MessageEntityType.HASHTAG: MessageEntityHashtag,
    MessageEntityType.CASHTAG: MessageEntityCashtag,
    MessageEntityType.BOT_COMMAND: MessageEntityBotCommand,
    MessageEntityType.URL: MessageEntityUrl,
    MessageEntityType.EMAIL: MessageEntityEmail,
    MessageEntityType.PHONE_NUMBER: MessageEntityPhone,
    MessageEntityType.BOLD: MessageEntityBold,
    MessageEntityType.ITALIC: MessageEntityItalic,
    MessageEntityType.UNDERLINE: MessageEntityUnderline,
    MessageEntityType.STRIKETHROUGH: MessageEntityStrike,
    MessageEntityType.CODE: MessageEntityCode,
    MessageEntityType.BLOCKQUOTE: MessageEntityBlockquote,
    MessageEntityType.BANK_CARD: MessageEntityBankCard,
    MessageEntityType.UNKNOWN: MessageEntityUnknown
}

abnormal_types_table = {
    MessageEntityType.PRE: lambda entity: MessageEntityPre(offset=entity.offset, length=entity.length, language=entity.language),
    MessageEntityType.TEXT_LINK: lambda entity: MessageEntityTextUrl(offset=entity.offset, length=entity.length, url=entity.url),
    MessageEntityType.TEXT_MENTION: lambda entity: MessageEntityMentionName(offset=entity.offset, length=entity.length, user_id=entity.user.id),
}

supported_types_table = set(normal_types_table) | set(abnormal_types_table)


class MakeEntites:
    def make_entities(self, entities: list[MessageEntity] = None):
        if entities is None:
            return None

        return [
            normal_types_table[entity.type](
                offset=entity.offset,
                length=entity.offset
            )
            if entity.type in normal_types_table else abnormal_types_table[entity.type](entity)
            for entity in entities
            if entity.type in supported_types_table
        ]
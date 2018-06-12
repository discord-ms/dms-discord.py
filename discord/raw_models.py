# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2015-2018 Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

class RawMessageDeleteEvent:
    """Represents the event payload for a :func:`on_raw_message_delete` event.

    Attributes
    ------------
    channel_id: :class:`int`
        The channel ID where the deletion took place.
    guild_id: Optional[:class:`int`]
        The guild ID where the deletion took place, if applicable.
    message_id: :class:`int`
        The message ID that got deleted.
    """

    __slots__ = ('message_id', 'channel_id', 'guild_id')

    def __init__(self, data):
        self.message_id = int(data['id'])
        self.channel_id = int(data['channel_id'])

        try:
            self.guild_id = int(data['guild_id'])
        except KeyError:
            self.guild_id = None

class RawBulkMessageDeleteEvent:
    """Represents the event payload for a :func:`on_raw_bulk_message_delete` event.

    Attributes
    -----------
    message_ids: Set[:class:`int`]
        A :class:`set` of the message IDs that were deleted.
    channel_id: :class:`int`
        The channel ID where the message got deleted.
    guild_id: Optional[:class:`int`]
        The guild ID where the message got deleted, if applicable.
    """

    __slots__ = ('message_ids', 'channel_id', 'guild_id')

    def __init__(self, data):
        self.message_ids = { int(x) for x in data.get('ids', []) }
        self.channel_id = int(data['channel_id'])

        try:
            self.guild_id = int(data['guild_id'])
        except KeyError:
            self.guild_id = None

class RawMessageUpdateEvent:
    """Represents the payload for a :func:`on_raw_message_edit` event.

    Attributes
    -----------
    message_id: :class:`int`
        The message ID that got updated.
    data: :class:`dict`
        The raw data given by the
        `gateway <https://discordapp.com/developers/docs/topics/gateway#message-update>`_
    """

    __slots__ = ('message_id', 'data')

    def __init__(self, data):
        self.message_id = int(data['id'])
        self.data = data

class RawReactionActionEvent:
    """Represents the payload for a :func:`on_raw_reaction_add` or
    :func:`on_raw_reaction_remove` event.

    Attributes
    -----------
    message_id: :class:`int`
        The message ID that got or lost a reaction.
    user_id: :class:`int`
        The user ID who added or removed the reaction.
    channel_id: :class:`int`
        The channel ID where the reaction got added or removed.
    guild_id: Optional[:class:`int`]
        The guild ID where the reaction got added or removed, if applicable.
    emoji: :class:`PartialEmoji`
        The custom or unicode emoji being used.
    """

    __slots__ = ('message_id', 'user_id', 'channel_id', 'guild_id', 'emoji')

    def __init__(self, data, emoji):
        self.message_id = int(data['message_id'])
        self.channel_id = int(data['channel_id'])
        self.user_id = int(data['user_id'])
        self.emoji = emoji

        try:
            self.guild_id = int(data['guild_id'])
        except KeyError:
            self.guild_id = None

class RawReactionClearEvent:
    """Represents the payload for a :func:`on_raw_reaction_clear` event.

    Attributes
    -----------
    message_id: :class:`int`
        The message ID that got its reactions cleared.
    channel_id: :class:`int`
        The channel ID where the reactions got cleared.
    guild_id: Optional[:class:`int`]
        The guild ID where the reactions got cleared.
    """

    __slots__ = ('message_id', 'channel_id', 'guild_id')

    def __init__(self, data):
        self.message_id = int(data['message_id'])
        self.channel_id = int(data['channel_id'])

        try:
            self.guild_id = int(data['guild_id'])
        except KeyError:
            self.guild_id = None
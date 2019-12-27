from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from yandex_music import Client

from yandex_music import YandexMusicObject


class Ratings(YandexMusicObject):
    def __init__(self,
                 week,
                 month,
                 day=None,
                 client: Optional['Client'] = None,
                 **kwargs) -> None:
        self.week = week
        self.month = month

        self.day = day

        self.client = client
        self._id_attrs = (self.week, self.month)

    @classmethod
    def de_json(cls, data: dict, client: 'Client'):
        if not data:
            return None

        data = super(Ratings, cls).de_json(data, client)

        return cls(client=client, **data)

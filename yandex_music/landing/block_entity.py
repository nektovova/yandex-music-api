from typing import TYPE_CHECKING, Optional, List

if TYPE_CHECKING:
    from yandex_music import Client

from yandex_music import YandexMusicObject, Promotion, Album, Playlist, MixLink, PlayContext, ChartItem,\
    GeneratedPlaylist


de_json = {
    'personal-playlist': GeneratedPlaylist.de_json,
    'promotion': Promotion.de_json,
    'album': Album.de_json,
    'playlist': Playlist.de_json,
    'chart-item': ChartItem.de_json,
    'play-context': PlayContext.de_json,
    'mix-link': MixLink.de_json
}


class BlockEntity(YandexMusicObject):
    def __init__(self,
                 id_,
                 type_,
                 data,
                 client: Optional['Client'] = None,
                 **kwargs) -> None:

        self.id = id_
        self.type = type_
        self.data = data

        self.client = client
        self._id_attrs = (self.id, self.type, self.data)

    @classmethod
    def de_json(cls, data: dict, client: 'Client'):
        if not data:
            return None

        data = super(BlockEntity, cls).de_json(data, client)
        data['data'] = de_json.get(data.get('type_'))(data.get('data'), client)

        return cls(client=client, **data)

    @classmethod
    def de_list(cls, data: dict, client: 'Client'):
        if not data:
            return []

        entities = list()
        for entity in data:
            entities.append(cls.de_json(entity, client))

        return entities

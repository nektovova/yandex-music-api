from typing import TYPE_CHECKING, Optional, List

if TYPE_CHECKING:
    from yandex_music import Client

from yandex_music import YandexMusicObject


class ChartItem(YandexMusicObject):
    def __init__(self,
                 track,
                 chart,
                 client: Optional['Client'] = None,
                 **kwargs) -> None:
        self.track = track
        self.chart = chart

        self.client = client
        self._id_attrs = (self.track, self.chart)

    @classmethod
    def de_json(cls, data: dict, client: 'Client'):
        if not data:
            return None

        data = super(ChartItem, cls).de_json(data, client)
        from yandex_music import Chart, Track
        data['track'] = Track.de_json(data.get('track'), client)
        data['chart'] = Chart.de_json(data.get('chart'), client)

        return cls(client=client, **data)

    @classmethod
    def de_list(cls, data: dict, client: 'Client'):
        if not data:
            return []

        tracks = list()
        for track in data:
            tracks.append(cls.de_json(track, client))

        return tracks

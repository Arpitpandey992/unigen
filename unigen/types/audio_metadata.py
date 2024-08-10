from dataclasses import dataclass, field

from unigen.types.picture import Picture


@dataclass
class Tags:
    title: list[str] = field(default_factory=list)
    album: list[str] = field(default_factory=list)
    artist: list[str] = field(default_factory=list)
    album_artist: list[str] = field(default_factory=list)
    disc_number: int | None = None
    total_discs: int | None = None
    track_number: int | None = None
    total_tracks: int | None = None
    comment: list[str] = field(default_factory=list)
    date: str | None = None
    catalog: list[str] = field(default_factory=list)
    barcode: list[str] = field(default_factory=list)
    disc_name: list[str] = field(default_factory=list)
    custom_tags: dict[str, list[str]] = field(default_factory=dict)
    pictures: list[Picture] = field(default_factory=list)
    extension: str = ""

    # currently not supported by unigen
    genre: str | None = None
    duration: str | None = None
    arranger: str | None = None
    author: str | None = None
    bpm: str | None = None
    composer: str | None = None
    conductor: str | None = None
    copyright: str | None = None
    encoded_by: str | None = None
    grouping: str | None = None
    isrc: str | None = None
    language: str | None = None
    lyricist: str | None = None
    lyrics: str | None = None
    media: str | None = None
    original_album: str | None = None
    original_artist: str | None = None
    original_date: str | None = None
    part: str | None = None
    performer: str | None = None
    publisher: str | None = None
    remixer: str | None = None
    subtitle: str | None = None
    website: str | None = None


@dataclass
class MediaInfo:
    sample_rate: int | None = None
    channels: int | None = None
    bitrate: int | None = None
    bits_per_sample: int | None = None
    codec: str | None = None


@dataclass
class AudioFileMetadata:
    file_name: str
    file_path: str
    extension: str
    tags: Tags
    media_info: MediaInfo

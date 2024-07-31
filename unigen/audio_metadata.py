from pydantic import BaseModel, Field
from typing import Optional

from unigen.audio_manager import IAudioManager
from .utils import pictureNumberToName


class Picture(BaseModel):
    picture_type: int
    data: bytes

    @property
    def picture_type_name(self):
        return pictureNumberToName[self.picture_type]


class AudioFileMetadata(BaseModel):
    title: list[str] = Field(default_factory=list)
    album: list[str] = Field(default_factory=list)
    artist: list[str] = Field(default_factory=list)
    album_artist: list[str] = Field(default_factory=list)
    disc_number: Optional[int] = None
    total_discs: Optional[int] = None
    track_number: Optional[int] = None
    total_tracks: Optional[int] = None
    comment: list[str] = Field(default_factory=list)
    date: Optional[str] = None
    catalog: list[str] = Field(default_factory=list)
    barcode: list[str] = Field(default_factory=list)
    disc_name: list[str] = Field(default_factory=list)
    custom_tags: dict[str, list[str]] = Field(default_factory=dict)
    pictures: list[Picture] = Field(default_factory=list)
    extension: str = ""

    # unsupported fields
    genre: Optional[str] = None
    duration: Optional[str] = None
    arranger: Optional[str] = None
    author: Optional[str] = None
    bpm: Optional[str] = None
    composer: Optional[str] = None
    conductor: Optional[str] = None
    copyright: Optional[str] = None
    encoded_by: Optional[str] = None
    grouping: Optional[str] = None
    isrc: Optional[str] = None
    language: Optional[str] = None
    lyricist: Optional[str] = None
    lyrics: Optional[str] = None
    media: Optional[str] = None
    original_album: Optional[str] = None
    original_artist: Optional[str] = None
    original_date: Optional[str] = None
    part: Optional[str] = None
    performer: Optional[str] = None
    publisher: Optional[str] = None
    remixer: Optional[str] = None
    subtitle: Optional[str] = None
    website: Optional[str] = None

    @classmethod
    def from_audio_manager(cls, audio_manager: IAudioManager) -> "AudioFileMetadata":
        """
        Factory method to create an AudioFileMetadata instance from an IAudioManager instance.
        """
        return cls(
            title=audio_manager.getTitle(),
            album=audio_manager.getAlbum(),
            artist=audio_manager.getArtist(),
            album_artist=audio_manager.getAlbumArtist(),
            disc_number=audio_manager.getDiscNumber(),
            total_discs=audio_manager.getTotalDiscs(),
            track_number=audio_manager.getTrackNumber(),
            total_tracks=audio_manager.getTotalTracks(),
            comment=audio_manager.getComment(),
            date=audio_manager.getDate(),
            catalog=audio_manager.getCatalog(),
            barcode=audio_manager.getBarcode(),
            disc_name=audio_manager.getDiscName(),
            custom_tags=audio_manager.getAllCustomTags(),
            # pictures=audio_manager.
            extension=audio_manager.getExtension(),
        )


metadata = AudioFileMetadata(title=["Song Title"], album=["Album Name"], artist=["Artist Name"])

print(metadata.model_dump_json())

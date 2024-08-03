from dataclasses import dataclass, field
from typing import Dict, List, Optional

from unigen.types.picture import Picture
from unigen.wrapper.audio_manager import IAudioManager


@dataclass
class AudioFileMetadata:
    title: List[str] = field(default_factory=list)
    album: List[str] = field(default_factory=list)
    artist: List[str] = field(default_factory=list)
    album_artist: List[str] = field(default_factory=list)
    disc_number: Optional[int] = None
    total_discs: Optional[int] = None
    track_number: Optional[int] = None
    total_tracks: Optional[int] = None
    comment: List[str] = field(default_factory=list)
    date: Optional[str] = None
    catalog: List[str] = field(default_factory=list)
    barcode: List[str] = field(default_factory=list)
    disc_name: List[str] = field(default_factory=list)
    custom_tags: Dict[str, List[str]] = field(default_factory=dict)
    pictures: List[Picture] = field(default_factory=list)
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
            pictures=audio_manager.getAllPictures(),
            extension=audio_manager.getExtension(),
        )


if __name__ == "__main__":
    metadata = AudioFileMetadata(title=["Song Title"], album=["Album Name"], artist=["Artist Name"])
    print(metadata)

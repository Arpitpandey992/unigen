import os
from abc import ABC, abstractmethod
from typing import Optional

from unigen.types.audio_metadata import AudioFileMetadata, MediaInfo, Tags
from unigen.types.picture import PICTURE_TYPE, Picture

"""
This is a wrapper around mutagen module. 
It allows us to call the same functions for any supported extension, and hence reducing code complexity.
"""


class IAudioManager(ABC):
    """
    Interface Class for generalizing usage of Mutagen across multiple formats
    """

    @abstractmethod
    def getFilePath(self) -> str:
        """filepath of the audio file"""

    def getFileName(self) -> str:
        """filename of the audio file"""
        return os.path.basename(self.getFilePath())

    def getExtension(self) -> str:
        """Extension of the audio file like .mp3, .flac, etc"""
        _, extension = os.path.splitext(self.getFilePath())
        return extension.lower()

    @abstractmethod
    def setTitle(self, newTitle: list[str]):
        """Set the title of track"""

    @abstractmethod
    def setAlbum(self, newAlbum: list[str]):
        """Set the album name of the track"""

    @abstractmethod
    def setDiscNumbers(self, discNumber: int, totalDiscs: int):
        """
        set disc number and total number of discs
        """

    @abstractmethod
    def setTrackNumbers(self, trackNumber: int, totalTracks: int):
        """
        Set Track number and total number of tracks
        """

    @abstractmethod
    def setComment(self, comment: list[str]) -> None:
        """Set comment"""

    @abstractmethod
    def setPictureOfType(self, imageData: bytes, pictureType: PICTURE_TYPE) -> None:
        """Set a picture of some type"""

    @abstractmethod
    def hasPictureOfType(self, pictureType: PICTURE_TYPE) -> bool:
        """check whether a picture of some type (3 = front Cover) is present"""

    @abstractmethod
    def deletePictureOfType(self, pictureType: PICTURE_TYPE) -> bool:
        """delete a picture of some type (3 = front Cover), returns True if picture successfully deleted"""

    @abstractmethod
    def setDate(self, date: str) -> None:
        """Set the album release date"""

    @abstractmethod
    def setCustomTag(self, key: str, value: list[str]) -> None:
        """Set a custom tag as Key = value"""

    @abstractmethod
    def setCatalog(self, value: list[str]) -> None:
        """Set Catalog number"""

    @abstractmethod
    def setBarcode(self, value: list[str]) -> None:
        """Set Barcode number"""

    @abstractmethod
    def setDiscName(self, value: list[str]) -> None:
        """Set The Name of The Disc"""

    @abstractmethod
    def getTitle(self) -> list[str]:
        """get the title of track"""

    @abstractmethod
    def getAlbum(self) -> list[str]:
        """get the album name of the track"""

    @abstractmethod
    def getArtist(self) -> list[str]:
        """get the artist name of the track"""

    @abstractmethod
    def getAlbumArtist(self) -> list[str]:
        """get the album Artist name"""

    @abstractmethod
    def getDiscNumber(self) -> Optional[int]:
        """get disc number"""

    @abstractmethod
    def getTotalDiscs(self) -> Optional[int]:
        """get total number of discs"""

    @abstractmethod
    def getTrackNumber(self) -> Optional[int]:
        """get Track number"""

    @abstractmethod
    def getTotalTracks(self) -> Optional[int]:
        """get Total number of tracks"""

    @abstractmethod
    def getComment(self) -> list[str]:
        """get comment"""

    @abstractmethod
    def getDate(self) -> Optional[str]:
        """get the album release date"""

    @abstractmethod
    def getCustomTag(self, key: str) -> list[str]:
        """get a custom tag as Key = value (which can be a string or a list of strings)"""

    @abstractmethod
    def getAllCustomTags(self) -> dict[str, list[str]]:
        """get a dict containing all custom tags in the file defined as key-value pairs"""

    @abstractmethod
    def getCatalog(self) -> list[str]:
        """get Catalog number of the album"""

    @abstractmethod
    def getBarcode(self) -> list[str]:
        """get Barcode of the album"""

    @abstractmethod
    def getDiscName(self) -> list[str]:
        """get the name of the disc"""

    @abstractmethod
    def getAllPictures(self) -> list[Picture]:
        """get all pictures embedded into the audio file"""

    @abstractmethod
    def printInfo(self) -> str:
        """See the metadata information in Human Readable Format"""

    def getMetadata(self) -> AudioFileMetadata:
        return AudioFileMetadata(
            file_name=self.getFileName(),
            file_path=self.getFilePath(),
            extension=self.getExtension(),
            tags=Tags(
                title=self.getTitle(),
                album=self.getAlbum(),
                artist=self.getArtist(),
                album_artist=self.getAlbumArtist(),
                disc_number=self.getDiscNumber(),
                total_discs=self.getTotalDiscs(),
                track_number=self.getTrackNumber(),
                total_tracks=self.getTotalTracks(),
                comment=self.getComment(),
                date=self.getDate(),
                catalog=self.getCatalog(),
                barcode=self.getBarcode(),
                disc_name=self.getDiscName(),
                custom_tags=self.getAllCustomTags(),
                pictures=self.getAllPictures(),
                extension=self.getExtension(),
            ),
            media_info=self.getMediaInfo(),
        )

    @abstractmethod
    def getMediaInfo(self) -> MediaInfo:
        """Retrieve media information like bitrate, bits per channel, etc"""

    @abstractmethod
    def save(self) -> None:
        """Apply metadata changes"""

    @abstractmethod
    def clearTags(self) -> None:
        """clear all metadata tags"""


non_custom_tags: list[str] = [
    "title",
    "album",
    "artist",
    "albumartist",
    "discnumber",
    "totaldiscs",
    "disctotal",
    "tracknumber",
    "totaltracks",
    "tracktotal",
    "comment",
    "date",
    "catalog",
    "labelno",
    "catalognumber",
    "barcode",
    "discname",
    "discsubtitle",
]

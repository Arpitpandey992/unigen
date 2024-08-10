from typing import Literal

from mutagen.id3 import ID3
from mutagen.id3._frames import APIC, COMM, TALB, TDRC, TIT2, TPOS, TRCK, TXXX
from mutagen.mp3 import MP3
from mutagen.wave import WAVE

from unigen.types.audio_metadata import AudioFileMetadata, MediaInfo
from unigen.types.picture import PICTURE_NAME_TO_NUMBER, Picture

from .audio_manager import IAudioManager, non_custom_tags
from .utils import (
    cleanDate,
    convertStringToNumber,
    extractYearFromDate,
    getFirstElement,
    getProperCount,
    splitAndGetFirst,
    splitAndGetSecond,
    toList,
)


class CustomWAVE(WAVE):
    def add(self, frame):
        frameHashKey = frame.HashKey
        self[frameHashKey] = frame

    def getall(self, key):
        if key in self:
            return [self[key]]
        else:
            key = key + ":"
            return [v for s, v in self.items() if s.startswith(key)]


class CustomMP3(ID3):
    def __init__(self, *args, **kwargs):
        if args:
            filePath = args[0]
            # ensuring that the file contains an ID3 tag beforehand
            audio = MP3(filePath)
            if audio.tags is None:
                audio.add_tags()
                audio.save()
            self.info = audio.info

        super().__init__(*args, **kwargs)


class ID3Wrapper(IAudioManager):
    def __init__(self, file_path: str, extension: Literal[".mp3", ".wav"]):
        extension_handlers = {".mp3": CustomMP3, ".wav": CustomWAVE}
        self.extension = extension
        self.audio = extension_handlers[extension](file_path)
        self.file_path = file_path

    def getFilePath(self):
        return self.file_path

    def setTitle(self, newTitle):
        self.audio.add(TIT2(encoding=3, text=[title for title in newTitle[:1]]))
        # Multiple titles are not supported in ID3 -> add other titles as custom tag!
        self.setCustomTag("Alternate Title", newTitle[1:])

    def setAlbum(self, newAlbum):
        self.audio.add(TALB(encoding=3, text=[album for album in newAlbum[:1]]))
        # Multiple Album Names are not supported in ID3 -> add other album names as custom tag!
        self.setCustomTag("Alternate Album Name", newAlbum[1:])

    def setDiscNumbers(self, discNumber, totalDiscs):
        properDiscNumber, properTotalDiscs = getProperCount(discNumber, totalDiscs)
        self.audio.add(TPOS(encoding=3, text=[properDiscNumber + "/" + properTotalDiscs]))

    def setTrackNumbers(self, trackNumber, totalTracks):
        properTrackNumber, properTotalTracks = getProperCount(trackNumber, totalTracks)
        self.audio.add(TRCK(encoding=3, text=[properTrackNumber + "/" + properTotalTracks]))

    def setComment(self, comment):
        self.audio.add(COMM(encoding=3, text=comment))

    def setPictureOfType(self, imageData, pictureType):
        picture = APIC(encoding=3, mime="image/jpeg", type=PICTURE_NAME_TO_NUMBER[pictureType], desc=pictureType, data=imageData)
        self.audio.add(picture)

    def hasPictureOfType(self, pictureType):
        pictures = self.audio.getall("APIC")
        if pictures:
            for picture in pictures:
                if picture.type == PICTURE_NAME_TO_NUMBER[pictureType]:
                    return True
        return False

    def deletePictureOfType(self, pictureType):
        for frame in self.audio.getall("APIC"):
            if frame.type == PICTURE_NAME_TO_NUMBER[pictureType]:
                self.audio.pop(frame.HashKey)
                return True
        return False

    def setDate(self, date):
        self.audio.add(TDRC(encoding=3, text=[cleanDate(date)]))
        year = extractYearFromDate(date)
        if year:
            self.setCustomTag("year", [year])

    def setCustomTag(self, key, value):
        # deleting the custom tag if exists beforehand.
        self._delete_custom_tag(key)
        if not value:
            return
        self.audio.add(TXXX(encoding=3, desc=key, text=value))

    def setCatalog(self, value):
        self.setCustomTag("CATALOGNUMBER", value)
        self.setCustomTag("CATALOG", value)

    def setBarcode(self, value):
        self.setCustomTag("barcode", value)

    def setDiscName(self, value):
        self.setCustomTag("DISCSUBTITLE", value)

    def getTitle(self):
        ans = self.audio.get("TIT2")
        if not ans or not ans.text:
            return []
        title = [x for x in ans.text]
        other_titles = self.getCustomTag("Alternate Title")
        title.extend(other_titles) if other_titles else None
        return title

    def getAlbum(self):
        ans = self.audio.get("TALB")
        if not ans or not ans.text:
            return []
        album = [x for x in ans.text]
        other_album_names = self.getCustomTag("Alternate Album Name")
        album.extend(other_album_names) if other_album_names else None
        return album

    def getArtist(self):
        ans = self.audio.get("TPE1")
        return toList(ans.text) if ans else []

    def getAlbumArtist(self):
        ans = self.audio.get("TPE2")
        return toList(ans.text) if ans else []

    def getDiscNumber(self):
        ans = self.audio.get("TPOS")
        return convertStringToNumber(splitAndGetFirst(getFirstElement(ans.text))) if ans else None

    def getTotalDiscs(self):
        ans = self.audio.get("TPOS")
        return convertStringToNumber(splitAndGetSecond(getFirstElement(ans.text))) if ans else None

    def getTrackNumber(self):
        ans = self.audio.get("TRCK")
        return convertStringToNumber(splitAndGetFirst(getFirstElement(ans.text))) if ans else None

    def getTotalTracks(self):
        ans = self.audio.get("TRCK")
        return convertStringToNumber(splitAndGetSecond(getFirstElement(ans.text))) if ans else None

    def getComment(self):
        ans = self.audio.get("COMM::XXX")
        return toList(ans.text) if ans else []

    def getDate(self):
        ans = self.audio.get("TDRC")
        if not ans or not ans.text:
            return None
        return cleanDate(str(ans.text[0]))

    def getCustomTag(self, key):
        frames = self.audio.getall("TXXX")
        for frame in frames:
            if key == frame.desc:
                return frame.text
        return []

    def getAllCustomTags(self):
        frames = self.audio.getall("TXXX")
        custom_tags = {frame.desc: frame.text for frame in frames if frame.desc.lower() not in non_custom_tags}
        return custom_tags

    def getCatalog(self):
        return self._searchMultiCustomTags(["CATALOGNUMBER", "CATALOG", "LABELNO"])

    def getBarcode(self):
        return self._searchMultiCustomTags(["barcode", "BARCODE"])

    def getDiscName(self):
        return self._searchMultiCustomTags(["DISCSUBTITLE", "DISCNAME"])

    def getAllPictures(self):
        pictures: list[Picture] = []
        audio_pictures = self.audio.getall("APIC")
        if audio_pictures:
            for picture in audio_pictures:
                if isinstance(picture, APIC):
                    picture_dict = picture.__dict__
                    if "type" not in picture_dict:
                        print("warning: picture does not contain a type. taking 0 as default")
                    if "data" not in picture_dict:
                        print("warning: picture does not contain any data. skipped")
                        continue
                    pictures.append(Picture(picture_type=picture.__dict__.get("type", 0), data=picture.__dict__["data"]))
        return pictures

    def getMediaInfo(self) -> MediaInfo:
        info = self.audio.info
        return MediaInfo(
            sample_rate=info.sample_rate if hasattr(info, "sample_rate") else None,
            channels=info.channels if hasattr(info, "channels") else None,
            bits_per_sample=info.bits_per_sample if hasattr(info, "bits_per_sample") else None,
            bit_rate=info.bitrate if hasattr(info, "bitrate") else None,
        )

    def printInfo(self):
        return self.audio.pprint()

    def save(self):
        self.audio.save()

    def clearTags(self):
        self.audio.delete()

    def _searchMultiCustomTags(self, possibleFields: list[str]) -> list[str]:
        for field in possibleFields:
            ans = self.getCustomTag(field)
            if ans:
                return ans
        return []

    def _delete_custom_tag(self, key: str):
        frames = self.audio.getall("TXXX")
        for frame in frames:
            if key == frame.desc:
                self.audio.pop(frame.HashKey)
                return

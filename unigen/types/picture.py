from dataclasses import dataclass
from typing import Literal


@dataclass
class Picture:
    picture_type: int
    data: bytes

    @property
    def picture_type_name(self) -> str:
        return PICTURE_NUMBER_TO_NAME.get(self.picture_type, "Unknown")


PICTURE_TYPE = Literal[
    "Other",
    "File icon",
    "Other file icon",
    "Cover (front)",
    "Cover (back)",
    "Leaflet page",
    "Media (e.g. lable side of CD)",
    "Lead artist/lead performer/soloist",
    "Artist/performer",
    "Conductor",
    "Band/Orchestra",
    "Composer",
    "Lyricist/text writer",
    "Recording Location",
    "During recording",
    "During performance",
]
PICTURE_NAME_TO_NUMBER: dict[PICTURE_TYPE, int] = {
    "Other": 0,
    "File icon": 1,
    "Other file icon": 2,
    "Cover (front)": 3,
    "Cover (back)": 4,
    "Leaflet page": 5,
    "Media (e.g. lable side of CD)": 6,
    "Lead artist/lead performer/soloist": 7,
    "Artist/performer": 8,
    "Conductor": 9,
    "Band/Orchestra": 10,
    "Composer": 11,
    "Lyricist/text writer": 12,
    "Recording Location": 13,
    "During recording": 14,
    "During performance": 15,
}

PICTURE_NUMBER_TO_NAME: dict[int, PICTURE_TYPE] = {number: name for name, number in PICTURE_NAME_TO_NUMBER.items()}

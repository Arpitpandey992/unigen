from pydantic import BaseModel
from unigen.utils import pictureNumberToName


class Picture(BaseModel):
    picture_type: int
    data: bytes

    @property
    def picture_type_name(self):
        return pictureNumberToName[self.picture_type]

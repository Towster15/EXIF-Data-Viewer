import filetype
from PIL import Image, ExifTags

from fileformaterror import FileFormatError


class DisplayedImage:
    def __init__(self, file_path: str) -> None:
        self.image = None
        self.load_new_image(file_path)
        self.__exif_data = self.image.getexif()

    def load_new_image(self, file_path) -> None:
        if filetype.is_image(file_path):
            try:
                self.image = Image.open(file_path)
            except OSError:
                raise FileFormatError("image")
        else:
            raise FileFormatError("image")

    def get_exif(self) -> dict:
        return {
            ExifTags.TAGS[k]: v
            for k, v in self.__exif_data.items()
            # if k in ExifTags.TAGS
        }

    def get_important_exif(self) -> dict:
        return {
            ExifTags.TAGS[k]: v
            for k, v in self.__exif_data.items()
            if k
            in [
                0x0100,
                0x0101,
                0x011A,
                0x011B,
                0x0132,
                0x9003,
                0x9004,
                0x9010,
                0x9011,
                0x9012,
                0xA002,
                0xA003,
            ]
            # ImageWidth, ImageLength, XResolution, YResolution,
            # DateTime, DateTimeOriginal, DateTimeDigitized, OffsetTime,
            # OffsetTimeOriginal, OffsetTimeDigitized, ExifImageWidth,
            # ExifImageHeight
        }

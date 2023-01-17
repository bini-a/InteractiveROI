import re
from PIL import Image
import numpy as np


class ImageFile:
    """ Image File class to save file path, file name, date, mask_id"""

    def __init__(self, filename):
        self.path = filename
        self.image_name = filename.split("\\")[-1]
        self.mask_id = None

    def read_img(self, sliced):
        """
        reads image path and returns original image(np.array)
        if sliced=True, returns sliced image for faster display
        """
        img = np.asarray(Image.open(self.path))
        return img if not sliced else img[::2, ::2]


class WaterImageFile(ImageFile):
    def __init__(self, filename):
        super().__init__(filename)
        self.date = self.get_date()
        self.mm, self.dd, self.yy = self.date.split("/")

    def get_date(self):
        """
        extracts date pattern (MM/DD/YY) from file name (eg. Hbwtr_w3_20200315_115918.JPG)
        :return: date
        """
        date_pattern = "\d{8}"  # eg 12-12-2020
        date = re.search(date_pattern, self.path).group(0)
        dd, mm, yy = date[-2:], date[-4:-2], date[-8:-4]
        date = mm + '/' + dd + '/' + yy
        return date

    def get_water_year(self):
        """
        extracts water year from dates
        """
        if self.mm >= "10" or self.mm <= "12":
            return int(self.yy[-2:]) + 1
        return int(self.yy[-2:])

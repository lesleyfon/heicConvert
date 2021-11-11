from django.db import models
from wand.image import Image
# Create your models here.


class Model:

    def downloadImage(self):
        pass

    def convertImageTo(image_file, image_type):

        # img = Image(filename=imagedata)
        if image_type is None or len(image_type) == 0:
            image_type = 'jpeg'
        with Image(blob=image_file) as i:
            # i.save(filename="/Users/lesley/Desktop/formatImage/" +
            #        imagename + filetype)

            i.format = image_type
            return i

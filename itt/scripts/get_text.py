from PIL import Image
from pytesseract import image_to_string

from .constants import OEM_ENGINE_DEFAULT, PSM_DEFAULT


def convert_to_text(image, psm=PSM_DEFAULT, oem=OEM_ENGINE_DEFAULT, langs='spa'):
    """
    Extract text from image.
    :param image: Image used to extract text.
    :param psm: psm config, set text detection type (see constants.py).
    :param oem: oem config, set engine mode. (see constants.py).
    :param langs: lang config, set text langs to be extracted.
    :return: text: text extracted.
    """

    text = None
    if image is not None:
        image = Image.open(image)
        config = '--tessdata-dir {td} -l {langs} --oem {oem} --psm {psm}'.format(
            td='/home/alfy/Dev/python/image_to_text/src/data/',
            langs=langs,
            oem=oem,
            psm=psm
        )  # '--tessdata-dir"./data"'
        text = image_to_string(image, config=config)
        image.close()

    return text

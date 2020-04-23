import os

from django.db import models


def save_image_name(instance, filename):
    """
    Cambia el nombre del fichero para ser guardado con el formato UUID.extension
    :param instance: obj, instancia del objeto que llama a la función.
    :param filename: str, cadena con el nombre del fichero a modificar
    :return: str, cadena con el formato final a guardar 'carpeta/UUID.extension'
    """
    print(filename)
    name, extension = os.path.splitext(filename)
    return 'tmp/{}{}'.format(instance.unique_id, extension)


class ImageModel(models.Model):
    image = models.ImageField(upload_to=save_image_name)
    unique_id = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.unique_id)


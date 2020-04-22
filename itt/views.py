import os
import uuid

from datetime import datetime, timedelta

from django import views
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.timezone import make_aware
from django.views.generic import CreateView

from .forms import ImageForm, ImageModel
from .scripts.get_text import convert_to_text


class HomeView(CreateView):
    template_name = "itt/home.html"
    form_class = ImageForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        data = uuid.uuid1()
        request.POST = request.POST.copy()
        request.POST['unique_id'] = data
        self.success_url = reverse_lazy('itt:image', kwargs={'unique_id': data})

        return super(HomeView, self).post(request, *args, **kwargs)


class ShowImage(views.View):

    @staticmethod
    def get(request, unique_id):
        data = get_object_or_404(ImageModel, unique_id=unique_id)

        return render(
            request,
            'itt/show_image.html',
            {
                'url': '{url}text/{uuid}/'.format(
                    url=settings.MAIN_URL,
                    uuid=str(unique_id)),
                'image': data.image
            }
        )


class ImageToText(views.View):

    @staticmethod
    def get(request, unique_id):
        error = False
        data = get_object_or_404(ImageModel, unique_id=unique_id)
        text = convert_to_text(data.image)
        if not text:
            error = 'Image error: Something has occurred handling image.'

        return JsonResponse({
            'text': text,
            'error': error
        })


class ClearTemp(views.View):

    def get(self, request):
        hours = self._check_hours(request.GET.get('hours'))
        url = settings.MEDIA_ROOT
        date = make_aware(datetime.now()) - timedelta(hours=hours)
        items = ImageModel.objects.filter(created__lte=date)

        for item in items:
            file = '{}/{}'.format(url, item.image.name)
            if os.path.exists(file):
                os.remove(file)
            item.delete()

        return HttpResponse('Done')

    @staticmethod
    def _check_hours(get_hours):
        """
        Comprueba si la cadena enviada es un número.
        Si es número lo convierte a Int y lo devuelve.
        Si no es número o es una cadena vacía devuelve el valor por defecto que es 1.
        :param get_hours: str cadena con las horas enviadas.
        :return: int. numero de horas.
        """
        hours = 1
        if get_hours:
            if get_hours.isdigit():
                hours = int(get_hours)

        return hours


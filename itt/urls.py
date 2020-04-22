from django.urls import path

from .views import HomeView, ShowImage, ImageToText, ClearTemp

app_name = 'itt'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('image/<uuid:unique_id>/', ShowImage.as_view(), name='image'),
    path('text/<uuid:unique_id>/', ImageToText.as_view(), name='to_text'),
    path('clear/', ClearTemp.as_view(), name='clear'),
]

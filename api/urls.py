from django.urls import path

from api.views import short, ShortView


urlpatterns = [
    path('short/', short, name='short'),
    path('short-you-url/<int:url>', ShortView.as_view()),
]

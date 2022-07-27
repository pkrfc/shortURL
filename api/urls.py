from django.urls import path

from api.views import ShortView, short

urlpatterns = [
    path('short/', short, name='short'),
    path('short-you-url/<int:url>', ShortView.as_view()),
]

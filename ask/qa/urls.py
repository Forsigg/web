from django.urls import path
from .views import new, test, popular, question

urlpatterns = [
    path('', new, name='new'),
    path('popular/', popular, name='popular'),
    path(r'question/<int:id>', question, name='question')

]
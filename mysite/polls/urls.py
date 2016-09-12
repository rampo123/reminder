from django.conf.urls import url

from .views import AppointmentCreateView

urlpatterns = [
     url(r'^$', AppointmentCreateView.as_view(), name='new_appointment'),
]
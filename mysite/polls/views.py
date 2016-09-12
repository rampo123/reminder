from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.template import RequestContext 
from django.shortcuts import render_to_response 
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Appointment
from twilio.rest import TwilioRestClient 
from datetime import datetime 
from pytz import timezone 
from phonenumbers import timezone as ptz 
import phonenumbers as ph 
from time import sleep
from twilio.rest.exceptions import TwilioRestException

 
# put your own credentials here 
 
class AppointmentCreateView(CreateView):
    """Powers a form to create a new appointment"""

    model = Appointment
    fields = ['name', 'phone_number']

    def post(self, request, *args, **kwargs):
         ACCOUNT_SID = "AC493fbcfcd4aeda77fac77e21f34f76d8" 
         AUTH_TOKEN = "8380863ae73c793559a283dbc29d4392"
         day_start_hour = 6
         day_end_hour = 23
         name = request.POST['name'] 
         number = request.POST['phone_number'] 
         phone_number = ph.parse(number, None) 
         country_timezone = ptz.time_zones_for_number(phone_number)[0] 
         created = datetime.now(timezone(country_timezone)) 
         if not name: 
             return render(request, 'polls/redict.html', context={'error_message': 'Please enter a name'}) 
         if not number: 
             return render(request, 'polls/redict.html', context={'error_message': 'Please enter a number'}) 
         client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
         long_enough = 3600
         attempts = 0
         while attempts < 5 :
         	log_file = open("log.txt", "a+")
         	time_file = open("time.txt", 'a+')
         	print("Running periodic task!")
         	phone_number = ph.parse(number, None) 
         	country_timezone = ptz.time_zones_for_number(phone_number)[0] 
         	country_time = datetime.now(timezone(country_timezone)) 
         	running_time = country_time - created
         	try:
         	    if  country_time.hour >= day_start_hour and country_time.hour <= day_end_hour: 
         	        client.messages.create(
         	        to=number, 
         	        from_="+12015003031", 
         	        body="your name is john",)
         	        attempts = 0
         	        running_tm = str(running_time)
         	        time_file.write("running time in format h:min:s:ms")
         	        time_file.write(running_tm)
         	        time_file.close()
         	except TwilioRestException as e:
                    running_t = str(e)
                    print "yep"
                    log_file.write(running_t)
                    attempts = attempts + 1 
                    log_file.close()
           	sleep(long_enough)

    # Create your views here.

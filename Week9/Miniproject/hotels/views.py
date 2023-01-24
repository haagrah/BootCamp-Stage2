from django.shortcuts import render
from hotels.models import Hotel, Reservation
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import ReservationForm

def home(request):
    return render(request, 'hotel/home.html')
def hotel(request):
    hotels = Hotel.objects.order_by('-disponible')
    resers = Reservation.objects.all()
    return render(request, 'hotel/hotel.html', {"hotels":hotels, "resers":resers})

class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservationForm.html'
    success_url = reverse_lazy('reservation_success')
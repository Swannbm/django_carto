from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods

from .models import PointOfInterest as POI
from .forms import ContactForm


def cours(request):
    return render(request, 'carto/map.1.html')


def index(request):
    context = {
        'poi_list': POI.objects.filter(is_localised=True),
        'center': (48.915246, 2.394479)
    }
    return render(request, 'carto/map.2.html', context)


@require_http_methods(["POST"])
def search(request):
    slug = request.POST['slug']
    points = POI.objects.filter(is_localised=True) \
                        .filter(title__contains=slug)
    if len(points) > 0:
        long = sum([_.longitude for _ in points]) / len(points)
        lat = sum([_.latitude for _ in points]) / len(points)
    else:
        long, lat = 2.394479, 48.915246
    context = {
        'poi_list': points,
        'center': (lat, long)
    }
    return render(request, 'carto/map.html', context)


class PoiDetailView(generic.DetailView):
    model = POI
    template_name = 'carto/poi_detail.html'


def contact(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['email']
            body = form.cleaned_data['message']
            recipients = ['info@example.com']
            subject = 'Formulaire contact site auberentransition'
            send_mail(subject, body, sender, recipients)
            return render(request, 'carto/contact.html')
    else:
        form = ContactForm()  # blank form
    return render(request, 'carto/contact.html', {'form': form})


def test(request):
    context = {
        'poi_list': POI.objects.filter(is_localised=True)[:10],
        'center': (48.915246, 2.394479)
    }
    return render(request, 'carto/map.2.html', context)



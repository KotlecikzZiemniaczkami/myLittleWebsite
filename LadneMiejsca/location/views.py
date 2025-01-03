from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

text = {
    'wroclaw': ['Wroclaw is a really old city which history has started in A.D. 142.<br>It has pretty sunsets.',
                'location/images/Wroclaw.jpg',
                '<a href=wroclaw/>{{ place|title }}</a>'],
    'posadowo': ['It has beautiful forgotten palace',
                'location/images/posadowo.jpg']
        }

def index(request):
    return render(request, 'location/index.html', {'places': list(text)})


def loc(request, location):
    if location in text.keys():
        return render(request, 'location/place.html', {
            'place': location.upper(),
            'descryption': text[location][0],
            'image': text[location][1],
        })
    else:
        return HttpResponseNotFound("404\nSorry Traveler, maybe next time")
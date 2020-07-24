from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        'title': 'the Doctor will return shortly',
        'my_number': 123456,
        'my_list': [ 1, 2, 3, 4, 5, 6, 7 ],
        "my_html": '<h1>h3lL0 W0rlD</h1>'
    }

    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")

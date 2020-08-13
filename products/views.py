from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# products url is map -> to this index function
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {
        'products': products,
        'change_view': 'False'
    })
    # return HttpResponse('<h4>Hello World!, welcome to the space and time of building apps with DJango</h4>')


def new_product(request):
    return HttpResponse('New product out to0!')


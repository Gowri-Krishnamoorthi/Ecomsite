from django.shortcuts import render
from .models import Products , Order
# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse
import json




def index(request):
    product_objects = Products.objects.all()

    item_name = request.GET.get('item_name')

    if item_name != '' and item_name != None:
        product_objects = product_objects.filter(title__icontains = item_name)

    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request , 'shop/index.html' , {'product_objects' : product_objects})

def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request , 'shop/detail.html' , {'product_object' : product_object})

def checkout(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        zipcode = request.POST.get("zipcode")
        cart_data = request.POST.get("cartData")  # JSON cart data

        try:
            cart_data = json.loads(cart_data)  # Convert JSON string to dictionary
        except json.JSONDecodeError:
            cart_data = {}

        order = Order(name=name, email=email, phone=phone, address=address, zipcode=zipcode, items=cart_data)
        order.save()

        # Clear cart after successful order

    return render(request, "shop/checkout.html")



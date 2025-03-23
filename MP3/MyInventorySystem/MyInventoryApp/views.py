from django.shortcuts import render
from MyInventoryApp.models import Supplier, WaterBottle
from django.shortcuts import redirect

def view_supplier(request):
    suppliers = Supplier.objects.all()  
    return render(request, "view_supplier.html", {"suppliers": suppliers})
def home_redirect(request):
    return redirect("view_supplier")
def view_bottles(request):
    bottles = WaterBottle.objects.all()
    return render(request, 'view_bottles.html', {'bottles': bottles})
def add_bottle(request):
    suppliers = Supplier.objects.all() 
    return render(request, "add_bottle.html", {"suppliers": suppliers})
    


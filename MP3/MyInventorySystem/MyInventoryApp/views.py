from django.shortcuts import render
from MyInventoryApp.models import Supplier  
from django.shortcuts import redirect

def view_supplier(request):
    suppliers = Supplier.objects.all()  
    return render(request, "view_supplier.html", {"suppliers": suppliers})
def home_redirect(request):
    return redirect("view_supplier")
    


from django.shortcuts import render

# Create your views here.
def payment_cart(request):
    return render(request, "payment/cart.html")
def payment_complate(request):
    return render(request, "payment/complate.html")
def payment_purchase(request):
    return render(request, "payment/purchase.html")
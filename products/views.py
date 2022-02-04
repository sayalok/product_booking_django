from django.http import JsonResponse

from .models import Product

# Create your views here.
def getProductList(request):
    response = {}
    response['status'] = 'Success!'
    response['message'] = 'Success!'
    product_list = Product.objects.all().values()
    if product_list.count() > 0:
        response['data'] = list(product_list)
    else: 
        response['data'] = []

    return JsonResponse(response, safe=False)
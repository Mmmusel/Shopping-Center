from django.http import JsonResponse, HttpResponse
from django.core import serializers

from myApp.models import Book, UserInfo, Product, CartItems
import json


def show_cart(request):
    response = {}
    try:
        o1 = UserInfo.objects.get(id=request.GET.get('user_id'))
        products = CartItems.objects.filter(user_id=o1)

        response['list'] = json.loads(serializers.serialize("json", products))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def add_to_cart(request):
    response = {}
    try:
        o1 = UserInfo.objects.get(id=request.GET.get('user_id'))
        o2 = Product.objects.get(id=request.GET.get('product_id'))
        cartItems = CartItems.objects.filter(user_id=o1, product_id=o2)
        if cartItems.count() == 0:
            cartItem = CartItems(user_id=o1, product_id=o2, num=1)
            cartItem.save()
        else:
            cartItem = CartItems.objects.get(user_id=o1, product_id=o2)
            cartItem.num += 1
            cartItem.save()

        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def delete_item_in_cart(request):
    response = {}
    try:
        o1 = UserInfo.objects.get(id=request.GET.get('user_id'))
        o2 = Product.objects.get(id=request.GET.get('product_id'))
        cartItems = CartItems.objects.get(user_id=o1, product_id=o2)

        cartItems.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def edit_num_in_cart(request):
    response = {}
    try:
        o1 = UserInfo.objects.get(id=request.GET.get('user_id'))
        o2 = Product.objects.get(id=request.GET.get('product_id'))
        cartItems = CartItems.objects.get(user_id=o1, product_id=o2)

        if request.GET.get('num') == "1":
            cartItems.num += 1
            cartItems.save()
        else:
            if (cartItems.num != 1):
                cartItems.num -= 1
                cartItems.save()
            else:
                cartItems.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def cartProductsList(request):
    response = {}
    try:
        o1 = UserInfo.objects.get(id=int(request.GET.get('user_id')))
        items = CartItems.objects.filter(user_id=o1).values('product_id').values_list('product_id', flat=True)
        products = []
        for i in items:
            products.append(Product.objects.get(id=i))
        response['list'] = json.loads(serializers.serialize("json", products))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

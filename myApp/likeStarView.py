from django.core import serializers
from django.http import JsonResponse, HttpResponse


from myApp.models import UserInfo, Product, LikeList,StarList
import json


def get_user_like_to_product(request):
    response = {}
    try:
        o1 = UserInfo.objects.get(id=request.GET.get('user_id'))
        product = Product.objects.get(id=request.GET.get('product_id'))
        a=LikeList.objects.filter(user_id=o1,product_id=product)
        if(a.count()==1):
            response['good'] = 'good'
        else:
            response['good'] = 'not'
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def toggle_user_like_to_product(request):
    response = {}
    try:
        o1 = UserInfo.objects.get(id=request.GET.get('user_id'))
        product = Product.objects.get(id=request.GET.get('product_id'))
        a=LikeList.objects.filter(user_id=o1,product_id=product)
        if(a.count()==1):
            a[0].delete()
        else:
            newitem=LikeList(user_id=o1,product_id=product)
            newitem.save()

        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def get_product_likes(request):
    response = {}
    try:

        product = Product.objects.get(id=request.GET.get('product_id'))
        a=LikeList.objects.filter(product_id=product)
        p=a.count()
        response['goods']=p
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
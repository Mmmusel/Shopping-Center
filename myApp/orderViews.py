from django.http import JsonResponse, HttpResponse
from django.core import serializers

from myApp.models import Book, UserInfo, Product, CartItems,OrderInfo,OrderProducts
import json


def show_customer_order(request):
    response = {}
    try:
        o1 = UserInfo.objects.get(id=request.GET.get('customer_id'))
        orders = OrderInfo.objects.filter(customer_id=o1)

        response['list'] = json.loads(serializers.serialize("json", orders))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def show_business_order(request):
    response = {}
    try:
        o1 = UserInfo.objects.get(id=request.GET.get('business_id'))
        orders = OrderInfo.objects.filter(business_id=o1)

        response['list'] = json.loads(serializers.serialize("json", orders))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def show_order_products(request):
    response = {}
    try:
        o1 = OrderInfo.objects.get(id=request.GET.get('order_id'))
        products = OrderProducts.objects.filter(order_id=o1)

        response['list'] = json.loads(serializers.serialize("json", products))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)



def add_order(request):
    response = {}
    try:
        o1 = UserInfo.objects.get(id=request.GET.get('user_id'))

        user_cart = CartItems.objects.filter(user_id=o1)
        items = user_cart.values('product_id').values_list('product_id', flat=True)

        #先找出购物车里涉及的所有商家
        business = []
        for i in items:
            business.append(Product.objects.get(id=i).product_business)

        business = list(set(business))

        # 遍历每个商家，写订单信息
        # 再找购物车里这个商家的所有商品，写一个订单的所有商品信息
        for k in business:
            o2 = k

            orderInfo = OrderInfo(customer_id=o1,
                                  business_id=o2,
                                  # order_createtime = ,

                                  customer_name=o1.user_name,
                                  customer_address=o1.user_address,
                                  customer_mobile=o1.user_mobile,
                                  business_name=o2.user_name,
                                  business_address=o2.user_address,
                                  business_mobile=o2.user_mobile
                                  )
            orderInfo.save()

            for i in user_cart:
                raw_product = Product.objects.get(id=i.product_id.id)
                if(raw_product.product_business==o2):
                    order_items = OrderProducts(order_id=orderInfo,
                                                product_id=i.product_id,
                                                num = i.num,
                                                order_product_cost=raw_product.product_cost)
                    order_items.save()


        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
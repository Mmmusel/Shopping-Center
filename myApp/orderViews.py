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

#http://127.0.0.1:8000/show_business_orderProduct/?business_id=8
def show_business_orderProduct(request):
    response = {}
    try:
        #所有订单
        o1 = UserInfo.objects.get(id=request.GET.get('business_id'))
        orderIds = OrderInfo.objects.filter(business_id=o1).order_by('order_createtime')

        #商家的所有订单 涉及到的用户头像
        userAvatar=[]
        for i in orderIds:
            userAvatar.append(i.customer_id)

        #所有订单涉及到的商品
        orderProduct = []
        nowProduct = []
        for i in orderIds:
            t=OrderProducts.objects.filter(order_id=i)
            orderProduct.extend(t)
            for j in t:
                nowProduct.append(j.product_id)

        #去重
        nowProduct = list(set(nowProduct))

        response['orders'] = json.loads(serializers.serialize("json", orderIds))
        response['orderProducts'] = json.loads(serializers.serialize("json", orderProduct))
        response['nowProduct'] = json.loads(serializers.serialize("json", nowProduct))
        response['userAvatar'] = json.loads(serializers.serialize("json", userAvatar))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def alterOrderStatus(request):
    response = {}
    try:
        order = OrderInfo.objects.get(id=request.GET.get('order_id'))
        order.order_status=request.GET.get('status')
        order.save()


        response['msg'] = 'succes111s'
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
                                  order_status='买家未付款',

                                  customer_name=o1.user_name,
                                  customer_address=o1.user_address,
                                  customer_mobile=o1.user_mobile,
                                  customer_province=o1.user_province,
                                  customer_city=o1.user_city,
                                  customer_area=o1.user_area,


                                  business_name=o2.user_name,
                                  business_address=o2.user_address,
                                  business_mobile=o2.user_mobile,
                                  business_province=o2.user_province,
                                  business_city=o2.user_city,
                                  business_area=o2.user_area
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
from django.core import serializers
from django.http import JsonResponse, HttpResponse


from myApp.models import UserInfo, Product, LikeList,StarList,CheckProduct,UserLog,UserActionLog
import json

def get_users(request):
    response = {}
    try:
        o=UserInfo.objects.filter()
        response['business_lists']=json.loads(serializers.serialize("json", o))
        response['msg'] = 'succes111s'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

def get_check(request):
    response = {}
    try:
        o=CheckProduct.objects.filter(product_status=request.GET.get('product_status')).filter(check_status=request.GET.get('check_status'))
        response['list']=json.loads(serializers.serialize("json", o))
        response['msg'] = 'succes111s'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

def get_has_check(request):
    response = {}
    try:
        o=CheckProduct.objects.filter(check_status=request.GET.get('check_status'))
        response['list']=json.loads(serializers.serialize("json", o))
        response['msg'] = 'succes111s'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

def alterCheckStatus(request):
    response = {}
    try:
        result =request.GET.get('status')
        iid=int(request.GET.get('order_id'))

        o1=CheckProduct.objects.get(id=iid)
        o1.check_status=result
        o1.save()

        pid=o1.product_id.id

        o2=Product.objects.get(id=pid)
        if(result=='通过审核'):
            o2.product_status='上架'
            o2.save()
        if(result=='回退申请'):
            o2.product_status = '下架'
            o2.save()

        response['msg'] = 'succes111s'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


def alterEditCheckStatus(request):
    response = {}
    try:
        result = request.GET.get('status')
        iid = int(request.GET.get('order_id'))

        o1 = CheckProduct.objects.get(id=iid)
        o1.check_status = result
        o1.save()

        pid = o1.product_id.id

        o2 = Product.objects.get(id=pid)
        if (result == '通过审核'):
            o2.product_status = '上架'
            o2.product_name=o1.product_name
            o2.product_cost=o1.product_cost
            o2.product_brand = o1.product_brand
            o2.product_color = o1.product_color
            o2.product_image = o1.product_image
            o2.product_imageDetail = o1.product_imageDetail

            o2.save()


        response['msg'] = 'succes111s'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


def add_log(request):
    response = {}
    try:
        iid=request.GET.get('user_id')
        o1=UserInfo.objects.get(id=iid)
        l=UserLog(
            log_id=o1,

            log_name=o1.user_name,
            log_type=o1.user_type,
            log_province=o1.user_province,
            log_city=o1.user_city,
            log_area=o1.user_area
        )
        l.save()

        response['msg'] = 'succes111s'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


def get_user_log(request):
    response = {}
    try:
        o=UserLog.objects.filter()
        response['list']=json.loads(serializers.serialize("json", o))
        response['msg'] = 'succes111s'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

def get_user_action_log(request):
    response = {}
    try:
        o=UserActionLog.objects.filter()
        response['list']=json.loads(serializers.serialize("json", o))
        response['msg'] = 'succes111s'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

def get_user_action_num(request):
    response = {}
    try:
        from django.db import connection
        with connection.cursor() as cur:
            cur.callproc('testProc3', [0])
            resu = cur.fetchall()
            print(resu[0][0])

        response['num'] = resu[0][0]
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
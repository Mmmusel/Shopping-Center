import struct

from django.http import JsonResponse, HttpResponse
from django.core import serializers


from myApp.models import Book, UserInfo,Product,CartItems,StockInfo,CheckProduct
import json


def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def show_products(request):
    response = {}
    try:
        products = Product.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", products))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def show_customer_products(request):
    response = {}
    try:
        products = Product.objects.filter(product_status='上架')
        response['list'] = json.loads(serializers.serialize("json", products))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def show_searched_products(request):
    response = {}
    try:

        products = Product.objects.filter(product_status='上架').filter(product_name__contains=request.GET.get('search_text'))
        response['list'] = json.loads(serializers.serialize("json", products))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


def add_product(request):
    global product
    iid = int(str(request.FILES.get('user_id').read())[2:-1])
    product_business_obj = UserInfo.objects.get(id=iid)
    product_Info = json.loads(request.FILES.get('forms').read())

    if request.FILES.get('product_image1'):
        product_image1 = request.FILES.get('product_image1')
    else:
        product_image1 = 'avatar/default_pic.jpg'
    if request.FILES.get('product_image2'):
        product_imageDetail1 = request.FILES.get('product_image2')
    else:
        product_imageDetail1 = 'avatar/default_pic.jpg'

    response = {}
    if request.method == 'POST':
        #goods_image = request.FILES.get('goods_image')
        t=0.0
        print(product_Info['product_cost'])
        if product_Info['product_cost'].find('.'):
            t=float(product_Info['product_cost'])
        else:
            t=1.0*int(product_Info['product_cost'])
        product = Product(product_name=product_Info['product_name'],
                          product_brand=product_Info['product_brand'],
                          product_sales=0,
                          product_stock=0,


                          product_cost=t,
                          product_color=product_Info['product_color'],
                          product_image=product_image1,
                          product_imageDetail=product_imageDetail1,
        product_business=product_business_obj,
                          product_status='申请上架'

                          )
        product.save()

        productcheck = CheckProduct(
            product_id=product,
                          product_name=product_Info['product_name'],
                          product_brand=product_Info['product_brand'],


                          product_cost=t,
                          product_color=product_Info['product_color'],
                          product_image=product_image1,
                          product_imageDetail=product_imageDetail1,
                          product_business=product_business_obj,
                          product_status='申请上架',
            check_status='待审核'

                          )
        productcheck.save()
    try:

        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

def delete_product(request):
    response = {}
    try:
        product = Product.objects.filter(id=request.GET.get('product_id'))
        product.product_status='下架'

        cart=CartItems.objects.filter(product_id=product)
        for i in cart:
            i.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def edit_product(request):

    #iid = int(str(request.FILES.get('user_id').read())[2:-1])
    pid = int(str(request.FILES.get('product_id').read())[2:-1])

    #product_business_obj = UserInfo.objects.get(id=iid)
    product_Info = json.loads(request.FILES.get('forms').read())

    p = Product.objects.get(id=pid)


    response = {}
    if request.method == 'POST':

        t=0.0

        if product_Info['product_cost'].find('.'):
            t=float(product_Info['product_cost'])
        else:
            t=1.0*int(product_Info['product_cost'])

        """
        p.product_name=product_Info['product_name']
        p.product_brand=product_Info['product_brand']


        p.product_cost=t
        p.product_color=product_Info['product_color']
        #product_image=request.FILES.get('product_image1')
        #product_imageDetail=request.FILES.get('product_image2')
        if request.FILES.get('product_image1'):
            p.product_image=request.FILES.get('product_image1')
        if request.FILES.get('product_image2'):
            p.product_imageDetail=request.FILES.get('product_image2')

        p.save()
        """

        if request.FILES.get('product_image1'):
            product_image1 = request.FILES.get('product_image1')
        else:
            product_image1=p.product_image
        if request.FILES.get('product_image2'):
            product_imageDetail1 = request.FILES.get('product_image2')
        else:
            product_imageDetail1 = p.product_imageDetail


        productcheck = CheckProduct(
            product_id=p,
            product_name=product_Info['product_name'],
            product_brand=product_Info['product_brand'],

            product_cost=t,
            product_color=product_Info['product_color'],
            product_image=product_image1,
            product_imageDetail=product_imageDetail1,
            product_business=p.product_business,
            product_status='申请修改',
            check_status='待审核'

        )
        productcheck.save()
    try:

        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

def fetch_product(request):
    response = {}
    try:
        product = Product.objects.filter(id=request.GET.get('product_id'))
        response['product'] = json.loads(serializers.serialize("json", product))[0]
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def add_product_stock(request):
    response = {}
    try:
        product = Product.objects.get(id=request.GET.get('product_id'))


        stock=int(request.GET.get('stock'))


        product.product_stock+=stock
        product.save()

        cost = 0.0

        if request.GET.get('cost').find('.'):
            cost = float(request.GET.get('cost'))
        else:
            cost = 1.0 * int(request.GET.get('cost'))


        stockInfo = StockInfo(
                              business_id=product.product_business,
                            product_id=product,
        stock_num = stock,
        stock_cost = cost,
                              business_province=product.product_business.user_province,
                              business_city=product.product_business.user_city,
                              business_area=product.product_business.user_area
                              )
        stockInfo.save()




        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def fetch_stock(request):
    response = {}
    try:
        # 所有订单
        o1 = UserInfo.objects.get(id=request.GET.get('business_id'))
        orderIds = StockInfo.objects.filter(business_id=o1).order_by('stock_createtime')


        response['stock_orders'] = json.loads(serializers.serialize("json", orderIds))


        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)



def add_userInfo(request):
    response = {}
    try:
        userInfo = UserInfo(user_name=request.GET.get('user_name'),
                            user_password=request.GET.get('user_password'),
                            user_type=request.GET.get('user_type'))
        userInfo.save()
        response['msg'] = 'success'
        response['userId'] = userInfo.id
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def search_userInfo(request):
    response = {}
    try:
        userInfo = UserInfo.objects.get(user_name=request.GET.get('user_name'),
                                        user_password=request.GET.get('user_password'))
        response['userId'] = userInfo.id
        response['user_type'] = userInfo.user_type
        response['msg'] = 'succes111s'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

def search_usertype(request):
    response = {}
    try:
        userInfo = UserInfo.objects.get(id=request.GET.get('user_id'))

        response['user_type'] = userInfo.user_type
        response['msg'] = 'succes111s'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

def fetch_userInfo(request):
    response = {}
    try:
        userInfo = UserInfo.objects.get(id=request.GET.get('user_id'))
        userInfoss = UserInfo.objects.filter(id=request.GET.get('user_id'))
        response['user_name'] = userInfo.user_name if userInfo.user_name else ""
        response['user_mobile'] = userInfo.user_mobile if userInfo.user_mobile else ""
        response['user_avatar'] = json.loads(serializers.serialize("json", userInfoss))[0]
        response['user_address'] = userInfo.user_address if userInfo.user_address else ""
        response['user_createtime'] = str(userInfo.user_createtime)
        response['user_province'] = userInfo.user_province if userInfo.user_province else ""
        response['user_city'] = userInfo.user_city if userInfo.user_city else ""
        response['user_area'] = userInfo.user_area if userInfo.user_area else ""
        response['msg'] = 'succes111s'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

"""
def add_product(request):
    global product
    response = {}
    if request.method == 'POST':
        #goods_image = request.FILES.get('goods_image')
        product = Product(product_name="1",
                          product_brand="1",
                          product_sales=1,
                          product_cost=1.1,
                          product_color="",
                          product_image=request.FILES.get('goods_image')
                          #product_image=request.FILES.get('goods_image2')
                          )
        product.save()
    try:
        # avatar/705728-20160424234825491-384470376_1CaALm3.png
        response['image'] = str(product.product_image)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
"""
def edit_userInfo(request):
    response = {}
    global userInfo
    print("111")
    iid=int(str(request.FILES.get('user_id').read())[2:-1])


    try:

        print(iid)
        userInfo = UserInfo.objects.get(id=iid)
        print(iid)

        save_userInfo = json.loads(request.FILES.get('forms').read())
        same_name = UserInfo.objects.filter(user_name=save_userInfo['user_name'])
        if(same_name.count()==2):
            response['msg'] = "用户名重复"
            response['error_num'] = 1
            return JsonResponse(response)
        elif same_name.count()==1:
            if str(same_name[0].id)!=str(iid):
                print("name1:",str(same_name[0].id))
                print("name2:", str(iid))
                response['msg'] = "用户名重复"
                response['error_num'] = 1
                return JsonResponse(response)


        userInfo.user_name=save_userInfo['user_name']
        userInfo.user_address=save_userInfo['user_address']
        userInfo.user_mobile=save_userInfo['user_mobile']

        if request.FILES.get('user_image'):
            userInfo.user_avatar=request.FILES.get('user_image')

        save_addrInfo = json.loads(request.FILES.get('selectAddr').read())
        userInfo.user_province=save_addrInfo['province']
        userInfo.user_city=save_addrInfo['city']
        userInfo.user_area=save_addrInfo['area']

        userInfo.save()

        response['image'] = str(userInfo.user_avatar)
        response['msg'] = 'succes111s'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)



def userId2userName(request):
    response = {}
    try:
        userInfo = UserInfo.objects.get(id=request.GET.get('user_id'))
        response['user_name'] = userInfo.user_name
        response['msg'] = 'succes111s'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

def edit_password(request):
    response = {}
    try:
        userInfo = UserInfo.objects.filter(id=request.GET.get('user_id'),user_password=request.GET.get('old_password'))
        if(userInfo.count()==0):
            response['msg'] = 'succes111s'
            response['error_num'] = -1

        else:
            u=userInfo[0]
            u.user_password=request.GET.get('new_password')
            u.save()
            response['msg'] = 'succes111s'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

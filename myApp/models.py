from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

class UserInfo(models.Model):
    user_name = models.CharField(max_length=64,unique=True)
    user_password = models.CharField(max_length=64)

    user_type = models.CharField(max_length=10,null=True)

    user_address = models.CharField(max_length=64,null=True)
    user_mobile = models.CharField(max_length=64, null=True)
    user_avatar = models.ImageField(upload_to="user_avatar/",null=True)
    user_createtime = models.DateField(auto_now_add=True,null=True)

    user_province = models.CharField(max_length=16,null=True)
    user_city = models.CharField(max_length=16, null=True)
    user_area = models.CharField(max_length=16, null=True)


class OrderInfo(models.Model):
    customer_id = models.ForeignKey("UserInfo", related_name='customer',on_delete=models.CASCADE)
    business_id = models.ForeignKey("UserInfo", related_name='business',on_delete=models.CASCADE)
    order_createtime = models.DateTimeField(auto_now_add=True)

    customer_name = models.CharField(max_length=64)
    customer_address = models.CharField(max_length=64)
    customer_mobile = models.CharField(max_length=64)
    customer_province = models.CharField(max_length=16, null=True)
    customer_city = models.CharField(max_length=16, null=True)
    customer_area = models.CharField(max_length=16, null=True)


    business_name = models.CharField(max_length=64)
    business_address = models.CharField(max_length=64)
    business_mobile = models.CharField(max_length=64)
    business_province = models.CharField(max_length=16, null=True)
    business_city = models.CharField(max_length=16, null=True)
    business_area = models.CharField(max_length=16, null=True)

class OrderProducts(models.Model):
    order_id = models.ForeignKey("OrderInfo", on_delete=models.CASCADE)
    product_id = models.ForeignKey("Product", on_delete=models.CASCADE)

    num = models.IntegerField()
    order_product_cost = models.DecimalField(max_digits=9, decimal_places=2)

class CartItems(models.Model):
    user_id = models.ForeignKey("UserInfo",on_delete=models.CASCADE)
    product_id = models.ForeignKey("Product",on_delete=models.CASCADE)
    num = models.IntegerField()


class Product(models.Model):
    product_name = models.CharField(max_length = 100)
    product_brand = models.CharField(max_length=100)
    product_cost = models.DecimalField(max_digits=9, decimal_places=2)
    product_sales = models.IntegerField()
    product_color = models.CharField(max_length = 20)
    product_image = models.ImageField(upload_to="avatar/")
    product_imageDetail = models.ImageField(upload_to="avatar/")

    product_business=models.ForeignKey("UserInfo",on_delete=models.CASCADE,null=True)
    product_stock=models.IntegerField(null=True)

    """
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return '/media/default/user.jpg'

    photo_295_413 = ImageSpecField(  # 注意：ImageSpecField 不会生成数据库表的字段
        source='photo',
        processors=[ResizeToFill(295, 413)],  # 处理成一寸照片的大小
        format='JPEG',  # 处理后的图片格式
        options={'quality': 95}  # 处理后的图片质量
    )

    def photo_295_413_url(self):
        if self.photo_295_413 and hasattr(self.photo_295_413, 'url'):
            return self.photo_295_413.url
        else:
            return '/media/default/user.jpg'
    
    """
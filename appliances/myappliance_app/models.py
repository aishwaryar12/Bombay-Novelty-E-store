from django.db import models


class UserRegistration(models.Model):
    Firstname = models.CharField(default='', max_length=200)
    Lastname = models.CharField(default='', max_length=200)
    Gender = models.CharField(max_length=100)
    Address = models.CharField(max_length=400)
    City = models.CharField(max_length=100)
    Pincode = models.IntegerField(null=True,blank=True)
    MobileNumber = models.CharField(max_length=10)
    EmailID = models.EmailField(max_length=100)
    Password = models.CharField(max_length=50)
    ConfirmPassword = models.CharField(max_length=50)

class UserLogin(models.Model):
    emailid = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    utype = models.CharField(max_length=50)

class ProCategory(models.Model):
    cat_name = models.CharField(default='', max_length=200)

class Product(models.Model):
    pname = models.CharField(default='', max_length=200)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image1 = models.FileField(upload_to='documents/')
    price = models.IntegerField(null=True, blank=True)
    gst = models.IntegerField(null=True, blank=True)
    cgst = models.IntegerField(null=True, blank=True)
    sgst = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)

class StockItems(models.Model):
    transaction_no = models.CharField(max_length=200)
    Itemname = models.CharField(max_length=200)
    price = models.IntegerField(null=True, blank=True)
    gst = models.IntegerField(null=True, blank=True)
    cgst = models.IntegerField(null=True, blank=True)
    sgst = models.IntegerField(null=True, blank=True)
    transport_charges = models.IntegerField(null=True, blank=True)
    sdate = models.DateField(auto_now_add=True)
    total = models.IntegerField(null=True, blank=True)
    sold_out = models.IntegerField(null=True, blank=True)
    availability = models.IntegerField(null=True, blank=True)

class Supplier(models.Model):
    supplier_name = models.CharField(default='', max_length=200)
    address = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField(null=True, blank=True)


class Billing(models.Model):
    orderid = models.IntegerField(null=True, blank=True)
    customersid = models.EmailField(null=True, blank=True)
    bill_date = models.DateField(auto_now_add=True)
    items = models.CharField(default='', max_length=200)
    total = models.IntegerField(null=True, blank=True)
    gst = models.IntegerField(null=True, blank=True)
    tax_total = models.IntegerField(null=True, blank=True)
    shipping_charge = models.IntegerField(null=True, blank=True)
    grandtotal = models.IntegerField(null=True, blank=True)

class Payment(models.Model):
    Paymenttype = models.CharField(default='', max_length=200)
    BankName = models.CharField(default='', max_length=200)
    Amount = models.IntegerField(null=True, blank=True)
    Paymentdate = models.DateField(auto_now_add=True)

class Deliverydtails(models.Model):
    Deliverydate = models.DateField(auto_now_add=True)
    Trackingno = models.CharField(max_length=200)
    Packingstatus = models.CharField(max_length=200)
    Shippingstatus = models.CharField(max_length=200)
    Delivery_status = models.CharField(max_length=200)

class Purchase_Items(models.Model):
    pitem = models.CharField(default='', max_length=200)
    pprice = models.IntegerField(null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Purchase_date = models.DateField(auto_now_add=True)
    Total_price = models.IntegerField(null=True, blank=True)

class order_details(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(null=True, blank=True)
    unitprice = models.IntegerField(null=True, blank=True)
    Total = models.IntegerField(null=True, blank=True)
    uid = models.CharField(max_length=50, null=True)
    items = models.CharField(max_length=50, null=True)
    Amonth = models.IntegerField(null=True, blank=True)
    Ayear = models.IntegerField(null=True, blank=True)

class MB_scheme(models.Model):
    id = models.AutoField(primary_key=True)
    Schemeno = models.CharField(max_length=200)
    Customer_name = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    Email_Id = models.EmailField(max_length=200)
    Mobileno = models.CharField(max_length=200)
    Month = models.CharField(max_length=200)
    Winner = models.CharField(max_length=200)
    Coupon_code = models.CharField(max_length=200)

class ExchangeOffer(models.Model):
    exchngname = models.CharField(default='', max_length=200)
    dscrptn = models.CharField(max_length=500)
    discount = models.IntegerField(null=True, blank=True)
    Start_date = models.DateField(auto_now_add=True)
    finish_date = models.DateField(auto_now_add=True)
    coupon_code = models.CharField(max_length=200)

class Service(models.Model):
    Product_name = models.CharField(default='', max_length=200)
    Description = models.CharField(max_length=500)
    Price = models.IntegerField(null=True, blank=True)
    Service_men_name = models.CharField(default='', max_length=200)
    Service_men_Mbno = models.CharField(max_length=200)

class FeedBackForm(models.Model):
    userid = models.EmailField(max_length=200)
    servicefeedback = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)

class cart_details(models.Model):
    userid = models.CharField(default='', max_length=200)
    productname = models.CharField(default='', max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(default='', max_length=200)
    unitprice = models.IntegerField(null=True, blank=True)
    Total = models.IntegerField(null=True, blank=True)



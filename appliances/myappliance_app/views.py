from django.shortcuts import render
from django.db.models import Avg, Max, Min, Sum
from  myappliance_app.models import UserRegistration
from  myappliance_app.models import UserLogin
from  myappliance_app.models import ProCategory
from  myappliance_app.models import ExchangeOffer
from  myappliance_app.models import Supplier
from  myappliance_app.models import Purchase_Items
from  myappliance_app.models import StockItems
from  myappliance_app.models import Product
from  myappliance_app.models import Service
from  myappliance_app.models import MB_scheme
from  myappliance_app.models import order_details
from  myappliance_app.models import FeedBackForm
from  myappliance_app.models import Billing
from  myappliance_app.models import Payment
from  myappliance_app.models import cart_details

import datetime
import os
import smtplib
from django.core.files.storage import FileSystemStorage
from appliances.settings import BASE_DIR

# Create your views here.
def index(request):
    user_dict = Product.objects.all()
    prod_cat = ProCategory.objects.all()
    prod_list = Product.objects.all()
    #return render(request, 'index.html')
    return render(request, 'index.html', {'user_dict': user_dict, 'prod_cat': prod_cat, 'prod_list': prod_list })

def admins(request):
    user_dict = ''
    return render(request, 'admin_home.html', {'user_dict': user_dict})

def customers(request):
    user_dict = Product.objects.all()
    prod_cat = ProCategory.objects.all()
    prod_list = Product.objects.all()
    return render(request, 'customer_home.html', {'user_dict': user_dict, 'prod_cat': prod_cat, 'prod_list': prod_list, 'msg':'payment has been done successfully!'})

def customers_next(request):
    emailid = request.session['uid']
    content = "Bombay Novelty E-store--hello your order has been placed successfully! Your order will be delivered within two days. thank you "
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('priyankavrokhade@gmail.com', '789@pink@cool')
    mail.sendmail('priyankavrokhade@gmail.com', emailid, content)
    mail.close()

    prod_cat = ProCategory.objects.all()

    return render(request, 'customer_home.html', {'prod_cat': prod_cat, 'msg':'payment has been done successfully!'})
    return render(request, 'send_email.html')


def signup(request):
    user_dict = {'msg': 'login successfull!'}
    if request.method == "POST":
        Firstname = request.POST.get('t1','')
        Lastname = request.POST.get('t2','')
        Gender= request.POST.get('t3','')
        Address = request.POST.get('t4','')
        City = request.POST.get('t5','')
        Pincode = request.POST.get('t6','')
        MobileNumber = request.POST.get('t7','')
        EmailID = request.POST.get('t8','')
        Password = request.POST.get('t9','')
        ConfirmPassword = request.POST.get('t10','')
        #UserRegistration.Password(form.cleaned_data['Password'])

        UserRegistration.objects.create(Firstname=Firstname, Lastname=Lastname, Gender=Gender, Address=Address, City=City, Pincode=Pincode, MobileNumber=MobileNumber, EmailID=EmailID, Password=Password, ConfirmPassword=ConfirmPassword)
        UserLogin.objects.create(emailid=EmailID, password=Password, utype='customer')
        prod_cat = ProCategory.objects.all()
        return render(request, 'index.html', {'user_dict':user_dict, 'prod_cat':prod_cat})
    prod_cat = ProCategory.objects.all()

    return render(request, 'index.html', {'prod_cat':prod_cat })

def sampleview(request):
    user_dict = UserRegistration.objects.all()
    return render(request, 'sampleview.html', {'user_dict': user_dict})

def remove_items(request):
    if request.method == 'POST':
        userdata = UserRegistration.objects.all()
        id = request.POST.get('id')
        useritem = UserRegistration.objects.get(id=id)

        useritem.delete()
        useritem = UserRegistration.objects.all()
    return render(request, 'sampleview.html', context={'user_dict': useritem})


def update_items(request):
        if request.method == 'POST':
            userdata = UserRegistration.objects.all()
            id = request.POST.get('id')
            useritem = UserRegistration.objects.filter(id=id).values()
            return render(request, 'sampleedit.html', {'useritem': useritem})

def reg_db(request):
    if request.method == "POST":
        userdata = UserRegistration.objects.all()
        id = request.POST.get('id')
        useritem = UserRegistration.objects.filter(id=id).values()
        Firstname = request.POST.get('t1', '')
        Lastname = request.POST.get('t2', '')
        Gender = request.POST.get('t3', '')
        Address = request.POST.get('t4', '')
        City = request.POST.get('t5', '')
        Pincode = request.POST.get('t6', '')
        MobileNumber = request.POST.get('t7', '')
        EmailID = request.POST.get('t8', '')
        Password = request.POST.get('t9', '')
        ConfirmPassword = request.POST.get('t10', '')

        UserRegistration.objects.filter(id=id).update(Firstname=Firstname, Lastname=Lastname, Gender=Gender, Address=Address,
                                        City=City, Pincode=Pincode, MobileNumber=MobileNumber, EmailID=EmailID,
                                        Password=Password, ConfirmPassword=ConfirmPassword)
        useritem = UserRegistration.objects.all()
    return render(request, 'sampleview.html', context={'user_dict': useritem})

def signin(request):
    user_dict = {'msg': 'login successfull!'}
    if request.method == "POST":
        emailid = request.POST.get('Email', '')
        #uid = u['emailid']
        request.session['uid'] = emailid
        password = request.POST.get('ps', '')
        checklogin = UserLogin.objects.filter(emailid=emailid).count()
        if checklogin >= 1:
                user = UserLogin.objects.filter(emailid=emailid).values()
                for u in user:
                    upass = u['password']
                    utype = u['utype']
                    if upass == password:
                        if utype == "customer":
                            prod_cat = ProCategory.objects.all()
                            prolist = Product.objects.all()
                            return render(request, 'customer_home.html', {'prod_cat': prod_cat,'prolist':prolist,'msg':'login successfull!'})

                        if utype == "admin":
                            prod_cat = ProCategory.objects.all()
                            return render(request, 'admin_home.html', {'prod_cat': prod_cat, 'msg':'login successfull!'})
                    else:
                        return render(request, 'index.html', {'msg': 'invalid password'})
        else:
                    return render(request, 'index.html', {'msg': 'invalid username'})
    prod_cat = ProCategory.objects.all()

    return render(request, 'index.html', {'prod_cat': prod_cat})

def forgotpass(request):
    if request.method == "POST":
        uname = request.POST.get('a1')
        user = UserLogin.objects.filter(emailid=uname).count()
        if user >= 1:
            userlog = UserLogin.objects.filter(emailid=uname).values()
            for u in userlog:
                upass = u['password']
                content = upass
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login('priyankavrokhade@gmail.com', '789@pink@cool')
                mail.sendmail('priyankavrokhade@gmail.com', uname, content)
                mail.close()
                return render(request, 'forgotpassword.html', {'msg': 'your password has been sent to your email id'})
        else:
                return render(request, 'forgotpassword.html', {'msg': 'enter a valid username'})
    return render(request, 'forgotpassword.html')


def Category(request):
    user_dict = {'msg': 'one record inserted successfully'}
    if request.method == "POST":
        cname = request.POST.get('p2', '')
        ProCategory.objects.create(cat_name=cname)
        return render(request, 'admin_home.html', context=user_dict)
    prod_cat = ProCategory.objects.all()

    return render(request, 'Category.html', {'prod_cat': prod_cat, 'user_dict': user_dict})

def categoryview(request):
    user_dict = ProCategory.objects.all()
    prod_cat = ProCategory.objects.all()
    prod_list = Product.objects.all()
    return render(request, 'categoryview.html', {'prod_cat': prod_cat, 'prod_list': prod_list, 'user_dict': user_dict})

def catremove_items(request):
    if request.method == 'POST':
        userdatas = ProCategory.objects.all()
        id = request.POST.get('id')
        useritems = ProCategory.objects.get(id=id)

        useritems.delete()
        useritems = ProCategory.objects.all()
    return render(request,'categoryview.html',context={'user_dict': useritems})

def catupdate_items(request):
    if request.method == 'POST':
        userdatas = ProCategory.objects.all()
        id = request.POST.get('id')
        useritems = ProCategory.objects.filter(id=id).values()
        return render(request, 'catedit.html', {'useritems': useritems})

def cat_db(request):
    if request.method == "POST":
        userdatas = ProCategory.objects.all()
        id = request.POST.get('id')
        useritems = ProCategory.objects.filter(id=id).values()
        cname = request.POST.get('p2', '')
        ProCategory.objects.filter(id=id).update(cat_name=cname)
        useritems = ProCategory.objects.all()
    return render(request, 'categoryview.html', context={'user_dict': useritems})


def supplier(request):
    user_dict = {'msg': 'one record inserted successfully'}
    if request.method == "POST":
        p1 = request.POST.get('r1')
        p2 = request.POST.get('r2')
        p3 = request.POST.get('r3')
        p4 = request.POST.get('r4')
        p5 = request.POST.get('r5')
        p6 = request.POST.get('r6')
        print(p1)
        Supplier.objects.get_or_create(supplier_name=p1, address=p2, mobile_no=p3, email=p4, product_name=p5, quantity=p6)
        return render(request, 'admin_home.html', context=user_dict)
    return render(request,'supplier.html')

def supplierview(request):
    user_dict = Supplier.objects.all()
    return render(request, 'supplierview.html', {'user_dict': user_dict})

def supremove_items(request):
    if request.method == 'POST':
        userdatas = Supplier.objects.all()
        id = request.POST.get('id')
        useritems = Supplier.objects.get(id=id)

        useritems.delete()
        useritems = Supplier.objects.all()
    return render(request,'supplierview.html',context={'user_dict': useritems})

def supupdate_items(request):
    if request.method == 'POST':
        userdatas = Supplier.objects.all()
        id = request.POST.get('id')
        useritems = Supplier.objects.filter(id=id).values()
        return render(request, 'supplieredit.html', {'useritems': useritems})

def sup_db(request):
    if request.method == "POST":
        userdatas = Supplier.objects.all()
        id = request.POST.get('id')
        useritems = Supplier.objects.filter(id=id).values()
        supplier_name = request.POST.get('r1', '')
        address = request.POST.get('r2', '')
        mobile_no = request.POST.get('r3', '')
        email = request.POST.get('r4', '')
        product_name = request.POST.get('r5', '')
        quantity = request.POST.get('r6', '')
        Supplier.objects.filter(id=id).update(supplier_name=supplier_name, address=address, mobile_no=mobile_no, email=email, product_name=product_name, quantity=quantity )
        useritems = Supplier.objects.all()
    return render(request, 'supplierview.html', context={'user_dict': useritems})


def purchase(request):
    user_dict = {'msg': 'one record inserted successfully'}
    if request.method == "POST":
        pitem = request.POST.get('o4', '')
        pprice = request.POST.get('o5', '')
        Quantity = request.POST.get('o1', '')
        Purchase_date = request.POST.get('o2', '')
        Total_price = request.POST.get('o3', '')
        Purchase_Items.objects.create(pitem=pitem, pprice=pprice, Quantity=Quantity, Purchase_date=Purchase_date, Total_price=Total_price )
        return render(request, 'admin_home.html', context=user_dict)
    return render(request, 'Purchase_Items.html')

def purchaseview(request):
    user_dict = Purchase_Items.objects.all()
    return render(request, 'purchaseview.html', {'user_dict': user_dict})

def purremove_items(request):
    if request.method == 'POST':
        userdatas = Purchase_Items.objects.all()
        id = request.POST.get('id')
        user_items = Purchase_Items.objects.get(id=id)

        user_items.delete()
        user_items = Purchase_Items.objects.all()
    return render(request,'purchaseview.html', context={'user_dict': user_items})

def purupdate_items(request):
    if request.method == 'POST':
        userdatas = Purchase_Items.objects.all()
        id = request.POST.get('id')
        user_items = Purchase_Items.objects.filter(id=id).values()
        return render(request, 'purchaseedit.html', {'user_items': user_items})

def pur_db(request):
    if request.method == "POST":
        userdatas = Purchase_Items.objects.all()
        id = request.POST.get('id')
        user_items = Purchase_Items.objects.filter(id=id).values()
        pitem = request.POST.get('o4','')
        pprice = request.POST.get('o5','')
        Quantity = request.POST.get('o1', '')
        Purchase_date = request.POST.get('o2', '')
        Total_price = request.POST.get('o3', '')

        Purchase_Items.objects.filter(id=id).update(pitem=pitem, pprice=pprice, Quantity=Quantity, Purchase_date=Purchase_date, Total_price=Total_price)
        user_items = Purchase_Items.objects.all()
    return render(request, 'purchaseview.html', context={'user_dict': user_items})

def stock(request):
    user_dict = {'msg': 'one record inserted successfully'}
    if request.method == "POST":
        transaction_no = request.POST.get('q1', '')
        price = request.POST.get('q2', '')
        gst = request.POST.get('q3', '')
        cgst = request.POST.get('q4', '')
        sgst = request.POST.get('q5', '')
        transport_charges = request.POST.get('q6', '')
        sdate = request.POST.get('q7')
        total = request.POST.get('q8', '')
        sold_out = request.POST.get('q9', '')
        availability = request.POST.get('q10', '')
        Itemname = request.POST.get('q12', '')

        StockItems.objects.create(transaction_no=transaction_no, Itemname=Itemname, price=price, gst=gst, cgst=cgst, sgst=sgst, transport_charges=transport_charges, total=total, sdate=sdate, sold_out=sold_out, availability=availability)
        return render(request, 'admin_home.html', context=user_dict)
    return render(request,'Stock_Items.html')

def stockview(request):
    user_dict = StockItems.objects.all()
    return render(request, 'stockview.html', {'user_dict': user_dict})

def stkremove_items(request):
    if request.method == 'POST':
        userdatas = StockItems.objects.all()
        id = request.POST.get('id')
        useritems = StockItems.objects.get(id=id)

        useritems.delete()
        user_items = StockItems.objects.all()
    return render(request,'stockview.html',context={'user_dict': user_items})

def stkupdate_items(request):
    if request.method == 'POST':
        userdatas = StockItems.objects.all()
        id = request.POST.get('id')
        useritems = StockItems.objects.filter(id=id).values()
        return render(request, 'stockedit.html', {'useritems': useritems})

def stk_db(request):
    if request.method == "POST":
        userdatas = StockItems.objects.all()
        id = request.POST.get('id')
        useritems = StockItems.objects.filter(id=id).values()
        transaction_no = request.POST.get('q1', '')
        Itemname = request.POST.get('q12', '')
        price = request.POST.get('q2', '')
        gst = request.POST.get('q3', '')
        cgst = request.POST.get('q4', '')
        sgst = request.POST.get('q5', '')
        transport_charges = request.POST.get('q6', '')
        sdate = request.POST.get('q7', '')
        total = request.POST.get('q8', '')
        sold_out = request.POST.get('q9', '')
        availability = request.POST.get('q10', '')
        StockItems.objects.filter(id=id).update(transaction_no=transaction_no, Itemname=Itemname,  price=price, gst=gst, cgst=cgst, sgst=sgst, transport_charges=transport_charges, sdate=sdate, total=total, sold_out=sold_out, availability=availability )
        user_items = StockItems.objects.all()
    return render(request, 'stockview.html', context={'user_dict': user_items})

def exchange(request):
    user_dict = {'msg': 'one record inserted successfully'}
    if request.method == "POST":
        pname = request.POST.get('s1')
        p2 = request.POST.get('n2')
        p3 = request.POST.get('n3')
        p4 = request.POST.get('n4')
        p5 = request.POST.get('n5')
        p6 = request.POST.get('n6')
        ExchangeOffer.objects.create(exchngname=pname, dscrptn=p2, discount=p3, Start_date=p4, finish_date=p5, coupon_code=p6)
        eoffer_data = ExchangeOffer.objects.all()
        return render(request, 'admin_home.html', {'user_dict':eoffer_data})
    ex_offer = Product.objects.all()
    prod_cat = ProCategory.objects.all()
    prod_list = Product.objects.all()
    return render(request, 'Exchange_Offer.html', {'prod_list':ex_offer, 'prod_cat': prod_cat, 'prod_list':prod_list })

def exchangeview(request):
    user_dict = ExchangeOffer.objects.all()
    return render(request, 'exchangeview.html', {'user_dict': user_dict})

def exchgremove_items(request):
    if request.method == 'POST':
        userdata = ExchangeOffer.objects.all()
        id = request.POST.get('id')
        useritem = ExchangeOffer.objects.get(id=id)

        useritem.delete()
        user_item = ExchangeOffer.objects.all()
    return render(request,'exchangeview.html',context={'user_dict': user_item})

def exchgupdate_items(request):
    if request.method == 'POST':
        userdata = ExchangeOffer.objects.all()
        id = request.POST.get('id')
        useritem = ExchangeOffer.objects.filter(id=id).values()
        return render(request, 'exchangeedit.html', {'useritem': useritem})

def ex_db(request):
    if request.method == "POST":
        userdata = ExchangeOffer.objects.all()
        id = request.POST.get('id')
        useritem = ExchangeOffer.objects.filter(id=id).values()
        exchngname = request.POST.get('n1', '')
        dscrptn = request.POST.get('n2', '')
        discount = request.POST.get('n3', '')
        Start_date = request.POST.get('n4', '')
        finish_date = request.POST.get('n5', '')
        coupon_code = request.POST.get('n6', '')
        ExchangeOffer.objects.filter(id=id).update(exchngname=exchngname, dscrptn=dscrptn, discount=discount, Start_date=Start_date, finish_date=finish_date, coupon_code=coupon_code )
        user_item = ExchangeOffer.objects.all()
    return render(request, 'exchangeview.html', context={'user_dict': user_item})

def product(request):
    user_dict = {'msg': 'one record inserted successfully'}
    if request.method == "POST":
        cat_name = request.POST.get('p2','')
        pname = request.POST.get('s1', '')
        description = request.POST.get('s2','')
        image1 = request.FILES['s3']
        fs = FileSystemStorage()
        filename = fs.save(image1.name, image1)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/'+filename)
        price = request.POST.get('s4', '')

        gst = request.POST.get('s6', '')
        cgst = request.POST.get('s7', '')
        sgst = request.POST.get('s8', '')
        total = request.POST.get('s9', '')
        discount = request.POST.get('s10', '')

        Product.objects.create(pname=pname, description=description, image1=image1, price=price, gst=gst, cgst=cgst, sgst=sgst, total=total, discount=discount,category=cat_name)
        return render(request, 'admin_home.html', context=user_dict)
    prod_list = ProCategory.objects.all()
    return render(request,'product.html', {'prod_list': prod_list})

def productview(request):
    user_dict = Product.objects.all()
    return render(request, 'productview.html', {'user_dict': user_dict})

def proremove_items(request):
    if request.method == 'POST':
        userdatas = Product.objects.all()
        id = request.POST.get('id')
        user_items = Product.objects.get(id=id)

        user_items.delete()
        user_items = Product.objects.all()
    return render(request,'productview.html',context={'user_dict': user_items})

def proupdate_items(request):
    if request.method == 'POST':
        userdatas = Product.objects.all()
        id = request.POST.get('id')
        user_items = Product.objects.filter(id=id).values()
        return render(request, 'productedit.html', {'user_items': user_items})

def pro_db(request):
    if request.method == "POST":
        userdatas = Supplier.objects.all()
        id = request.POST.get('id')
        user_items = Product.objects.filter(id=id).values()
        pname = request.POST.get('s1', '')
        description = request.POST.get('s2', '')
        image1 = request.POST.get('s3', '')
        price = request.POST.get('s4', '')

        gst = request.POST.get('s6', '')
        cgst = request.POST.get('s7', '')
        sgst = request.POST.get('s8', '')
        total = request.POST.get('s9', '')
        discount = request.POST.get('s10', '')
        Product.objects.filter(id=id).update(pname=pname, description=description, image1=image1,
                                             price=price,  gst=gst, cgst=cgst, sgst=sgst, total=total, discount=discount  )
        user_items = Product.objects.all()
    return render(request, 'productview.html', context={'user_dict': user_items})

def service(request):
    user_dict = {'msg': 'one record inserted successfully'}
    if request.method == "POST":
        Product_name = request.POST.get('m1', '')
        Description = request.POST.get('m2', '')
        Price = request.POST.get('m3', '')
        Service_men_name = request.POST.get('m4', '')
        Service_men_Mbno = request.POST.get('m5', '')
        Service.objects.create(Product_name=Product_name, Description=Description, Price=Price,
                               Service_men_name=+Service_men_name, Service_men_Mbno=Service_men_Mbno)
        return render(request, 'admin_home.html', context=user_dict)

    prod_cat = ProCategory.objects.all()
    prod_list = Product.objects.all()
    return render(request, 'Service.html', {'user_dict': user_dict, 'prod_cat': prod_cat, 'prod_list': prod_list})

def serviceview(request):
    user_dict = Service.objects.all()
    return render(request, 'serviceview.html', {'user_dict': user_dict})

def serremove_items(request):
    if request.method == 'POST':
        userdatas = Service.objects.all()
        id = request.POST.get('id')
        useritems = Service.objects.get(id=id)

        useritems.delete()
        user_items = Service.objects.all()
    return render(request,'serviceview.html',context={'user_dict': user_items})

def serupdate_items(request):
    if request.method == 'POST':
        userdatas = Service.objects.all()
        id = request.POST.get('id')
        useritems = Service.objects.filter(id=id).values()
        return render(request, 'serviceedit.html', {'useritems': useritems})

def ser_db(request):
    if request.method == "POST":
        userdatas = Service.objects.all()
        id = request.POST.get('id')
        useritems = Service.objects.filter(id=id).values()
        Product_name = request.POST.get('m1', '')
        Description = request.POST.get('m2', '')
        Price = request.POST.get('m3', '')
        Service_men_name = request.POST.get('m4', '')
        Service_men_Mbno = request.POST.get('m5', '')
        Service.objects.filter(id=id).update(Product_name=Product_name, Description=Description, Price=Price, Service_men_name=Service_men_name, Service_men_Mbno=Service_men_Mbno)
        user_items = Service.objects.all()
    return render(request, 'serviceview.html', context={'user_dict': user_items})

def mbscheme(request):
    user_dict = {'msg': 'one record inserted successfully'}
    if request.method == "POST":
        Schemeno = request.POST.get('l1', '')
        Customer_name = request.POST.get('l2', '')
        Address = request.POST.get('l3', '')
        Email_Id = request.POST.get('l4', '')
        Mobileno = request.POST.get('l5', '')
        Month = request.POST.get('l6', '')
        Winner = request.POST.get('l7', '')
        Coupon_code = request.POST.get('l8', '')

        MB_scheme.objects.create(Schemeno=Schemeno, Customer_name=Customer_name, Address=Address, Email_Id=Email_Id, Mobileno=Mobileno, Month=Month, Winner=Winner, Coupon_code=Coupon_code)
        return render(request, 'customer_home.html', context=user_dict)
    return render(request,'mbscheme.html')

def mbschemeview(request):
    user_dict = MB_scheme.objects.all()
    return render(request, 'mbschemeview.html', {'user_dict': user_dict})

def mbsremove_items(request):
    if request.method == 'POST':
        userdatas = MB_scheme.objects.all()
        id = request.POST.get('id')
        useritems = MB_scheme.objects.get(id=id)

        useritems.delete()
        user_items = MB_scheme.objects.all()
    return render(request,'mbschemeview.html',context={'user_dict': user_items})

def mbsupdate_items(request):
    if request.method == 'POST':
        userdatas = MB_scheme.objects.all()
        id = request.POST.get('id')
        useritems = MB_scheme.objects.filter(id=id).values()
        return render(request, 'mbschemeedit.html', {'useritems': useritems})

def mbs_db(request):
    if request.method == "POST":
        userdatas = MB_scheme.objects.all()
        id = request.POST.get('id')
        useritems = MB_scheme.objects.filter(id=id).values()
        Schemeno = request.POST.get('l1', '')
        Customer_name = request.POST.get('l2', '')
        Address = request.POST.get('l3', '')
        Email_Id = request.POST.get('l4', '')
        Mobileno = request.POST.get('l5', '')
        Month = request.POST.get('l6', '')
        Winner = request.POST.get('l7', '')
        Coupon_code = request.POST.get('l8', '')

        MB_scheme.objects.filter(id=id).update(Schemeno=Schemeno, Customer_name=Customer_name, Address=Address, Email_Id=Email_Id, Mobileno=Mobileno, Month=Month, Winner=Winner, Coupon_code=Coupon_code)
        user_items = MB_scheme.objects.all()
    return render(request, 'mbschemeview.html', context={'user_dict': user_items})



def changepassword(request):
    user_dict = {'msg': 'one record inserted successfully'}
    if request.method == "POST":
        uname = request.POST.get('t1','')
        upass = request.POST.get('t2','')
        newpass = request.POST.get('t3','')
        confirmpass = request.POST.get('t4','')

        ucheck = UserLogin.objects.filter(emailid=uname).values()
        for a in ucheck:
            u = a['emailid']
            p = a['password']
            if u == uname and upass == p:
                if newpass == confirmpass:
                    UserLogin.objects.filter(emailid=uname).update(password=newpass)
                else:
                    return render(request,'changepassword.html', context={'msg':'both must be same'})
            else:
                return render(request, 'changepassword.html', context={'msg':'invalid username or password'})
    return render(request, 'changepassword.html')


def procustomerview(request):
    user_dict = Product.objects.all()
    prod_cat = ProCategory.objects.all()

    return render(request, 'product_view_customer.html', context={'prod_cat':prod_cat, 'user_dict': user_dict})

def procustomerview_cat(request, pk):

    catid= ProCategory.objects.get(id=pk)
    b = catid.cat_name
    user_dict = Product.objects.filter(category=b)
    prod_cat = ProCategory.objects.all()
    return render(request, 'product_view_customer.html', context={'prod_cat':prod_cat, 'user_dict': user_dict})

def porder(request):
    emailid = request.session['uid']
    today = ""
    quantity = ""
    unitprice = ""
    pname = ""

    if request.method == "POST":
        pid = request.POST.get('pid')
        quantity = request.POST.get('c3')
        now = datetime.datetime.now()
        today = now.strftime("%Y-%m-%d")
        uuprice = Product.objects.filter(id=pid).values()
        for p in uuprice:
            unitprice = p['price']
            print(unitprice)
            pname = p['pname']

    return render(request, 'order.html', {'use': today, 'qtty': quantity, 'ss': unitprice, 'user_dict': emailid, 'pp': pname})

def Orderview(request):
    user_dict = order_details.objects.all()
    prod_cat = ProCategory.objects.all()
    prod_list = Product.objects.all()
    return render(request, 'orderview.html', {'prod_cat': prod_cat, 'prod_list':prod_list, 'user_dict': user_dict})

def odelete(request):
    if request.method == 'POST':
        userdatas = order_details.objects.all()
        id = request.POST.get('id')
        useritems = order_details.objects.get(id=id)

        useritems.delete()
        user_items = order_details.objects.all()
    return render(request,'orderview.html',context={'user_dict': user_items})

def order_next(request):

    if request.method=="POST":
        order_date = request.POST.get('c2')
        quantity = request.POST.get('c3')
        unitprice = request.POST.get('c4')
        Total = request.POST.get('c5')
        now = datetime.datetime.now()
        today = now.strftime("%Y-%m-%d")
        m = now.month
        y = now.year
        uid = request.POST.get('c6', '')
        items = request.POST.get('c7', '')
        pname = request.POST.get('pname')

        order_details.objects.create(order_date=order_date, quantity=quantity, unitprice=unitprice, Total=Total, uid=uid, items=items, Amonth=m, Ayear=y)

        payment = order_details.objects.latest('id')
    return render(request, 'Payment.html', {'pay_amount': payment, 'dd':today})

def amonth(request):
    total = 0
    if request.method == "POST":
        m = request.POST.get('m')
        user_dict = order_details.objects.filter(Amonth=m).values()
        for u in user_dict:
            total = total+int(u['Total'])
        return render(request, 'monthreport.html', {'user_dict':user_dict,'Total': total})

def ayear(request):
    total = 0
    if request.method == "POST":
        m = request.POST.get('y')
        user_dict = order_details.objects.filter(Ayear=m).values()
        for u in user_dict:
            total = total + int(u['Total'])
        return render(request, 'monthreport.html', {'user_dict': user_dict, 'Total': total})


def bmonth(request):
    return render(request, 'bmonth.html')

def byear(request):
    return render(request, 'byear.html')

def cart(request):
    emailid = request.session['uid']
    user_dict = {'msg': 'one record inserted successfully'}
    if request.method == "POST":

        productname = request.POST.get('pname')
        now = datetime.datetime.now()
        mdate = now.strftime("%Y-%m-%d")
        unitprice = request.POST.get('unitprice')

        cart_details.objects.create(userid=emailid, productname=productname, date=mdate, order_status='pending', unitprice=unitprice, Total=unitprice)
        user_dict=Product.objects.all()
        return render(request, 'product_view_customer.html', {'user_dict':user_dict})


def mycart(request):
    emailid = request.session['uid']
    user_dict=cart_details.objects.filter(userid=emailid).values()
    total_paid = list(cart_details.objects.filter(userid=emailid).aggregate(Sum('unitprice')).values())[0]
    total = total_paid
    return render(request, 'Cart.html', {'pp': total, 'user_dict': user_dict, 'userid': emailid})

def cartpayment(request):
    if request.method == "POST":
        total = request.POST.get('tt')
        print(total)
        now = datetime.datetime.now()
        today = now.strftime("%Y-%m-%d")
        amt = int(total)
        return render(request, 'cpay2.html', {'total':amt, 'msg':'order has been placed successfully'})
        #return render(request, 'cartpayment.html', {'dd': today, 'tt': total})

def cpay(request):
    if request.method == "POST":
        #total =request.POST.get('tt')
        #amt =int(total)
        return render(request,'cpay2.html',{'total':1200})


def cartdelete(request):
    if request.method == 'POST':
        userdatas = cart_details.objects.all()
        id = request.POST.get('id')
        useritems = cart_details.objects.get(id=id)

        useritems.delete()
        useritems = cart_details.objects.all()
    return render(request,'Cart.html',context={'user_dict': useritems})

def billing(request):
    items = ""
    today = ""
    total = ""
    customersid = ""
    user_dict = {'msg': 'one record inserted successfully'}
    if request.method == "POST":
        id = request.POST.get('id')
        orderid = request.POST.get('f2')
        customersid = request.POST.get('f3')
        bill_date = request.POST.get('f4')
        now = datetime.datetime.now()
        today = now.strftime("%Y-%m-%d")
        items = request.POST.get('f5')
        total = request.POST.get('f6')

        order_dict = order_details.objects.filter(id=id).values()
        for s in order_dict:
            customersid = s['uid']
            print(customersid)
            items = s['items']
            print(items)
            total = s['unitprice']
            print('total')

        gst = request.POST.get('f7')
        tax_total = request.POST.get('f8')
        shipping_charge = request.POST.get('f9')
        grandtotal = request.POST.get('f10')

        Billing.objects.create(orderid=orderid, customersid=customersid, items=items, bill_date=bill_date, total=total, gst=gst, tax_total=tax_total, shipping_charge=shipping_charge, grandtotal=grandtotal)
        #return render(request, '')
    return render(request, 'Bill.html', {'oid': id, 'tt': today, 'cc': customersid, 'zz': items, 'yy': total})


def billview(request):
    user_dict = Billing.objects.all()
    return render(request, 'billingview.html', {'user_dict': user_dict})

def bill_delete(request):
    if request.method == 'POST':
        userdatas = Billing.objects.all()
        id = request.POST.get('id')
        useritems = Billing.objects.get(id=id)

        useritems.delete()
        user_items = Billing.objects.all()
    return render(request,'billingview.html',context={'user_dict': user_items})

def payment(request):
    emailid = request.session['uid']
    today = ""
    user_dict = ''
    if request.method == "POST":
        Paymenttype = request.POST.get('f2','')
        if Paymenttype == 'cod':
            content = "Bombay Novelty E-store--hello your order has been placed successfully! Your order will be delivered within two days. thank you "
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('priyankavrokhade@gmail.com', '789@pink@cool')
            mail.sendmail('priyankavrokhade@gmail.com', emailid, content)
            mail.close()
            return render(request, 'customer_home.html', {'msg':'Your order has been placed successfully'})
        else:
            BankName = request.POST.get('f3','')
            Amount = request.POST.get('f5')
            Paymentdate = request.POST.get('f6')
            now = datetime.datetime.now()
            today = now.strftime("%Y-%m-%d")
            print(Amount)
            Payment.objects.create(Paymenttype=Paymenttype, BankName=BankName,  Amount=Amount, Paymentdate=Paymentdate)
            amt = int(Amount)
            return render(request, 'payment2.html',{'amount': amt})
    return render(request, 'Payment.html', {'pid': id, 'dd': today})



def paymentview(request):
    user_dict = Payment.objects.all()
    return render(request, 'payview.html', {'user_dict': user_dict})

def paymentremove(request):
    useritems = ''
    if request.method == 'POST':
        userdatas = Payment.objects.all()
        id = request.POST.get('id')
        useritems = Payment.objects.get(id=id)

        useritems.delete()
        useritems = Payment.objects.all()
    return render(request,'payview.html', context={'user_dict': useritems})


def faq(request):
    user_dict = {'msg': 'sent'}
    prod_cat = ProCategory.objects.all()
    prod_list = Product.objects.all()
    return render(request, 'faqs.html', context={'user_dict': user_dict, 'prod_cat':prod_cat, 'prod_list':prod_list})

def catwise(request):

    return render(request,'catwise_view.html')

def prodwise(request):
    return render(request, 'prodwise_view.html')

def feedback(request):
    user_dict = {'msg': ''}
    if request.method == "POST":
        userid = request.POST.get('e2', '')
        servicefeedback = request.POST.get('e3', '')
        comments = request.POST.get('e4', '')

        FeedBackForm.objects.create(userid=userid, servicefeedback=servicefeedback, comments=comments)
        return render(request, 'index.html', context=user_dict)
    prod_cat = ProCategory.objects.all()
    prod_list = Product.objects.all()
    return render(request, 'Feedback.html', context={'user_dict': user_dict, 'prod_cat':prod_cat, 'prod_list':prod_list})

def fbackview(request):
    user_dict = FeedBackForm.objects.all()
    return render(request, 'feedbackview.html', {'user_dict': user_dict})

def servicecustomer(request):
    user_dict = Service.objects.all()
    prod_cat = ProCategory.objects.all()
    return render(request, 'servicecustomerview.html',{'user_dict':user_dict, 'prod_cat':prod_cat})

def single(request):
    if request.method == "POST":
        id = request.POST.get('id')
        user_dict = Product.objects.filter(id=id).values()
        print(id)
    return render(request, 'single.html', {'user_dict': user_dict})

def about(request):

    return render(request, 'aboutus.html')



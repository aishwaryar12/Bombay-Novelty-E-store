from django.conf.urls import url
from . import views

urlpatterns=[

    url('^$', views.index, name='index'),
    url('^admins/$', views.admins, name='admins'),
    url('^customers/$', views.customers, name='customers'),
    
    #url('^sample/$',views.sample, name='sample'),
    url('^signup/$', views.signup, name='signup'),
    url('^sampleview/$', views.sampleview, name='sampleview'),
    url('^remove_items/$', views.remove_items, name='remove_items'),
    url('^update_items/$', views.update_items, name='update_items'),
    url('^reg_db/$', views.reg_db, name='reg_db'),
    
    url('^changepassword/$',views.changepassword, name='changepassword'),
    url('^forgotpass/$',views.forgotpass, name='forgotpass'),
    
    url('^signin/$', views.signin, name='signin'),
    
    url('^Category/$',views.Category, name='Category'),
    url('^categoryview/$',views.categoryview, name='categoryview'),
    url('^catremove_items/$',views.catremove_items, name='catremove_items'),
    url('^catupdate_items/$',views.catupdate_items, name='catupdate_items'),
    url('^cat_db/$',views.cat_db, name='cat_db'),
    
    url('^purchase/$',views.purchase, name='purchase'),
    url('^purchaseview/$',views.purchaseview, name='purchaseview'),
    url('^purremove_items/$',views.purremove_items, name='purremove_items'),
    url('^purupdate_items/$',views.purupdate_items, name='purupdate_items'),
    url('^pur_db/$', views.pur_db, name='pur_db'),
    
    url('^supplier/$',views.supplier, name='supplier'),
    url('^supplierview/$',views.supplierview, name='supplierview'),
    url('^supremove_items/$',views.supremove_items, name='supremove_items'),
    url('^supupdate_items/$',views.supupdate_items, name='supupdate_items'),
    url('^sup_db/$',views.sup_db, name='sup_db'),
    
    url('^stock/$',views.stock, name='stock'),
    url('^stockview/$',views.stockview, name='stockview'),
    url('^stkremove_items/$',views.stkremove_items, name='stkremove_items'),
    url('^stkupdate_items/$',views.stkupdate_items, name='stkupdate_items'),
    url('^stk_db/$',views.stk_db, name='stk_db'),
    
    url('^exchange/$',views.exchange, name='exchange'),
    url('^exchangeview/$',views.exchangeview, name='exchangeview'),
    url('^exchgremove_items/$',views.exchgremove_items, name='exchgremove_items'),
    url('^exchgupdate_items/$',views.exchgupdate_items, name='exchgupdate_items'),
    url('^ex_db/$',views.ex_db, name='ex_db'),
    
    url('^product/$',views.product, name='product'),
    url('^productview/$',views.productview, name='productview'),
    url('^proremove_items/$',views.proremove_items, name='proremove_items'),
    url('^proupdate_items/$',views.proupdate_items, name='proupdate_items'),
    url('^pro_db/$',views.pro_db, name='pro_db'),
    
    url('^service/$', views.service, name='service'),
    url('^serviceview/$', views.serviceview, name='serviceview'),
    url('^serremove_items/$', views.serremove_items, name='serremove_items'),
    url('^serupdate_items/$', views.serupdate_items, name='serupdate_items'),
    url('^ser_db/$', views.ser_db, name='ser_db'),
    
    url('^servicecustomer/$', views.servicecustomer, name='servicecustomer'),
    
    url('^mbscheme/$', views.mbscheme, name='mbscheme'),
    url('^mbschemeview/$', views.mbschemeview, name='mbschemeview'),
    url('^mbsremove_items/$', views.mbsremove_items, name='mbsremove_items'),
    url('^mbsupdate_items/$', views.mbsupdate_items, name='mbsupdate_items'),
    url('^mbs_db/$', views.mbs_db, name='mbs_db'),
    
    url('^procustomerview/$',views.procustomerview, name='procustomerview'),
    
    url('^procustomerview_cat/(?P<pk>\d+)/$',views.procustomerview_cat, name='procustomerview_cat'),
    
    url('^porder/$', views.porder, name='porder'),
    url('^Orderview/$', views.Orderview, name='Orderview'),
    url('^odelete/$', views.odelete, name='odelete'),
    
    url('^amonth/$', views.amonth, name='amonth'),
    url('^ayear/$', views.ayear, name='ayear'),
    url('^bmonth/$', views.bmonth, name='bmonth'),
    url('^byear/$', views.byear, name='byear'),
    
    
    url('^billing/$', views.billing, name='billing'),
    url('^billview/$', views.billview, name='billview'),
    url('^bill_delete/$', views.bill_delete, name='bill_delete'),
    
    url('^payment/$', views.payment, name='payment'),
    url('^paymentview/$', views.paymentview, name='paymentview'),
    url('^paymentremove/$', views.paymentremove, name='paymentremove'),
    
    url('^cart/$', views.cart, name='cart'),
    url('^mycart/$', views.mycart, name='mycart'),
    url('^cartdelete/$', views.cartdelete, name='cartdelete'),
    
    url('^faq/$', views.faq, name='faq'),
    url('^feedback/$', views.feedback, name='feedback'),
    url('^fbackview/$', views.fbackview, name='fbackview'),
    
    
    url('^catwise/$', views.catwise, name='catwise'),
    url('^prodwise/$', views.prodwise, name='prodwise'),
    url('^order_next/$', views.order_next, name='order_next'),
    
    url('^customers_next/$', views.customers_next, name='customers_next'),
    url('^cartpayment/$', views.cartpayment, name='cartpayment'),
    url('^cpay/$', views.cpay, name='cpay'),
    
    url('^single/$', views.single, name='single'),
    
    url('^about/$', views.about, name='about'),
]
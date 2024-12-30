"""
URL configuration for petstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from petapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("pet/",views.addpet,name='pet/'),
    path("petlist/",views.getallpet,name='petlist/'),
    path("petupdate/",views.update ,name='update'),
    path("customer/",views.Addcustomer ,name='customer/'),
    path("customerlist/",views.getallcustomer,name='customerlist/'),
    path("update/",views.updatecustomer,name='update/'),

    path("petlist/edit/<int:pid>",views.getpet,name='petlist/'),    #edit pet url
    path("edit/<str:emailId>",views.getcustomer),    #edit customer url


    path("petlist/delete/<int:pid>",views.deletepet),   #delete pet url
    path("delete/<str:emailId>",views.deletecustomer),

    path("petlist/addcart/<int:pid>",views.addcart,name='addcart'),
    path("cartlist/",views.showcart ,name='cartlist/'),


    path("cartlist/placeorder",views.showorderform,name="cartlist/placeorder"),

    path('pay/',views.payment,name='pay/'),
    path('paymentsuccess/<int:order_id>/<str:payment_id>',views.paysucc,name='payementsuccess/'),



    path("login/",views.login,name="login/"),
    path("logout/",views.logout,name="logout/"),


    path("index/",views.index,name="index/"),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.shortcuts import render,HttpResponse
from.models import pet,customer,cart,orders,adminmodel
from datetime import date
from django.contrib.auth.hashers import make_password,check_password
import razorpay
from django.conf import settings
# Create your views here.



def index(request):
    return render(request,'petapp/index.html')


def addpet(request):
    if request.method=="POST":
        gender=request.POST['choice']
        name=request.POST['name']
        species=request.POST['species']
        age=request.POST['age']
        description=request.POST['description']
        price=request.POST['price']
        is_activate=request.POST['is_activate']
        pet_image=request.FILES['Images']

        data=pet.objects.create(gender=gender,name=name,species=species,age=age,description=description,price=price,is_activate=is_activate,pet_image=pet_image)
        data.save()
        return HttpResponse("Added successfully")
    else:
        return render(request,'petapp/addpet.html')
    

def getallpet(request):
    data=pet.objects.all()
    return render(request,'petapp/petlist.html',{"pet":data})

def update(request):
    if request.method=='POST':
        pid=request.POST['petid']
        gender=request.POST['choice']
        name=request.POST['name']
        species=request.POST['species']
        age=request.POST['age']
        description=request.POST['description']
        price=request.POST['price']
        is_activate=request.POST['is_activate']
        existingData=pet.objects.filter(pid=pid)
        existingData.update(gender=gender,name=name,species=species,age=age,description=description,price=price,is_activate=is_activate)

        return HttpResponse("Updated Successfully")
    else:
        return render(request,'petapp/updatepet.html')
    
def Addcustomer(request):
    if request.method=='POST':
        emailId=request.POST['emailId']
        custname=request.POST['custname']
        password=request.POST['password']
        passw = make_password(password)
        address=request.POST['address']
        contact_No=request.POST['contact_No']

        data=customer.objects.create(emailId=emailId,custname=custname,password=passw,address=address,contact_No=contact_No)
        data.save()

        return HttpResponse("Customer added  Successfully")
    else:
        return render(request,'petapp/addcustomer.html')
    

def getallcustomer(request):
    data=customer.objects.all()
    return render(request,'petapp/customerlist.html',{"customer":data})

def updatecustomer(request):
    if request.method=='POST':
        emailId=request.POST['emailId']
        custname=request.POST['custname']
        password=request.POST['password']
        address=request.POST['address']
        contact_No=request.POST['contact_No']
        existingData=customer.objects.filter(emailId=emailId)
        existingData.update(emailId=emailId,custname=custname,password=password,address=address,contact_No=contact_No)

        return HttpResponse("Updated Successfully")
    else:
        return render(request,'petapp/updatecustomer.html')
    



#below function if to editi the pet 
def getpet(request,pid):
    data=pet.objects.get(pid=pid)
    return render(request,'petapp/updatepet.html',{"pet":data})    


def getcustomer(request,emailId):
    data=customer.objects.get(emailId=emailId)
    return render(request,'petapp/updatecustomer.html',{"customer":data})   




def deletepet(request,pid):
    petobj=pet.objects.get(pid=pid)
    petobj.delete()
    return HttpResponse("deleted successfully")


def deletecustomer(request,emailId):
    custobj=customer.objects.get(emailId=emailId)
    custobj.delete()
    return HttpResponse("deleted successfully") 


def addcart(request,pid):
    pet_obj=pet.objects.get(pid=pid)
    emailId='jack@gmail.com'
    cust_obj=customer.objects.get(emailId=emailId)
    quantity=1
    totalprice=pet_obj.price*quantity
    data=cart.objects.create(pet_obj=pet_obj,cust_obj=cust_obj,quantity=quantity,totalprice=totalprice)
    data.save()
    return HttpResponse("Add to cart successfully")

def showcart(request):
    cust_obj='jack@gmail.com'
    data=customer.objects.get(emailId=cust_obj)
    data=cart.objects.filter(cust_obj=data)
    return render(request,'petapp/cartlist.html',{'cart':data})


def showorderform(request):
    if request.method=='POST':
        emailId="jack@gmail.com"
        data=customer.objects.get(emailId=emailId)
        data=cart.objects.filter(cust_obj=data)
        totalbill=0
        for i in data:
            totalbill=totalbill+i.totalprice
            name=request.POST['name']
            address=request.POST['address']
            city=request.POST['city']
            state=request.POST['state']
            pincode=request.POST['pincode']
            phoneno=request.POST['phoneno']
            # totalbillamount=request.POST['totalbillamount']


        data=orders.objects.create(emailId=emailId,name=name,address=address,city=city,state=state,pincode=pincode,phoneno=phoneno,totalbillamount=totalbill)
        data.save()
        today=date.today()
        today=str(today).replace('-','')
        datadata=str(data.id)+today
        data.ordernumber=datadata
        data.save()
        data=orders.objects.get(emailId=emailId,ordernumber=datadata)
        razorpay_client = razorpay.Client(
            auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    
    

        currency = 'INR'
        amount = 20000  # Rs. 200
    
        # Create a Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                        currency=currency,
                                                        payment_capture='0'))
    
        # order id of newly created order.
        razorpay_order_id = razorpay_order['id']
    
        # we need to pass these details to frontend.
        context = {}
        context['razorpay_order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = settings.RAZORPAY_KEY_ID
        context['razorpay_amount'] = amount
        context['currency'] = currency





        return render(request,'petapp/Payment.html',{'orderobj':data,'totalbill':totalbill,'context':context})






        return HttpResponse("<h1>Success</h1>")
    else:
        return render(request,'petapp/order.html')
    


def login(request):
    if request.method=='POST':
        emailId=request.POST['email']
        type=request.POST['type']
        password=request.POST['Password']
        if type=='user':
            cust=customer.objects.get(emailId=emailId)
            if cust:
                flag=check_password(password,cust.password)
                if flag:
                    request.session['username'] = emailId
                    return HttpResponse(request,"petapp/index.html")
                else:
                    return HttpResponse('<h1>Wrong</h1>')
        if type=='admin':
            admin=adminmodel.objects.get(adminemailid=emailId)
            if admin:
                if password==admin.adminpassword:
                    request.session["adminemailid"]= emailId

                    return HttpResponse(request,'petapp/index.html')
                else:
                    return HttpResponse('<h1>Wrong</h1>')
            else:
                return HttpResponse("<h1>admin does not exit</h1>")
    else:
        return render(request,'petapp/Login.html')
    


def logout(request):
    session_key=list(request.session.keys())
    for key in session_key:
        del request.session[key]
    return render(request,"petapp/index.html")
    



def payment(request):
    return render(request,'petapp/Payment.html')

def paysucc(request,oid,pid):
    return render(request,'petapp/PaymentSuccss.html')
       
    


 


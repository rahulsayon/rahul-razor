from django.shortcuts import render
from django.http import HttpResponse
import razorpay 
from . models import Cofee
from  django.views.decorators.csrf import csrf_exempt 
from django.core.mail import send_mail 
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = int(request.POST.get("amount")) * 100
        print(name,amount)
        client = razorpay.Client(auth=("rzp_test_mkzYuJKOPzhV1n", "KeeafZoOkWIsQHcR2nRVa9Bn"))
        payment = client.order.create({ 'amount':amount , 'currency':'INR', 'payment_capture':'1' })
        print(payment)
        coffee = Cofee(name=name, amount=amount, payment_id=payment['id'])
        coffee.save()
        return render(request,"index.html",{"payment" : payment})
    return render(request,"index.html")

@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        for key,val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
        user = Cofee.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()
        msg_plain = render_to_string('email.txt')
        msg_html = render_to_string('email.txt')

        res = send_mail( 'Order from Gmail',msg_plain, settings.EMAIL_HOST_USER,
                            recipient_list = ['rahulsayon98@gmail.com'],
                            html_message=msg_html
                            )    
        print(a)
    return render(request,"success.html")

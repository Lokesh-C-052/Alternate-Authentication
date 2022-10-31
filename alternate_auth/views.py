from django.shortcuts import render,redirect


from .models import details
import hashlib
# Create your views here.

def index(request):
    return render(request,'alternate_auth/index.html')

def signup_ref(request):
    return render(request,'alternate_auth/image_selector.html')


def login(request):

    if request.method=="POST":
        username=request.POST.get("username");
        return redirect('/login/'+username)
    else:
        return render(request,'alternate_auth/login.html',{'flag':0})


def login_ref(request,username):
    flag = 0
    try:
        detail = details.objects.get(username=username)
    except:
        flag=1

    if flag==1:
        return render(request,'alternate_auth/login.html',{'flag':1})
    if request.method=="POST":
        password=request.POST.get("password").encode("utf-8")
        hashed_password=hashlib.sha256(str(password).encode('utf-8')).hexdigest()
        if detail.password==hashed_password:
            return redirect('https://feba.bobibanking.com/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=012')
        else:
            return render(request, 'alternate_auth/login_page.html',{'username': detail.username, 'image_type': detail.password_type,'flag':1})

    else:
        return render(request, 'alternate_auth/login_page.html',{'username':detail.username,'image_type':detail.password_type})



def signup(request ,id):

    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        age=request.POST.get("age")
        account_number=request.POST.get("account_number")
        phone_number=request.POST.get("ph_number")
        password_type=request.POST.get("password-type")
        password=request.POST.get("password").encode("utf-8")
        hashed_password=hashlib.sha256(str(password).encode('utf-8')).hexdigest()



        user=details(username=username,email=email,age=age,Account_number=account_number,phone_number=phone_number,password=hashed_password,password_type=password_type);
        user.save()


        return render(request,'alternate_auth/index.html')
    else:
        return render(request, 'alternate_auth/signup.html' ,{'id':id})




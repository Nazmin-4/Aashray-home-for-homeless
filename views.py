from django.shortcuts import render,redirect
from .models import URegister,Zip,Upload
from hohmp import settings
from django.contrib import messages
# Create your views here.
context={'true':0,'name':"",'email':"",'count':0,'msg':"",'zpdata':[],'zip':0,'ngo':"",'dashdata':[],'dashcount':0,'mob':""}
def home(request):
    return render(request,'home.html',context)
def register(request):
    if request.method == "POST":
        username=request.POST["name"]
        useremail=request.POST["email"]
        userpassword=request.POST["password"]
        userrpassword=request.POST["rpassword"]
        print(userpassword,useremail,username)
        if userpassword == userrpassword:
            name=username
            email=useremail
            # password=userpassword
            passwordHash = userpassword
            ureg=URegister(name=name,email=email,passwordHash=passwordHash)
            ureg.save()
            return render(request,'home.html')
        else:
            context["message"]="Passwords do not match.Please register again."
            
            return render(request,'register.html',context)

    else:
        return render(request,'register.html')
def login(request):
    print("hi",request)
    try:
        if request.method == "POST":
            useremail = request.POST['email'] 
            password = request.POST['password']
            print("hie")
            mydata = URegister.objects.filter(email=useremail,passwordHash=password).values()
            if mydata is not None:
                print(mydata)
                mydata=list(mydata)
                context['name']=mydata[0]['name']
                context['email']=mydata[0]['email']
                context['true']=1
                print("true",context['true'])
                return render(request,'home.html',context)
    except:
                error={}
                error['msgg']="bad credentials"
                print("hello")
                return render(request,'login.html',error)
    
    return render(request,'login.html')
def logout(request):
    context={'true':0,'name':"",'email':"",'count':0,'msg':"",'zpdata':[],'zip':0,'ngo':"",'dashdata':[],'dashcount':0,'mob':""}
    print('context logout',context)
    return render(request,'home.html',context)
def dash(request):
    details=Upload.objects.filter(uemail=context['email'])
    print(details)
    details=list(details)
    context['dashdata']=details
    context['dashcount']=len(details)
    return render(request,'dash.html',context)
def help(request):
    try:
        if context['true']:
            zip=request.GET['zip']
            zipdata=Zip.objects.filter(zipcode=zip)
            zipdata_count=Zip.objects.filter(zipcode=zip).count()
            zipdata=list(zipdata)
            context['zpdata']=zipdata
            context['count']=zipdata_count
            context['zip']=zip

            print(zipdata)
            return render(request,'help.html',context)
    # except:
        else:
            context['msg']="you need to login first"
            return render(request,'login.html',context)
    except:
        print("errors")
    return render(request,'help.html',context)
def upload(request,ngoname=None,ngoemail=None):
        if request.method == "POST":
            uname=context['name']
            uemail=context['email']
            ngoemail=context['ngoemail']
            ngoname=context['ngoname']
            umessage=request.POST["message"]
            uaddress=request.POST["address"]
            umobile=request.POST["mobile"]
            context['mob']=umobile
            usave=Upload(ngoname=ngoname,ngoemail=ngoemail,uname=uname,uemail=uemail,umobile=umobile,uaddress=uaddress,umessage=umessage,ustatus="Pending")
            print(usave)
            print(ngoemail)
            usave.save()
            context['msg']="uploaded successfully"
            return render(request,"dash.html",context)
        else:
            context['ngoemail']=ngoemail
            context['ngoname']=ngoname
            print("elseee")
            return render(request,"upload.html",context)
    # except:
    #     print("errorss")
    # print("out")
    # return render(request,"upload.html",context)
def ngologin(request):
    try:
        if request.method == "POST":
            useremail = request.POST['email'] 
            password = request.POST['password']
            print("hie")
            mydata = Zip.objects.filter(email=useremail,password=password).values()
            if mydata is not None:
                print(mydata)
                mydata=list(mydata)
                context['name']=mydata[0]['ngoname']
                context['email']=mydata[0]['email']
                context['mob']=mydata[0]['contactNumber']
                context['ngotrue']=1
                print("true",context['true'])
                print('ngologin',context)
                return render(request,'home.html',context)
    except:
                error={}
                error['msgg']="bad credentials"
                print("hello")
                return render(request,'ngologin.html',context)
    
    return render(request,'ngologin.html',context)
def ngoregister(request):
    if request.method == "POST":
        username=request.POST["ngoname"]
        useremail=request.POST["email"]
        userpassword=request.POST["password"]
        userrpassword=request.POST["rpassword"]
        print(userpassword,useremail,username)
        if userpassword == userrpassword:
            name=username
            email=useremail
            zip=request.POST['zipcode']
            contactnumber=request.POST['phn']
            address=request.POST['address']
            # password=userpassword
            password = userpassword
            ureg=Zip(ngoname=name,zipcode=zip,email=email,contactNumber=contactnumber,password=password,address=address)
            ureg.save()
            return render(request,'home.html')
        else:
            context["message"]="Passwords do not match.Please register again."
            
            return render(request,'ngoregister.html',context)

    else:
        # return render(request,'register.html')
        return render(request,'ngoregister.html',context)
def ngodash(request):
    print('cngodash',context)
    details=Upload.objects.filter(ngoemail=context['email'])
    print(details)
    details=list(details)
    context['ngodashdata']=details
    context['ngodashcount']=len(details)
    context['status']='Pending'
    return render(request,'ngodash.html',context)
def success(request,id):
    if request.method == "POST":
        sucdata=Upload.objects.get(id=id)
        print('succ')
        sucdata.ustatus='Success'
        sucdata.save()
        return redirect(ngodash)

from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from bankapp.models import District, Branch, Customer


# Create your views here.


def home(request):
    branches = District.objects.all()

    return render(request, 'home.html', {'branches': branches})


def login(request):
    if request.user.is_authenticated:
        return redirect('bankapp:main')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('bankapp:profile')
            else:
                messages.info(request, "Invalid Username or Password")
                return redirect('bankapp:login')
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpass = request.POST['cpass']
        if password == cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return redirect('bankapp:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('bankapp:login')
        else:
            messages.info(request, "Passwords not match")
            return redirect('bankapp:register')
    return render(request, 'register.html')


def form(request):
    try:
        user = User.objects.get(id=request.user.id)
        us=Customer.objects.filter(user=user)
        if us:
            messages.info(request,"Form already submitted")
            return redirect('bankapp:profile')
    except:
        pass

    if request.method == 'POST':
        user=User.objects.get(id=request.user.id)
        print(user)
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        district = District.objects.get(id=request.POST['district'])
        branch = Branch.objects.get(id=request.POST['branch'])
        actype = request.POST['actype']
        material = request.POST.getlist('material')
        print(name)
        print(material)
        customer = Customer.objects.create(user=user,name=name, dob=dob, age=age, gender=gender, phone=phone, email=email,
                                           address=address, district=district, branch=branch, actype=actype,
                                           material=material)
        customer.save()
        messages.info(request,"Form submitted successfully")
        return redirect('bankapp:profile')
    return render(request, 'main.html')


class AjaxHandlerView(View):
    def get(self, request):
        dist_id = request.GET.get('district')
        branch = []
        if dist_id:
            print(dist_id)
            district = District.objects.get(id=dist_id)
            branch = Branch.objects.filter(district=district)
        return render(request, 'branch_select.html', {'branch': branch})


def profile(request):
    return render(request,'profile.html')
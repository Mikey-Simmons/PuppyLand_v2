from django.shortcuts import render, HttpResponse, redirect
from .models import Dog, User, Customer
from django.contrib import messages
import bcrypt
from .forms import ImageForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def aboutus(request):
    return render(request,'aboutus.html')
def puppies(request):
    context = {
        'all_dogs': Dog.objects.all()
    }
    return render(request,'puppies.html',context)
def admin(request):
    return render(request,'admin.html')
def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/adminpage')
    else:
        password=request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
        new_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = pw_hash
    )
    messages.success(request,"User Successfully created!")
    request.session['user_id'] = new_user.id
    return redirect('/')
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/') 
    list_of_users = User.objects.filter(email=request.POST['email'])
    if len(list_of_users) > 0:
        user = list_of_users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            return redirect('/adminpage')
def adminpage(request):
    if 'user_id' not in request.session:
        return redirect('/')
    logged_in_user = User.objects.get(id=request.session['user_id'])
    context = {
        'logged_in_user': logged_in_user,
        'all_dogs': Dog.objects.all()
    }
    return render(request,'adminpage.html',context)
def adddog(request):
    if 'user_id' not in request.session:
        return redirect('/')
    logged_in_user = User.objects.get(id=request.session['user_id'])
    form= ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        newform = Dog(img = request.FILES['img'])
        newform.save()
    context = {
        'form': form,
        'logged_in_user': logged_in_user,
    }
    return render(request,'dogform.html',context)
def addpup(request):
    logged_in_user = User.objects.get(id=request.session['user_id'])
    form= ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        new_dog = Dog.objects.create(
            dog_name = request.POST['dog_name'],
            dog_breed = request.POST['dog_breed'],
            dog_gender = request.POST['dog_gender'],
            dog_weight= request.POST['dog_weight'],
            dog_age= request.POST['dog_age'],
            img= request.FILES['img']
            )
    context = {
        'logged_in_user': logged_in_user,
        'form': form,
    }
    return redirect('/adminpage',context)
def contactpage(request):
    return render(request,'contactus.html')
def gallery(request):
    return render(request,'gallery.html')
def adoptpage(request):
    return render(request,'adoptform.html')
def submit_app(request):
    new_app= Customer.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        phone=request.POST['phone'],
        dogs_owned=request.POST['dogs_owned'],
        description=request.POST['description'],
        reason_why=request.POST['reason_why'],
        occupataion=request.POST['occupataion']
    )
    return redirect('/success')
def success(request):
    return render(request,'success.html')
from django.shortcuts import render,redirect,get_object_or_404
from blog.forms import PhotoForm,ContactForm,CategoryForm
from blog.models import Photo,Category,Contact
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
# home page func
def home(request):
    cat = Category.objects.all()
    photo = Photo.objects.all().order_by('-pub_date')
    context = {'photo':photo,'cat':cat}
    return render(request,'blog/home.html',context)


# for displayingspecific catergory phots . catergory= nature thne show only nature photo
def cat_detail(request,category_name):
    cat = get_object_or_404(Category,category_name=category_name)
    photo = Photo.objects.filter(category= cat).order_by('-pub_date')
    return render(request,'blog/cat_detail.html',{'photo':photo,'cat':cat})




# for contact form
def contact(request):
    register = False
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # for sending mail to client
            full_name = request.POST['Full_Name']
            email = request.POST['Email']
            contact_No = request.POST['Contact_No']
            purpose = request.POST['purpose']
            requirements = request.POST['requirements']

            message = ('Full Name : {} \nEmail : {} \nContact : {} \npurpose : {} \nRequirments : {}').format(full_name,email,contact_No,purpose,requirements)


            send_mail(subject = email,
            message= message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['mominarham2345@gmail.com'],
            fail_silently=True)






            messages.success(request,'ThankYou! We will Contact you Shortly ')
            return redirect('contact')
        else:
            messages.error(request,'Please fill all the detail correctly')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request,'blog/contact.html',{'form':form,'register':register})



# for about page
def about(request):
    return render(request,'blog/about.html')



# for showing all categries in gallery page 
def gallery(request):
    cat = Category.objects.all()
    return render(request,'blog/gallery.html',{"cat":cat})




# for client
# for login and create pos from front end
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        
        if user:
            auth.login(request,user)
            return redirect('create_post')
        else:
            messages.error(request,'Invalid Login')
            return redirect('login')
    else:
        return render(request,'blog/auffy.html')


# after login and creting post
@login_required
def create_post(request):
    form = PhotoForm()
    registered = False
    if request.method == "POST":
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            registered = True
            return redirect('create_post')
        else:
            messages.error(request,'Please fill the correct detail')
            return redirect('create_post')
    else:
        form = PhotoForm()
        
    return render(request,'blog/create_post.html',{'form':form, 'registered': registered})


# loggin out the person who is uplaoding content
@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')




# adding update button
@login_required
def update(request,id):
    photo = get_object_or_404(Photo,id = id)
    form = PhotoForm(instance=photo)
    if request.method =="POST":
        form = PhotoForm(request.POST,request.FILES,instance=photo)
        if form.is_valid():
            form.save()
            return redirect('gallery')
        else:
            messages.error(request,'Please enter the detail correctly')
            return redirect ('update')
    return render(request,'blog/update.html',{'form':form})


# for deleting pphoto
@login_required
def delete(request,id):
    photo = Photo.objects.get(id=id)
    if request.method =="POST":
        photo.delete()
        return redirect('gallery')
    return render(request,'blog/delete.html',{'photo':photo})



# adding category
@login_required
def add_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create_post')
        else:
            messages.error(request,'Please fill the correct detail')
            return redirect('add_category')
    else:
        form = CategoryForm()
        
    return render(request,'blog/add_category.html',{'form':form})


# fro showing category
@login_required
def show_cat(request):
    cat = Category.objects.all()
    return render(request,'blog/show_cat.html',{'cat':cat})


# for updating category
@login_required
def update_cat(request,id):
    cat = get_object_or_404(Category,id = id)
    form = CategoryForm(instance=cat)
    if request.method == 'POST':
        form = CategoryForm(request.POST,request.FILES,instance=cat)
        if form.is_valid():
            form.save()
            return redirect('create_post')
        else:
            messages.error(request,'Enter Detail Correctly')
            return HttpResponse('nahi hua')
    return render(request,'blog/update_cat.html',{'form':form})
        

# for deleting category
@login_required
def delete_cat(request,id):
    cat = Category.objects.get(id=id)
    if request.method =="POST":
        cat.delete()
        return redirect('show_cat')
    return render(request,'blog/delete_cat.html',{'cat':cat})



# def basic(request):
#     form = PhotoForm()
#     if request.method == "POST":
#         form = PhotoForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             return HttpResponse('kakdma')
#     else:
#         form = PhotoForm()

#     return render(request,'blog/basic.html',{'form':form})


    

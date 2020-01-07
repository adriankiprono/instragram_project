from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm



# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()
    
    return render(request,'home.html',{"images":images})

@login_required(login_url='/accounts/login/')
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/image.html", {"image":image})

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

def reg_view(request):
    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form=UserCreationForm()
    return render(request, 'registration/register.html',{"form":form})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.editor = current_user
            image.save()
        return redirect('home')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.all()
    profile_pic = Profile.objects.all()
    
    return render(request,'profile.html',{"profile_pic":profile_pic,'profile':profile})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == 'POST':
        user_form = UpdateUser(request.POST,instance=request.user)
        profile_form = UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your Profile account has been updated successfully')
        return redirect('my_profile')
    else:
        user_form = UpdateUser(instance=request.user)
        profile_form = UpdateProfile(instance=request.user.profile)
        forms = {
        'user_form':user_form,
        'profile_form':profile_form
        }
    return render(request,'update_profile.html',forms)



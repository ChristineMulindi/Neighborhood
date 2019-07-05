from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Neighborhood,Profile,Post,Business
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm,NeighborhoodForm,BusinessForm


# Create your views here.

@login_required(login_url='/accounts/login')
def home(request):
    hoods = Neighborhood.objects.all()
    print(hoods)
    return render(request, 'index.html',{'hoods':hoods})


@login_required(login_url='/accounts/login')
def profile(request, id):
    user = User.objects.get(id=id)
    current_user = request.user
    images = Neighborhood.objects.filter(id = id)
    try:
        profile = Profile.objects.get(user_id=id)
    except ObjectDoesNotExist:
        return redirect(update_profile, current_user.id)   
    else:
    
        return render(request, 'profile.html',{"user":user, "images":images, "profile":profile})


@login_required(login_url='/accounts/login/')
def update_profile(request,id): 
    current_user = request.user
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id =id
            profile.save()
        return redirect(home)

    else:
        form = ProfileForm()
    return render(request, 'update_profile.html', {"user": user, "form": form})  


@login_required(login_url='/accounts/login')
def neighborhood(request, id):
    user = User.objects.get(id=id)
    current_user = request.user
    name = Neighborhood.objects.filter(id = id)
    try:
        neighborhood = Neighborhood.objects.get(neighborhood_id=id)
    except ObjectDoesNotExist:
        return redirect(index_html, current_user.id)   
    
    return render(request, 'index.html', {"user":user, "name":name, "neighborhood":neighborhood})




@login_required(login_url='/accounts/login')
def join(request, id):
    current_user = request.user
    form = NeighborhoodForm() 
    
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighborhood = form.save(commit=False)
            print(neighborhood)
            neighborhood.user_id =id
            neighborhood.save()

        return redirect(home)

    else:
        form = NeighborhoodForm()                    
        
    return render(request, 'neighborhood.html', {"user": current_user, "form": form})  


@login_required(login_url='/accounts/login')
def business(request, id):
    businesses = Business.objects.all()
    print(businesses)
    return render(request, 'business.html',{'businesses':businesses})


@login_required(login_url='/accounts/login')
def add_business(request, id):
    current_neighborhood = Neighborhood.objects.get(id = id)
    current_user = request.user
    form = BusinessForm()   
    
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            print(business)
            business.business_user = current_user
            business.business_neighborhood = current_neighborhood
          
            business.save()

        return redirect(home)

    else:
        form = BusinessForm()                    
        
    return render(request, 'add_business.html', {"user": current_user, "form": form})  



    






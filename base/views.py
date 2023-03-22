from django.shortcuts import render, redirect
from .models import Picture
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    images = Picture.objects.all()
    context = {'images': images}
    return render(request, 'home.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            return render(request, 'login.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('home')


def add_photos(request):
    if request.method == "POST":
        if request.user.is_superuser:
            images = request.FILES.getlist('images')
            for img in images:
                print("image saved")
                Picture.objects.create(image=img)
        return redirect('home')
    return render(request, 'add-photos.html', {})


def manage_photo(request, pk):
    img = Picture.objects.get(id=pk)
    if request.method == 'POST':
        if request.user.is_superuser:
            img.image.delete()
            img.delete()
        return redirect('home')
    return render(request, 'manage-photo.html', {'image': img})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, BlogCatagory, BlogSeries
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import NewUserForm, EditProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def single_slug(request, single_slug):
    catagiries = [i.catagory_slug for i in BlogCatagory.objects.all()]
    if single_slug in catagiries:
        matching_series = BlogSeries.objects.filter(blog_catagory__catagory_slug = single_slug)

        series_urls = {}

        for k in matching_series.all():
            part_one = Blog.objects.filter(blog_series__blog_series = k.blog_series).earliest('published')
            series_urls[k] = part_one.slug


        return render(
            request=request,
            template_name='main/catagory.html',
            context={'part_ones': series_urls}
        )

    blogs = [x.slug for x in Blog.objects.all()]
    if single_slug in blogs:
        this_blog = Blog.objects.get(slug = single_slug)
        blogs_from_series = Blog.objects.filter(blog_series__blog_series = this_blog.blog_series).order_by('published')
        this_blog_index = list(blogs_from_series).index(this_blog)
        return render(
            request=request,
            template_name='main/blog.html',
            context={'blog': this_blog, 'sidebar': blogs_from_series, 'this_blog_index': this_blog_index}
        )
    


    return HttpResponse(f'{single_slug} does not exist')


def homepage(request):
    return render(
        request=request,
        template_name='main/catagories.html',
        context={'catagories': BlogCatagory.objects.all}

    )

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'New account has been created: {username}')
            login(request, user)
            messages.info(request, f'You are now logged in as: {username}')
            return redirect('main:homepage')

        else:
            for i in form.error_messages:
                messages.error(request, f'{i}: {form.error_messages[i]}')

    form = NewUserForm
    return render(
        request=request,
        template_name='main/register.html',
        context={'form': form}
    )

def logout_request(request):
    logout(request)
    messages.info(request, f'Logged out successfully!')
    return redirect('main:homepage')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as: {username}')
                return redirect('main:homepage')
            else:
                messages.error(request, f'Invalid username or password')
        else:
            messages.error(request, f'Invalid username or password')

    form = AuthenticationForm()
    return render(
        request=request,
        template_name='main/login.html',
        context={'form': form}
    )

def account(request):
    return render(
        request = request,
        template_name = 'main/account.html',
        context={'account': request.user}
    
    )
def edit_account(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account has been updated!')
            
        else:
            messages.error(request, f'Account was not updated!')
        return redirect('/account/')

    form = EditProfileForm(instance=request.user)
    return render(
        request=request,
        template_name='main/edit-account.html',
        context={'form': form, 'user': request.user}
    )

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Password has been changed!')
            
        else:
            messages.error(request, f'Password was not changed!')
        return redirect('/login/')

    form = PasswordChangeForm(user=request.user)
    return render(
        request=request,
        template_name='main/change-password.html',
        context={'form': form}
    )
    







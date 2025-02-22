from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import FavoritedProducts, Products, Users, Posts, Messages, ChatRooms, Likedposts, Followers
import json
from django.contrib.auth.models import User, auth
from django.http import JsonResponse
import requests
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages
from taggit.models import Tag  
from django.db.models import Q


def index(request):
    user_profile=None
    if request.user.is_authenticated:
        user_profile = Users.objects.get(username=request.user.username)
    posts = Posts.objects.all()
    
   
    if user_profile:
        return render(request, 'dashboard.html', {'posts':posts, 'user_profile': user_profile})
    else:
        return render(request, 'dashboard.html', {'posts':posts})
    

def apigrabber(request):
       # grabbing stuffs from API into database if they're not there already
    response = requests.get("https://fakestoreapi.com/products/category/men's clothing")
    data = response.json()
    for p in data:
        if not Products.objects.filter(productname=p['title'], price=p['price'], image=p['image'], category=p['category']):
            b = Products(productname=p['title'], price=p['price'], image=p['image'], category=p['category'])
            b.save()

    response = requests.get("https://fakestoreapi.com/products/category/women's clothing")
    data = response.json()
    for p in data:
        if not Products.objects.filter(productname=p['title'], price=p['price'], image=p['image'], category=p['category']):
            b = Products(productname=p['title'], price=p['price'], image=p['image'], category=p['category'])
            b.save()
    return render(request, 'index.html')

def get_favorite(request,userid):
    response=list(FavoritedProducts.objects.filter(userid=userid).values('productid'))
    return JsonResponse(response, content_type='application/json', safe=False)

def get_inbox(request,userid):
    room = ChatRooms.objects.filter(Q(userone=userid) | Q(usertwo=userid))
    data = []
    for i in room:
        message = Messages.objects.filter( (Q(fromuser=i.userone.userid) & Q(touser=i.usertwo.userid)) | (Q(fromuser=i.usertwo.userid) & Q(touser=i.userone.userid)) ).order_by('-created_at').values().first()
        item = {'id': i.chatroomid, 'userOneID':i.userone.userid, 'userTwoID':i.usertwo.userid,'userOneName':i.userone.username,'userTwoName':i.usertwo.username, 'lastMessageSent': message['content']}
        data.append(item)
    return JsonResponse(data, content_type='application/json', safe=False)


def change_favorite(request,userid, productid):
    count = FavoritedProducts.objects.filter(productid=productid,userid=userid).count()
    if (count > 0):
         FavoritedProducts.objects.filter(productid=productid,userid=userid).delete()
    else:
         user = Users.objects.get(userid=userid)
         product = Products.objects.get(productid=productid)
         FavoritedProducts.objects.create(productid=product,userid=user,date=datetime.datetime.now())

    return JsonResponse(productid, content_type='application/json', safe=False)


def marketplace(request):
 
    

    search_query = request.GET.get('search', '')
    if search_query:
        product_list = Products.objects.filter(productname__icontains=search_query)
    else:
        product_list = Products.objects.all()

    tag = request.GET.get('tag', '')
    if tag:
        product_list = product_list.filter(tags__name__in=[tag])

    all_tags = Tag.objects.all()  
    

    paginator = Paginator(product_list, 10)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    
    return render(request, 'marketplace.html', {'products':products})


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # Create User in Django built-in User model
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect('main:signup')  # No .html
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('main:signup')  # No .html
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()

                # Create the actual User profile that would be saved in our own database
                user_object = User.objects.get(username=username)
                new_user = Users.objects.create(
                    username=user_object.username, 
                    userid=user_object.id, 
                    password=user_object.password, 
                    email=user_object.email
                )
                new_user.save()

                
                user=auth.authenticate(username=username, password=password)
                auth.login(request, user)
                return redirect('main:settings')  # Optionally redirect to login instead of signup

        else:
            messages.info(request, 'Passwords do not match')
            return redirect('main:signup')  # No .html

    return render(request, 'signup.html') 

def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username, password=password) # check if a user with this info exists
        if user is not None:  #log in if exsits and return to home page
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid login")
            return redirect("main:signin")

    else:
        return render(request, "signin.html")
    
@login_required(login_url='main:signin')
def logout(request):
    auth.logout(request)
    return redirect("main:signin")

@login_required(login_url='main:signin')
def settings(request):
    user_profile = Users.objects.get(username=request.user.username)
    if request.method=="POST":
        email=request.POST["email"]
        biography=request.POST["biography"]
        image=request.FILES.get("image")

        user_profile.email = email 
        user_profile.biography=biography
        if image:
            user_profile.profileimg = image 
            
        user_profile.save()
        return redirect('main:index')
    return render(request, "settings.html", {"user_profile": user_profile})

@login_required(login_url='main:signin')
def upload(request):
    if request.method=="POST":
        user_profile = Users.objects.get(userid=request.user.id)
        image=request.FILES.get("uploadedImage")
        content=request.POST["content"]

        new_post=Posts.objects.create(userid=user_profile, image=image, content=content)
        new_post.save()
        return redirect('main:index')
        
    
    return render(request, "upload.html")

@login_required(login_url='main:signin')
def like_post(request):
    user_profile = Users.objects.get(userid=request.user.id)
    postid=request.GET.get("postid")

    post=Posts.objects.get(postid=postid)
    
    like_filter=Likedposts.objects.filter(postid=post, userid=user_profile ).first()
    if like_filter==None:
        new_like=Likedposts.objects.create(postid=post,userid=user_profile)
        new_like.save()
       
    else:
        like_filter.delete()
    return redirect('main:index')

def profile(request, userid):
    try:
        user_profile = Users.objects.get(userid=userid)
    except Users.DoesNotExist:  
        return redirect("/")  

    
    current_user = None
    if request.user.is_authenticated:  
        try:
            current_user = Users.objects.get(userid=request.user.id)
        except Users.DoesNotExist:
            current_user = None 
    user_posts = Posts.objects.filter(userid=userid)
    user_posts_length=len(user_posts)
    
    user_followers=len(Followers.objects.filter(touser=user_profile))
    user_following=len(Followers.objects.filter(fromuser=user_profile))
    if Followers.objects.filter(fromuser=current_user, touser=user_profile).first():
        button_text="Unfollow"
    else:
        button_text="Follow"
    info={
        "user_profile": user_profile,
        "user_posts":user_posts,
        "user_posts_length":user_posts_length, 
        "current_user":current_user,
        "button_text":button_text,
        "user_followers":user_followers,
        "user_following":user_following,
    }
    return render(request, "profile.html", info)

@login_required(login_url='main:signin')
def follow(request):
    if request.method=="POST":
        fromuser_id=request.POST['current_user']
        touser_id=request.POST['user_profile']
        try:
           
            fromuser = Users.objects.get(userid=fromuser_id)
            touser = Users.objects.get(userid=touser_id)
        except User.DoesNotExist:
            return redirect("/") 

        if Followers.objects.filter(fromuser=fromuser, touser=touser).first():
            delete_follower=Followers.objects.get(fromuser=fromuser, touser=touser)
            delete_follower.delete()
            return redirect('/profile/'+str(touser.userid))
        else:
            new_follower=Followers.objects.create(fromuser=fromuser, touser=touser)
            new_follower.save()
            return redirect('/profile/'+str(touser.userid))
    else:
        return redirect("/") 

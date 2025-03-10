from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import FavoritedProducts, Products, Users, Posts, Messages, ChatRooms, Likedposts, Followers,Notifications
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
import datetime
import time
from itertools import chain


def index(request):
    user_profile=None
    if request.user.is_authenticated:
        user_profile = Users.objects.get(username=request.user.username)
        notification = Notifications.objects.filter(userid=request.user.id)
        notification_count = Notifications.objects.filter(userid=request.user.id, status__isnull=True).count()
    
    
    user_following = Followers.objects.filter(fromuser=user_profile).values_list('touser', flat=True)
    feed_list_following = Posts.objects.filter(userid__in=user_following)
    other_posts = Posts.objects.exclude(userid__in=user_following).exclude(userid=user_profile)
    if user_profile:
        return render(request, 'dashboard.html', {'posts_following':feed_list_following, "other_posts":other_posts, 'user_profile': user_profile, 'notification':notification, 'notification_count':notification_count})
    else:
        feed_list=Posts.objects.all()
        return render(request, 'dashboard.html', {'posts':feed_list})
    

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

def get_user(request):
    if request.method == "POST":
        response=list(Users.objects.filter(Q(firstname__contains=request.POST['get-user-text']) | Q(lastname__contains=request.POST['get-user-text'])).exclude(userid=request.user.id).values())
    return JsonResponse(response, content_type='application/json', safe=False)

def create_chat(request):
    if request.method == "POST":
        if not ChatRooms.objects.filter( Q(userone_id=request.POST['fromuser'],usertwo_id=request.POST['touser']) | Q(userone_id=request.POST['touser'],usertwo_id=request.POST['fromuser'])):
            room = ChatRooms(userone_id=request.POST['fromuser'],usertwo_id=request.POST['touser'])
            room.save()
    return HttpResponse()

def read_notif(request):
    if request.method == "POST":
        user_profile = Users.objects.get(userid=request.user.id)
        if (user_profile):
            notification = Notifications.objects.filter(userid = request.user.id)
            notification.update(status='read')
    return HttpResponse()


# def get_inbox(request,userid):
#     room = ChatRooms.objects.filter(Q(userone=userid) | Q(usertwo=userid))
#     data = []
#     for i in room:
#         message = Messages.objects.filter( (Q(fromuser=i.userone.userid) & Q(touser=i.usertwo.userid)) | (Q(fromuser=i.usertwo.userid) & Q(touser=i.userone.userid)) ).order_by('-created_at').values().first()
#         item = {'id': i.chatroomid, 'userOneID':i.userone.userid, 'userTwoID':i.usertwo.userid,'userOneName':i.userone.username,'userTwoName':i.usertwo.username, 'lastMessageSent': message['content']}
#         data.append(item)
#     return JsonResponse(data, content_type='application/json', safe=False)


def change_favorite(request,userid, productid):
    count = FavoritedProducts.objects.filter(productid=productid,userid=userid).count()
    if (count > 0):
         FavoritedProducts.objects.filter(productid=productid,userid=userid).delete()
    else:
         user = Users.objects.get(userid=userid)
         product = Products.objects.get(productid=productid)
         FavoritedProducts.objects.create(productid=product,userid=user,date=datetime.datetime.now())

    return JsonResponse(productid, content_type='application/json', safe=False)

def message(request):
    if request.user.is_authenticated:
        user_profile = Users.objects.get(username=request.user.username)
        rooms = ChatRooms.objects.filter(Q(userone=request.user.id) | Q(usertwo=request.user.id))
        users = Users.objects.exclude(userid = user_profile.userid)
        notification = Notifications.objects.filter(userid=request.user.id)
        notification_count = Notifications.objects.filter(userid=request.user.id, status__isnull=True).count()

    if user_profile:
        return render(request, 'message.html', {'user_profile': user_profile, 'rooms' : rooms, 'users':users,  'notification':notification,  'notification_count':notification_count}) 
    return render(request, 'signin.html')

def get_message(request,userid):
    start_time = time.time()
    message = Messages.objects.filter( (Q(fromuser=userid) & Q(touser=request.user.id)) | (Q(fromuser=request.user.id) & Q(touser=userid)) ).order_by('created_at')
    data = []
    if message:
        for m in message:
            if (request.user.id==m.fromuser_id):
                tag = "send"
            else:
                tag = "receive"
            item = {'id':m.messageid, 'fromuser':m.fromuser_id, 'touser':m.touser_id,'content':m.content,'tag':tag, 'created_at':m.created_at,'chatroomid':m.chatroomid_id }
            data.append(item)
        print("Getting time: --- %s seconds ---" % (time.time() - start_time))
        return JsonResponse(data, content_type='application/json', safe=False)
    else:
        room = ChatRooms.objects.get( (Q(userone=userid) & Q(usertwo=request.user.id)) | (Q(userone=request.user.id) & Q(usertwo=userid)) )
        item = {'chatroomid':room.chatroomid }
        data.append(item)
        return JsonResponse(data, content_type='application/json', safe=False)


def send_message(request):
    if request.method == "POST":
        start_time = time.time()
        fromUser = Users.objects.get(userid=request.user.id)
        toUser = Users.objects.get(userid=request.POST['touser'])
        chatroom = ChatRooms.objects.get(chatroomid=request.POST['chatroomid'])
        message = Messages.objects.create(fromuser=fromUser,touser=toUser,content=request.POST['message'],created_at=datetime.datetime.now(),chatroomid=chatroom)
        message.save()
        print("Saving time: --- %s seconds ---" % (time.time() - start_time))
        return HttpResponse(str(toUser.userid))
    
    return HttpResponse()
   


def marketplace(request):
    search_query = request.GET.get('search', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    clothing_type = request.GET.get('type', '')
    size = request.GET.get('size', '')
    color = request.GET.get('color', '')
    category_filter = request.GET.get('category', '')
    tag = request.GET.get('tag', '')
    season = request.GET.get('season')

    product_list = Products.objects.all()

    if search_query:
        product_list = product_list.filter(productname__icontains=search_query)

    if min_price and max_price:
        product_list = product_list.filter(price__gte=min_price, price__lte=max_price)
    elif min_price:
        product_list = product_list.filter(price__gte=min_price)
    elif max_price:
        product_list = product_list.filter(price__lte=max_price)

    if clothing_type:
        product_list = product_list.filter(type__icontains=clothing_type)

    if size:
        product_list = product_list.filter(size__icontains=size)

    if color:
        product_list = product_list.filter(color__icontains=color)

    if tag:
        product_list = product_list.filter(tags__name__in=[tag])
        
    if category_filter:  
        product_list = product_list.filter(category=category_filter)
        
    if season:
        product_list = product_list.filter(tags__name=season)
    else:
        products = Products.objects.all()
        
    if category_filter:  
        product_list = product_list.filter(category=category_filter)
        
    if season:
        product_list = product_list.filter(tags__name=season)
    else:
        products = Products.objects.all()

    all_tags = Tag.objects.all()

    categories = Products.objects.values_list('category', flat=True).distinct()

    categories = Products.objects.values_list('category', flat=True).distinct()

    # Paginate results
    paginator = Paginator(product_list, 10)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    # Paginate results
    paginator = Paginator(product_list, 10)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    user_profile = None
    notification = None
    notification_count = 0
    if request.user.is_authenticated:
        user_profile = Users.objects.get(username=request.user.username)
        notification = Notifications.objects.filter(userid=request.user.id)
        notification_count = Notifications.objects.filter(userid=request.user.id, status__isnull=True).count()
    if user_profile:
        return render(request, 'marketplace.html', {
        'products': products,
        'all_tags': all_tags,
        'search_query': search_query,
        'min_price': min_price,
        'max_price': max_price,
        'clothing_type': clothing_type,
        'size': size,
        'color': color,
        'user_profile':user_profile,
        'notification':notification,
        'notification_count':notification_count
    })

    return render(request, 'marketplace.html', {
        'products': products,
        'all_tags': all_tags,
        'search_query': search_query,
        'min_price': min_price,
        'max_price': max_price,
        'clothing_type': clothing_type,
        'size': size,
        'color': color,
        'notification_count':0
    })



def signup(request):
    if request.method == "POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
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
                user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                user.save()

                # Create the actual User profile that would be saved in our own database
                user_object = User.objects.get(username=username)
                new_user = Users.objects.create(
                    firstname=user_object.first_name,
                    lastname=user_object.last_name,
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
        new_notif = Notifications.objects.create(content=new_like.userid.username + " liked your post.", userid = new_like.postid.userid, link = '')
        new_notif.save()
       
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
    user_posts_length=user_posts.count()
    
    user_followers=Followers.objects.filter(touser=user_profile).count()
    user_following=Followers.objects.filter(fromuser=user_profile).count()
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

        check_follower = Followers.objects.filter(fromuser=fromuser, touser=touser).first()
        if check_follower:
            check_follower.delete()
            return redirect('/profile/'+str(touser.userid))
        else:
            new_follower=Followers.objects.create(fromuser=fromuser, touser=touser)
            new_follower.save()
            new_notif = Notifications.objects.create(content=new_follower.fromuser.username + " followed you.", userid = new_follower.touser, link = '/profile/'+ str(new_follower.fromuser.userid))
            new_notif.save()

            return redirect('/profile/'+str(touser.userid))
    else:
        return redirect("/") 

def search(request):
    query=request.GET.get("search", "")

    if query:
        results=Users.objects.filter(
            Q(username__icontains=query)|
            Q(firstname__icontains=query)|
            Q(lastname__icontains=query)
        )
    else:
        results=[]
    return render(request, 'search.html', {'results': results})


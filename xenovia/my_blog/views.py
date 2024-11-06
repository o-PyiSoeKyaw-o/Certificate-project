from django.shortcuts import render,redirect
from my_blog.models import PostModel,CommentModel,Category
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
# Create Product View
@permission_required('my_blog.add_postmodel',login_url='login')
def createProduct(request):
    if request.method == "GET":
        category = Category.objects.all()
        return render(request, 'create_product.html',{"category":category})
    
    if request.method == "POST":
        products = PostModel.objects.create(
            image = request.FILES.get('image'),
            item = request.POST.get('item'),
            about = request.POST.get('about'),
            category_id = request.POST.get('category'),
            price = request.POST.get('price'),
            author_id = request.user.id,
            created_at = datetime.now(),
        )
        products.save()
        messages.success(request,"The product has been created successfully.")
        return redirect('/home/')

# Product List View with Pagination
@permission_required('my_blog.view_postmodel',login_url='login')
def productList(request):
    products = PostModel.objects.all().order_by('-created_at')
    paginator = Paginator(products,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'product_list.html',{"products":page_obj})

# Product Detail View
@permission_required('my_blog.view_postmodel',login_url='login')
def productDetail(request,product_id):
    products = PostModel.objects.get(id=product_id)
    user = User.objects.get(id=products.author_id)
    comments = CommentModel.objects.filter(product_id = product_id)    
    context = {"products": products, "author": user, "comments":comments}
    return render(request,'product_detail.html',context)

# Update Product View
@permission_required('my_blog.change_postmodel',login_url='login')
def productUpdate(request,product_id):
    if request.method == "GET":
        products = PostModel.objects.get(id=product_id)
        products.created_at = products.created_at.strftime('%Y-%m-%dT%H:%M')
        category = Category.objects.all()
        return render(request, 'product_update.html', {"products": products,"category":category})
    
    if request.method == "POST":
        products = PostModel.objects.get(id=product_id)
        products.item = request.POST.get('item')
        products.description = request.POST.get('description')
        products.price = request.POST.get('price')
        if request.FILES.get('image'):
            products.image = request.FILES.get('image')
    # products.created_at = request.POST.get('created')
        
        products.save()
        messages.success(request,"The product has been updated successfully.")
        return redirect('/home/')

# Delete Product View
@permission_required('my_blog.delete_postmodel',login_url='login')
def productDelete(request,product_id):
    products = PostModel.objects.filter(id=product_id)
    products.delete()
    messages.success(request,"The product has been deleted successfully.")
    return redirect('/home/')

# Login View
def loginView(request):
    if request.method == "GET":
        return render(request,'login_page.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            messages.success(request,"You're logged as "+username)
            return redirect('/home/')
        else:
            messages.error(request,"Invalid username or password.")
            return render(request,'login_page.html')

# Logout View
def logoutView(request):
    logout(request)
    return redirect('/home/login/')

# Create Comment View
def cmt_create(request, product_id):
        if request.method == "POST":
            comment = CommentModel.objects.create(
                content = request.POST.get('content'), 
                author_id = request.user.id, 
                product_id = product_id, 
                created_at = datetime.now(),
            )
            
        comment.save()
        messages.success(request, "The comment has been created successfully.")
        return redirect('/home/detail/' + str(product_id) +'/')

# Update Comment View
def cmt_update(request,cmt_id,product_id):
    if request.method == "GET":
        comment = CommentModel.objects.get(id=cmt_id)
        product = PostModel.objects.get(id=product_id)
        return render(request, "comment_update.html", {"comment":comment,"product":product})
    if request.method == "POST":
        comment = CommentModel.objects.get(id=cmt_id)
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('/home/detail/' + str(product_id) + '/')

# Delete Comment View
def cmt_delete(request,cmt_id,product_id):
    comment = CommentModel.objects.filter(id=cmt_id)
    comment.delete()
    return redirect('/home/detail/' + str(product_id) + '/')

# Search View
def search_by(request):
    search = request.GET.get('search')
    if search:
        products = PostModel.objects.filter(
            Q(item__icontains=search)|
            Q(about__icontains=search)
        )
        return render(request,'product_list.html',{'products':products})
    else:
        products = PostModel.objects.all().order_by('-created_at')
        return render(request,'product_list.html',{'products':products})
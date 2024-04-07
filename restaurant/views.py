from django.shortcuts import redirect, render, get_object_or_404
from restaurant.forms import CommentForm, ContactForm, RegistrationForm, ReservationForm, ReviewsForm
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from restaurant.models import About, AllSections, CartItem, ChooseUs, CommentBlog, CommentDish, DishesMenu, FunFactor, MenuCategory, Openhoure, PopularDishes, Testimonial, blogList, contact_Address, teamMembers

# Create your views here.


# Home page views here.
def home(request):
    contactAddresses = contact_Address.objects.all().order_by('-id')[:1]
    testMonial = Testimonial.objects.all()
    opEn = Openhoure.objects.all()
    allSections = AllSections.objects.all().order_by('-id')[:1]

    blogObj = blogList.objects.all().order_by('-id')[:3]

    popularDishes = PopularDishes.objects.all()
    MenucAT = MenuCategory.objects.all().order_by('id')[:6]
    dishesMenu = DishesMenu.objects.all()


    # Reservation Form Booking Statrt
    contactfo = ReservationForm()
    if request.method == 'POST':
        contactfo = ReservationForm(request.POST)
        if contactfo.is_valid():
            contactfo.save()
            print(messages.success(request, "Thanks ! We received your message and will respond shortly."))
            #return redirect('reservation')
        else:
            print(contactfo.errors)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():   # Send email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            reservation_date = form.cleaned_data['reservation_date']
            reservation_time = form.cleaned_data['reservation_time']
            body = form.cleaned_data['total_person']
            if contactfo.is_valid():
                contactfo.save()

                # Send an email
                email_subject = 'Reservation Booking Submission From Website'
                message = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nReservation_date: {reservation_date}\nReservation_time: {reservation_time}\nPerson:\n{body}'
                from_email = 'tahsinhossen58@gmail.com'  # Replace with your email
                recipient_list = ['tahsinhossen58@gmail.com']  # Replace with your recipient's email

                send_mail(email_subject, message, from_email, recipient_list, fail_silently=False)
                return redirect('reservation')
                
            else:
                print(messages.error(request, "Contact Messages Send Not Success."))

    else:
         form = ReservationForm()


    context = {
        'contactAddresses': contactAddresses,
        'testMonial': testMonial,
        'opEn': opEn,
        'allSections': allSections,
        'blogObj': blogObj,
        'popularDishes': popularDishes,
        'MenucAT': MenucAT,
        'dishesMenu': dishesMenu,
    }
    return render(request, 'base/home.html', context)


# About page views here.
def about(request):
    contactAddresses = contact_Address.objects.all().order_by('-id')[:1]
    testMonial = Testimonial.objects.all()
    opEn = Openhoure.objects.all()
    blogObj = blogList.objects.all()
    allSections = AllSections.objects.all().order_by('-id')[:1]

    aboutObj = About.objects.all().order_by('id')[:1].first()
    aboutObj2 = About.objects.all()
    funFactor = FunFactor.objects.all()[0:4]
    chooseUs = ChooseUs.objects.all().order_by('-id')[:1]
    teamMember = teamMembers.objects.all()[0:4]

    context = {
        'contactAddresses': contactAddresses,
        'testMonial': testMonial,
        'opEn': opEn,
        'aboutObj': aboutObj,
        'aboutObj2': aboutObj2,
        'teamMember': teamMember,
        'funFactor': funFactor,
        'chooseUs': chooseUs,
        'blogObj': blogObj,
        'allSections': allSections,
    }
    return render(request, 'base/about.html', context)

# Blog page views here.
def blog(request, pk):  # pk parameter is required
    contactAddresses = contact_Address.objects.all().order_by('-id')[:1]
    testMonial = Testimonial.objects.all()
    opEn = Openhoure.objects.all()
    allSections = AllSections.objects.all().order_by('-id')[:1]

   
    blogObj = blogList.objects.all().order_by('-id')

     # Search functionality
    query = request.GET.get('s')
    if query:
        blogObj = blogObj.filter(
            Q(blog_title__icontains=query) | 
            Q(date__icontains=query) | 
            Q(top_details__icontains=query)
            )
    
    # Check if a specific blog post is requested
    if pk:
        blog = get_object_or_404(blogList, id=pk)
    else:
        blog = None

    # Blog Comment Functionality
    comments = CommentBlog.objects.filter(blog_name=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_name = blog 
            comment.save()
            return redirect('blog', pk=pk) 
    else:
        form = CommentForm()

    context = {
        'contactAddresses': contactAddresses,
        'testMonial': testMonial,
        'opEn': opEn,
        'allSections': allSections,
        'blogObj': blogObj,
        'blog': blog,
        'comments': comments,
        'form': form,
    }
   
    return render(request, 'base/blog.html', context)

# Contact page views here.
def contact(request):
    contactAddresses = contact_Address.objects.all().order_by('-id')[:1]
    testMonial = Testimonial.objects.all()
    opEn = Openhoure.objects.all()
    blogObj = blogList.objects.all()
    allSections = AllSections.objects.all().order_by('-id')[:1]


    # Contact Form Booking Statrt
    contactfo = ContactForm()
    if request.method == 'POST':
        contactfo = ContactForm(request.POST)
        if contactfo.is_valid():
            contactfo.save()
            print(messages.success(request, "Thanks ! We received your message and will respond shortly."))
            #return redirect('contact')
        else:
            print(contactfo.errors)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():   # Send email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            body = form.cleaned_data['messages']
            if contactfo.is_valid():
                contactfo.save()

                # Send an email
                email_subject = 'Contact Submission From Website'
                message = f'Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{body}'
                from_email = 'tahsinhossen58@gmail.com'  # Replace with your email
                recipient_list = ['tahsinhossen58@gmail.com']  # Replace with your recipient's email

                send_mail(email_subject, message, from_email, recipient_list, fail_silently=False)
                return redirect('contact')
                
            else:
                print(messages.error(request, "Contact Messages Send Not Success."))

    else:
         form = ContactForm()


    context = {
        'contactAddresses': contactAddresses,
        'testMonial': testMonial,
        'contactfo': contactfo,
        'opEn': opEn,
        'blogObj': blogObj,
        'allSections': allSections,
    }
    return render(request, 'base/contact.html', context)

# Reservation page views here.
def reservation(request):
    contactAddresses = contact_Address.objects.all().order_by('-id')[:1]
    testMonial = Testimonial.objects.all()
    funFactor = FunFactor.objects.all()[0:4]
    opEn = Openhoure.objects.all()
    blogObj = blogList.objects.all()

    # Reservation Form Booking Statrt
    contactfo = ReservationForm()
    if request.method == 'POST':
        contactfo = ReservationForm(request.POST)
        if contactfo.is_valid():
            contactfo.save()
            print(messages.success(request, "Thanks ! We received your message and will respond shortly."))
            #return redirect('reservation')
        else:
            print(contactfo.errors)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():   # Send email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            reservation_date = form.cleaned_data['reservation_date']
            reservation_time = form.cleaned_data['reservation_time']
            body = form.cleaned_data['total_person']
            if contactfo.is_valid():
                contactfo.save()

                # Send an email
                email_subject = 'Reservation Booking Submission From Website'
                message = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nReservation_date: {reservation_date}\nReservation_time: {reservation_time}\nPerson:\n{body}'
                from_email = 'tahsinhossen58@gmail.com'  # Replace with your email
                recipient_list = ['tahsinhossen58@gmail.com']  # Replace with your recipient's email

                send_mail(email_subject, message, from_email, recipient_list, fail_silently=False)
                return redirect('reservation')
                
            else:
                print(messages.error(request, "Contact Messages Send Not Success."))

    else:
         form = ReservationForm()


    context = {
        'contactAddresses': contactAddresses,
        'testMonial': testMonial,
        'opEn': opEn,
        'blogObj': blogObj,
        'funFactor': funFactor,
    }
    return render(request, 'base/reservation.html', context)


# Contact page views here.
def dashboard(request):
    contactAddresses = contact_Address.objects.all().order_by('-id')[:1]
    testMonial = Testimonial.objects.all()
    opEn = Openhoure.objects.all()
    blogObj = blogList.objects.all()



    context = {
        'contactAddresses': contactAddresses,
        'testMonial': testMonial,
        'opEn': opEn,
        'blogObj': blogObj,
    }
   
    
    return render(request, 'base/dashboard.html', context)

# Menu page views here.
def menu(request):
    contactAddresses = contact_Address.objects.all().order_by('-id')[:1]
    testMonial = Testimonial.objects.all()
    funFactor = FunFactor.objects.all()[0:4]
    opEn = Openhoure.objects.all()
    allSections = AllSections.objects.all().order_by('-id')[:1]
    blogObj = blogList.objects.all()

    popularDishes = PopularDishes.objects.all()
    MenucAT = MenuCategory.objects.all().order_by('id')[:6]
    dishesMenu = DishesMenu.objects.all()

    # Reservation Form Booking Statrt
    contactfo = ReservationForm()
    if request.method == 'POST':
        contactfo = ReservationForm(request.POST)
        if contactfo.is_valid():
            contactfo.save()
            print(messages.success(request, "Thanks ! We received your message and will respond shortly."))
            #return redirect('reservation')
        else:
            print(contactfo.errors)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():   # Send email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            reservation_date = form.cleaned_data['reservation_date']
            reservation_time = form.cleaned_data['reservation_time']
            body = form.cleaned_data['total_person']
            if contactfo.is_valid():
                contactfo.save()

                # Send an email
                email_subject = 'Reservation Booking Submission From Website'
                message = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nReservation_date: {reservation_date}\nReservation_time: {reservation_time}\nPerson:\n{body}'
                from_email = 'tahsinhossen58@gmail.com'  # Replace with your email
                recipient_list = ['tahsinhossen58@gmail.com']  # Replace with your recipient's email

                send_mail(email_subject, message, from_email, recipient_list, fail_silently=False)
                return redirect('reservation')
                
            else:
                print(messages.error(request, "Contact Messages Send Not Success."))

    else:
         form = ReservationForm()


    context = {
        'contactAddresses': contactAddresses,
        'testMonial': testMonial,
        'opEn': opEn,
        'allSections': allSections,
        'funFactor': funFactor,
        'blogObj': blogObj,
        'popularDishes': popularDishes,
        'dishesMenu': dishesMenu,
        'MenucAT': MenucAT,
    }
    return render(request, 'base/menu.html', context)

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Shop page views here.
def shop(request):
    contactAddresses = contact_Address.objects.all().order_by('-id')[:1]
    testMonial = Testimonial.objects.all()
    opEn = Openhoure.objects.all()
    blogObj = blogList.objects.all()
    allSections = AllSections.objects.all().order_by('-id')[:1]
    MenucAT = MenuCategory.objects.all().order_by('id')
    popularDishes = PopularDishes.objects.all().order_by('-id')

     # Search functionality
    query = request.GET.get('s')
    if query:
        popularDishes = popularDishes.filter(
            Q(dish_name__icontains=query) | 
            Q(dish_price=query) | 
            Q(details__icontains=query)
            )
        

    paginator = Paginator(popularDishes, 3)  # 3 items per page
    page_number = request.GET.get('page')
    try:
        popular_dishes = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        popular_dishes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        popular_dishes = paginator.page(paginator.num_pages)


    context = {
        'contactAddresses': contactAddresses,
        'testMonial': testMonial,
        'opEn': opEn,
        'blogObj': blogObj,
        'popularDishes': popularDishes,
        'MenucAT': MenucAT,
        'allSections': allSections,
        'popular_dishes': popular_dishes,
    }
    return render(request, 'base/shop.html', context)

# Shop-details page views here.
def shopdetails(request , shop_id):
    contactAddresses = contact_Address.objects.all().order_by('-id')[:1]
    testMonial = Testimonial.objects.all()
    opEn = Openhoure.objects.all()
    allSections = AllSections.objects.all().order_by('-id')[:1]
   
    MenucAT = MenuCategory.objects.all().order_by('id')[:6]
    blogObj = blogList.objects.all().order_by('-id')[:6]

    popularDishes = PopularDishes.objects.all().order_by('-id')[:3]
    sHop = PopularDishes.objects.all()

     # Search functionality
    query = request.GET.get('s')
    if query:
        popularDishes = popularDishes.filter(
            Q(dish_name__icontains=query) | 
            Q(dish_price=query) | 
            Q(details__icontains=query)
            )


    # Shop-details singal funcationality
    if shop_id:
        shopDetails = get_object_or_404(PopularDishes, id=shop_id)
    else:
        shopDetails = None

    # Dish Reviews Functionality
    reViews = CommentDish.objects.filter(dish_name=shop_id)
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.dish_name = shopDetails
            comment.save()
            return redirect('shop-details', shop_id=shop_id) 
    else:
        form = ReviewsForm()

    #Related Dishes Views
    current_dish = get_object_or_404(PopularDishes, id=shop_id)
    related_dishes = PopularDishes.objects.filter(
        Q(category_name=current_dish.category_name) |  # Filter 
        Q(dish_name=current_dish.dish_name) |  
        Q(dish_price__icontains=current_dish.dish_price) |  
        Q(details__icontains=current_dish.details)      # Filter by similar details
    ).exclude(id=current_dish.id).order_by('-id')[:6]   

    context = {
        'contactAddresses': contactAddresses,
        'testMonial': testMonial,
        'opEn': opEn,
        'blogObj': blogObj,
        'allSections': allSections,
        'MenucAT': MenucAT,
        'popularDishes': popularDishes,
        'shopDetails': shopDetails,
        'sHop': sHop,
        'reViews': reViews,
        'form': form,
        'related_dishes': related_dishes,
    }
    return render(request, 'base/shop-details.html', context)


@login_required(login_url='/login-page')
# Shopping-cart page views here.
def shoppingcart(request, dish_id=None):
    contactAddresses = contact_Address.objects.all().order_by('-id')[:1]
    testMonial = Testimonial.objects.all()
    opEn = Openhoure.objects.all()
    blogObj = blogList.objects.all()
    cart_items = CartItem.objects.filter(username=request.user)
    

    for cart_item in cart_items:
        cart_item.item_total = cart_item.quantity * float(cart_item.dish.dish_price)

    subtotal = sum(cart_item.item_total for cart_item in cart_items)


    # Add and Remove views here.
    if request.method == 'POST':
        if 'remove_item' in request.POST:
            cart_item_id = request.POST.get('remove_item')
            cart_item = get_object_or_404(CartItem, id=cart_item_id)
            cart_item.delete()
            return redirect('shopping-cart')

        elif 'dish_id' in request.POST:
            dish_id = request.POST.get('dish_id')
            dish = get_object_or_404(PopularDishes, pk=dish_id)
            cart_item, created = CartItem.objects.get_or_create(dish=dish, username=request.user)
            if not created:
                cart_item.quantity += 1
                cart_item.save()
            return redirect('shopping-cart')


    context = {
        'contactAddresses': contactAddresses,
        'testMonial': testMonial,
        'opEn': opEn,
        'blogObj': blogObj,
        'cart_items': cart_items,
        'subtotal': subtotal,
    }
    return render(request, 'base/shopping-cart.html', context)

from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import auth
# Contact page views here.
def loginpage(request):
    contactAddresses = contact_Address.objects.all().order_by('-id')[:1]
    testMonial = Testimonial.objects.all()
    allSections = AllSections.objects.all().order_by('-id')[:1]
    opEn = Openhoure.objects.all()
    blogObj = blogList.objects.all()

    #page = 'loginpage'
    
    # if request.user.is_authenticated:
    #     #return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email', '').lower() 
        password = request.POST.get('password', '')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid login credentials. Please try again.'
            return render(request, 'base/login-page.html', {'error_message': error_message})

    

    
    context = {
        'contactAddresses': contactAddresses,
        'testMonial': testMonial,
        'opEn': opEn,
        'blogObj': blogObj,
        'allSections': allSections,
    }
    return render(request, 'base/login-page.html', context)


# LogoutUser views here.
def logoutUser(request):
    logout(request)
    return redirect('home')

# Register page views here.
def register(request):
    contactAddresses = contact_Address.objects.all().order_by('-id')[:1]
    testMonial = Testimonial.objects.all()
    allSections = AllSections.objects.all().order_by('-id')[:1]
    opEn = Openhoure.objects.all()
    blogObj = blogList.objects.all()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Use the renamed function
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('register')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = RegistrationForm()


    context = {
        'contactAddresses': contactAddresses,
        'testMonial': testMonial,
        'opEn': opEn,
        'blogObj': blogObj,
        'allSections': allSections,
    }
    return render(request, 'base/register.html', context)

# Search page views here.
def search(request):
    contactAddresses = contact_Address.objects.all().order_by('-id')[:1]
    testMonial = Testimonial.objects.all()
    opEn = Openhoure.objects.all()
    blogObj = blogList.objects.all()


    context = {
        'contactAddresses': contactAddresses,
        'testMonial': testMonial,
        'opEn': opEn,
        'blogObj': blogObj,
    }
    return render(request, 'base/search.html', context)


# Shopping-cart page views here.
def thankyou(request):
    contactAddresses = contact_Address.objects.all().order_by('-id')[:1]
    testMonial = Testimonial.objects.all()
    opEn = Openhoure.objects.all()
    blogObj = blogList.objects.all()


    context = {
        'contactAddresses': contactAddresses,
        'testMonial': testMonial,
        'opEn': opEn,
        'blogObj': blogObj,
    }
    return render(request, 'base/thank-you.html', context)

# 404 page views here.
def error404(request, exception):
    contactAddresses = contact_Address.objects.all().order_by('-id')[:1]
    testMonial = Testimonial.objects.all()
    opEn = Openhoure.objects.all()
    blogObj = blogList.objects.all()


    context = {
        'contactAddresses': contactAddresses,
        'testMonial': testMonial,
        'opEn': opEn,
        'blogObj': blogObj,
    }
    return render(request, 'base/404.html', context , status=404)


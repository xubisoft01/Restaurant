import time
from django.db import models
from django.utils import timezone

# Create your models here.

# User Registtions page models here.
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
        
class User(AbstractUser):
    username = models.CharField(max_length=150)
    user_phone_no = models.CharField(max_length=20,)
    email = models.EmailField(unique=True)
    picture = models.ImageField(null=True, default="avatar.svg")

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
    




# Contact Page models here...
class contact_Address(models.Model):
    primary_phone_no = models.CharField(null=True, max_length=20)
    phone_no = models.CharField(max_length=20, blank=True)
    primary_email = models.EmailField(null=True, max_length=62)
    email = models.EmailField(max_length=62, blank=True)
    address = models.TextField(null=True)
    top_title = models.CharField(max_length=255, null=True)
    header_logo = models.ImageField(null=True, default="avatar.svg")
    footer_logo = models.ImageField(null=True, default="avatar.svg")
    google_map = models.TextField(max_length=500, null=True)
    
    def __str__(self):
        return self.primary_phone_no
    
    class Meta:
        verbose_name_plural = "Contact Address & Logo"

class Contact_Us(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(null=True, max_length=15)
    messages = models.TextField(null=True)
    date_time = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Contact Us"

# Testmonial models here...
class Testimonial(models.Model):
    clint_name = models.CharField(null=True, max_length=30)
    messages = models.TextField(null=True)

    def __str__(self):
        return self.clint_name
    
    class Meta:
        verbose_name_plural = "Testimonial / Review"

# Open Houres models here...
class Openhoure(models.Model):
    day = models.CharField(null=True, max_length=30)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)

    def __str__(self):
        return self.day
    
    class Meta:
        verbose_name_plural = "Open Time Schedule"
        

# About Page models here...
class About(models.Model):
    title = models.CharField(null=True, max_length=30)
    detailes = models.CharField(null=True, max_length=250)
    full_detailes = models.TextField(null=True)
    slider_image = models.ImageField(null=True, default="avatar.svg")
   

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "About & sliders"

# About Page Fun-Factor models here...
class FunFactor(models.Model):
    title = models.CharField(null=True, max_length=30)
    values = models.CharField(null=True, max_length=15)
    icone = models.CharField(null=True,max_length=63)
   
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "About Fun-Factor"

# About Page Choose Us models here...
class ChooseUs(models.Model):
    chooseUs_title = models.TextField(null=True)
    choose_image = models.ImageField(null=True, default="avatar.svg")
    chef_title = models.CharField(null=True, max_length=255)
    total_tables = models.CharField(null=True, max_length=15)
    tables_detailes = models.CharField(null=True, max_length=255)
    clean_detailes = models.CharField(null=True, max_length=255)
    our_chefs_title = models.CharField(null=True, max_length=255)
   
    def __str__(self):
        return self.chooseUs_title
    
    class Meta:
        verbose_name_plural = "Choose Us"

# Team Members models start  here...
class teamMembers(models.Model):
    name = models.CharField(null=True, max_length=31)
    picture = models.ImageField(null=True, default="avatar.svg")
    sort_details= models.TextField(null=True,max_length=255)
    facebook_link = models.CharField(default='Write..', max_length=127)
    twitter_link = models.CharField(default='Write..', max_length=127)
    google_link = models.CharField(default='Write..', max_length=127)
    instagram_link = models.CharField(default='Write..', max_length=127)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Team Members List"


# Blog Page models here...
class blogList(models.Model):
    blog_title = models.CharField(null=True, max_length=127)
    blog_image = models.ImageField(null=True, default="avatar.svg")
    date = models.DateField(auto_now_add=True)
    home_image = models.ImageField(null=True, default="avatar.svg")
    main_image = models.ImageField(null=True, default="avatar.svg")
    top_details = models.TextField(null=True)
    details2 = models.TextField(null=True)
    banner_details = models.TextField(null=True)
    buttom_details = models.TextField(null=True)
   
    def __str__(self):
        return self.blog_title
    
    class Meta:
        verbose_name_plural = "Blog List"

class CommentBlog(models.Model):
    blog_name = models.ForeignKey(blogList, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Blog Comment" 

# Reservation
class Reservation(models.Model):
    name = models.CharField(max_length=63, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(null=True, max_length=15)
    reservation_date = models.DateField(null=True)
    reservation_time = models.TimeField(null=True)
    total_person = models.CharField(null=True, max_length=15)
    date_time = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Reservation Booking Clint"

# Menu Dishes Page models here...
class MenuCategory(models.Model):
    name = models.CharField(null=True, max_length=27)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "All Menu Category"

# Our Popular Dishes Page models here...
class PopularDishes(models.Model):
    category_name = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, null=True)
    dish_name = models.CharField(null=True, max_length=27)
    dish_title = models.CharField(null=True, max_length=27)
    dish_picture = models.ImageField(null=True, default="avatar.svg")
    dish_price = models.CharField(null=True, max_length=27)
    details = models.TextField(null=True)
    details_picture = models.ImageField(null=True, default="avatar.svg")
    description1 = models.TextField(null=True)
    description2 = models.TextField(null=True)
   
    def __str__(self):
        return self.dish_name
    
    class Meta:
        verbose_name_plural = "Our Popular Dishes"

# New model for Cart Items
class CartItem(models.Model):
    dish = models.ForeignKey(PopularDishes, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    #date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.dish.dish_name}"
    
    class Meta:
        verbose_name_plural = "Cart Item"

class CommentDish(models.Model):
    dish_name = models.ForeignKey(PopularDishes, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Dish Reviews" 

class DishesMenu(models.Model):
    category_name = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, null=True)
    dish_name = models.CharField(null=True, max_length=27)
    dish_title = models.CharField(null=True, max_length=27)
    dish_picture = models.ImageField(null=True, default="avatar.svg")
    dish_price = models.CharField(null=True, max_length=27)
    details = models.TextField(null=True)
   
    def __str__(self):
        return self.dish_name
    
    class Meta:
        verbose_name_plural = "All Menu List"




# All Sections Title models here...
class AllSections(models.Model):
    order_delivery_title = models.CharField(null=True, max_length=255)
    popular_dish_title = models.CharField(null=True, max_length=255)
    menu_title = models.CharField(null=True, max_length=255)
    booking_table_title = models.CharField(null=True, max_length=255)
    blog_title = models.CharField(null=True, max_length=255)
    newsletter = models.CharField(null=True, max_length=255)
    login_title = models.CharField(null=True, max_length=255)
    register_title = models.CharField(null=True, max_length=255)
    recent_food_title = models.CharField(null=True, max_length=255)
    
    def __str__(self):
        return self.order_delivery_title
    
    class Meta:
        verbose_name_plural = "All Page Sections Titles"

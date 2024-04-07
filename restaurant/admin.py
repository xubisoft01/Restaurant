from tokenize import Comment
from django.contrib import admin
from django.utils.html import format_html, mark_safe
from restaurant.models import About, AllSections, CartItem, ChooseUs, CommentBlog, CommentDish, Contact_Us, DishesMenu, FunFactor, MenuCategory, Openhoure, PopularDishes, Reservation, Testimonial, User, blogList, contact_Address, teamMembers

# Register your models here.

# Register your models here.
admin.site.site_header  =  "Restaurant"  
admin.site.site_title  =  "Restaurant"
admin.site.index_title  =  "Welcome to Restaurant Admin"


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'picture','password')

admin.site.register(User, UserAdmin)

# Contact page admin here.
class AddressAdmin(admin.ModelAdmin):
    list_filter = ('primary_phone_no',)
    search_fields = ('primary_phone_no',)
    list_display = ('primary_phone_no', 'primary_email', 'address', 'display_header_logo', 'display_footer_logo')

    def display_header_logo(self, obj):
        if obj.header_logo:
            return format_html('<img src="{}" width="100" />', obj.header_logo.url)
        else:
            return 'No Image'
    display_header_logo.short_description = 'Header Logo'

    def display_footer_logo(self, obj):
        if obj.footer_logo:
            return format_html('<img src="{}" width="100" />', obj.footer_logo.url)
        else:
            return 'No Image'
    display_footer_logo.short_description = 'Footer Logo'

admin.site.register(contact_Address, AddressAdmin)

# Contuct Us admin here.
class ContactAdminForms(admin.ModelAdmin):
    list_filter = ('name', 'email','date_time' )
    search_fields = ('name', 'email', 'messages')
    list_per_page = 10
    list_display = ('name', 'email', 'formatted_messages', 'phone', 'date_time', 'is_read_icon') 

    # Define a custom admin action to mark messages as read
    actions = ['mark_as_read']

    def formatted_messages(self, obj):
        if obj.is_read:
            return obj.messages
        else:
            formatted_message = format_html('<strong font-weight: bold; style="color: black;">{}</strong>', obj.messages)
            return mark_safe(formatted_message)
    formatted_messages.short_description = "Message"

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"

    def is_read_icon(self, obj):
        return format_html('<span style="color: {}; font-weight: bold; font-size: 15px;">{}</span>',
                        'green' if obj.is_read else 'red',
                        '✓' if obj.is_read else '✗')

    is_read_icon.short_description = "Is Read"
    is_read_icon.admin_order_field = 'is_read'
admin.site.register(Contact_Us, ContactAdminForms)

# Testimonial admin here.
class TestimonialAdmin(admin.ModelAdmin):
    list_filter = ('clint_name',)
    search_fields = ('clint_name',)
    list_display_links = ('clint_name',)
    list_display = ('id', 'clint_name', 'messages')

admin.site.register(Testimonial, TestimonialAdmin)

# Open Hourse admin here.
class openAdmin(admin.ModelAdmin):
    list_filter = ('day',)
    search_fields = ('day',)
    list_display_links = ('day',)
    list_display = ('id', 'day', 'start_time', 'end_time')

admin.site.register(Openhoure, openAdmin)

# About Page admin here.
class AboutAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    search_fields = ('title',)
    list_display_links = ('title',)
    list_display = ('id', 'title', 'detailes', 'full_detailes', 'display_slider_image')

    def display_slider_image(self, obj):
        if obj.slider_image:
            return format_html('<img src="{}" width="50" />', obj.slider_image.url)
        else:
            return 'No Image'
    display_slider_image.short_description = 'Slider Image'

admin.site.register(About, AboutAdmin)

# About Page FunFactor admin here.
class FunFactorAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    search_fields = ('title',)
    list_display_links = ('title',)
    list_display = ('id', 'title', 'values', 'icone')

admin.site.register(FunFactor, FunFactorAdmin)

# About Page Choose Us admin here.
class ChooseUsAdmin(admin.ModelAdmin):
    list_filter = ('chooseUs_title',)
    search_fields = ('chooseUs_title',)
    list_display_links = ('chooseUs_title',)
    list_display = ('chooseUs_title', 'display_choose_image', 'chef_title', 'total_tables', 'tables_detailes', 'our_chefs_title')

    def display_choose_image(self, obj):
        if obj.choose_image:
            return format_html('<img src="{}" width="150" height="100" />', obj.choose_image.url)
        else:
            return 'No Image'
    display_choose_image.short_description = 'Choose Image'

admin.site.register(ChooseUs, ChooseUsAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)
    list_display_links = ('name',)
    list_per_page = 10
    list_display = ('id', 'name', 'display_picture', 'sort_details')

    def display_picture(self, obj):
        if obj.picture:
            return format_html('<img src="{}" width="50" />', obj.picture.url)
        else:
            return 'No Image'
    display_picture.short_description = 'Picture'

admin.site.register(teamMembers, TeamAdmin)


# Blog Page admin here.
class blogAdmin(admin.ModelAdmin):
    list_filter = ('blog_title',)
    search_fields = ('blog_title',)
    list_per_page = 5
    list_display_links = ('blog_title',)
    list_display = ('id', 'blog_title', 'display_blog_image', 'date', 'top_details', 'display_home_image', 'display_main_image', 'banner_details')

    def display_blog_image(self, obj):
        if obj.blog_image:
            return format_html('<img src="{}" width="50" />', obj.blog_image.url)
        else:
            return 'No Image'
    display_blog_image.short_description = 'Blog Image'

    def display_home_image(self, obj):
        if obj.home_image:
            return format_html('<img src="{}" width="50" />', obj.home_image.url)
        else:
            return 'No Image'
    display_home_image.short_description = 'Home Image'

    def display_main_image(self, obj):
        if obj.main_image:
            return format_html('<img src="{}" width="50" />', obj.main_image.url)
        else:
            return 'No Image'
    display_main_image.short_description = 'Main Image'

admin.site.register(blogList, blogAdmin)

# Comments Blog Page admin here.
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)
    list_display_links = ('name',)
    list_display = ('id', 'blog_name', 'name', 'email','body','created','active')

admin.site.register(CommentBlog, CommentAdmin)

# Reservation admin here.
class ReservationAdminForms(admin.ModelAdmin):
    list_filter = ('name', 'email', 'date_time')
    search_fields = ('name', 'email', 'phone')
    list_per_page = 15
    list_display_links = ('name',)
    list_display = (
        'id',
        'name',
        'formatted_email',
        'formatted_phone',
        'reservation_date',
        'reservation_time',
        'total_person',
        'formatted_date_time',
        'is_read_icon'
    )

    def formatted_email(self, obj):
        return self.formatted_field(obj, 'email')
    formatted_email.short_description = 'Email'

    def formatted_phone(self, obj):
        return self.formatted_field(obj, 'phone')
    formatted_phone.short_description = 'Phone'

    def formatted_date_time(self, obj):
        return self.formatted_field(obj, 'date_time')
    formatted_date_time.short_description = 'Date Time'

    def formatted_field(self, obj, field_name):
        field_value = getattr(obj, field_name)
        if not obj.is_read:  # Apply formatting only if is_read is False
            return format_html('<strong style="color: black;">{}</strong>', field_value)
        return field_value  # Otherwise, return the field value as is

    def is_read_icon(self, obj):
        if obj.is_read:
            return format_html('<span style="color: green; font-weight: bold;">✓</span>')
        else:
            return format_html('<span style="color: red; font-weight: bold;">✗</span>')

    is_read_icon.short_description = 'Is Read'
    is_read_icon.admin_order_field = 'is_read'

admin.site.register(Reservation, ReservationAdminForms)


# Our Popular Dishes Page admin here.
class PopularAdmin(admin.ModelAdmin):
    list_filter = ('dish_name',)
    search_fields = ('dish_name',)
    list_display_links = ('dish_name',)
    list_per_page = 12
    list_display = ('id', 'dish_name', 'display_dish_picture', 'dish_price', 'details')

    def display_dish_picture(self, obj):
        if obj.dish_picture:
            return format_html('<img src="{}" width="50" />', obj.dish_picture.url)
        else:
            return 'No Image'
    display_dish_picture.short_description = 'Dish Picture'

admin.site.register(PopularDishes, PopularAdmin)


class CartAdmin(admin.ModelAdmin):
    list_filter = ('dish',)
    search_fields = ('dish',)
    list_display_links = ('dish',)
    list_per_page = 12
    list_display = ('id', 'username', 'dish', 'quantity')

admin.site.register(CartItem, CartAdmin)

# Dish Reviews Page admin here.
class RewiewsAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)
    list_display_links = ('name',)
    list_display = ('id', 'dish_name', 'name', 'email','body','created','active')

admin.site.register(CommentDish, RewiewsAdmin)

class MenucasAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)
    list_display_links = ('name',)
    list_per_page = 12
    list_display = ('id', 'name')

admin.site.register(MenuCategory, MenucasAdmin)

# Dish Mnue Page admin here.
class MenuAdmin(admin.ModelAdmin):
    list_filter = ('dish_name', 'category_name', 'dish_price')
    search_fields = ('dish_name',)
    list_display_links = ('dish_name',)
    list_per_page = 12
    list_display = ('id', 'category_name', 'dish_name', 'display_dish_picture', 'dish_price', 'details')

    def display_dish_picture(self, obj):
        if obj.dish_picture:
            return format_html('<img src="{}" width="50" />', obj.dish_picture.url)
        else:
            return 'No Image'
    display_dish_picture.short_description = 'Dish Picture'

admin.site.register(DishesMenu, MenuAdmin)

class TitleAdmin(admin.ModelAdmin):
    search_fields = ('order_delivery_title',)
    list_display_links = ('order_delivery_title',)
    list_display = ('order_delivery_title', 'popular_dish_title','menu_title','booking_table_title','blog_title','newsletter')

admin.site.register(AllSections, TitleAdmin)



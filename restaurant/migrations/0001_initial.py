# Generated by Django 4.2.6 on 2024-03-09 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=150)),
                ('user_phone_no', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('picture', models.ImageField(default='avatar.svg', null=True, upload_to='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='custom_user_groups', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_permissions', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, null=True)),
                ('detailes', models.CharField(max_length=250, null=True)),
                ('full_detailes', models.TextField(null=True)),
                ('slider_image', models.ImageField(default='avatar.svg', null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'About & sliders',
            },
        ),
        migrations.CreateModel(
            name='AllSections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_delivery_title', models.CharField(max_length=255, null=True)),
                ('popular_dish_title', models.CharField(max_length=255, null=True)),
                ('menu_title', models.CharField(max_length=255, null=True)),
                ('booking_table_title', models.CharField(max_length=255, null=True)),
                ('blog_title', models.CharField(max_length=255, null=True)),
                ('newsletter', models.CharField(max_length=255, null=True)),
                ('login_title', models.CharField(max_length=255, null=True)),
                ('register_title', models.CharField(max_length=255, null=True)),
                ('recent_food_title', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'All Page Sections Titles',
            },
        ),
        migrations.CreateModel(
            name='blogList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=127, null=True)),
                ('blog_image', models.ImageField(default='avatar.svg', null=True, upload_to='')),
                ('date', models.DateField(auto_now_add=True)),
                ('home_image', models.ImageField(default='avatar.svg', null=True, upload_to='')),
                ('main_image', models.ImageField(default='avatar.svg', null=True, upload_to='')),
                ('top_details', models.TextField(null=True)),
                ('details2', models.TextField(null=True)),
                ('banner_details', models.TextField(null=True)),
                ('buttom_details', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Blog List',
            },
        ),
        migrations.CreateModel(
            name='ChooseUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chooseUs_title', models.TextField(null=True)),
                ('choose_image', models.ImageField(default='avatar.svg', null=True, upload_to='')),
                ('chef_title', models.CharField(max_length=255, null=True)),
                ('total_tables', models.CharField(max_length=15, null=True)),
                ('tables_detailes', models.CharField(max_length=255, null=True)),
                ('clean_detailes', models.CharField(max_length=255, null=True)),
                ('our_chefs_title', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Choose Us',
            },
        ),
        migrations.CreateModel(
            name='contact_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_phone_no', models.CharField(max_length=20, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=20)),
                ('primary_email', models.EmailField(max_length=62, null=True)),
                ('email', models.EmailField(blank=True, max_length=62)),
                ('address', models.TextField(null=True)),
                ('top_title', models.CharField(max_length=255, null=True)),
                ('header_logo', models.ImageField(default='avatar.svg', null=True, upload_to='')),
                ('footer_logo', models.ImageField(default='avatar.svg', null=True, upload_to='')),
                ('google_map', models.TextField(max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Address & Logo',
            },
        ),
        migrations.CreateModel(
            name='Contact_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('messages', models.TextField(null=True)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_read', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='FunFactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, null=True)),
                ('values', models.CharField(max_length=15, null=True)),
                ('icone', models.CharField(max_length=63, null=True)),
            ],
            options={
                'verbose_name_plural': 'About Fun-Factor',
            },
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=27, null=True)),
            ],
            options={
                'verbose_name_plural': 'All Menu Category',
            },
        ),
        migrations.CreateModel(
            name='Openhoure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=30, null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Open Time Schedule',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('reservation_date', models.DateField(null=True)),
                ('reservation_time', models.TimeField(null=True)),
                ('total_person', models.CharField(max_length=15, null=True)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_read', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Reservation Booking Clint',
            },
        ),
        migrations.CreateModel(
            name='teamMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31, null=True)),
                ('picture', models.ImageField(default='avatar.svg', null=True, upload_to='')),
                ('sort_details', models.TextField(max_length=255, null=True)),
                ('facebook_link', models.CharField(default='Write..', max_length=127)),
                ('twitter_link', models.CharField(default='Write..', max_length=127)),
                ('google_link', models.CharField(default='Write..', max_length=127)),
                ('instagram_link', models.CharField(default='Write..', max_length=127)),
            ],
            options={
                'verbose_name_plural': 'Team Members List',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clint_name', models.CharField(max_length=30, null=True)),
                ('messages', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Testimonial / Review',
            },
        ),
        migrations.CreateModel(
            name='PopularDishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=27, null=True)),
                ('dish_title', models.CharField(max_length=27, null=True)),
                ('dish_picture', models.ImageField(default='avatar.svg', null=True, upload_to='')),
                ('dish_price', models.CharField(max_length=27, null=True)),
                ('details', models.TextField(null=True)),
                ('details_picture', models.ImageField(default='avatar.svg', null=True, upload_to='')),
                ('description1', models.TextField(null=True)),
                ('description2', models.TextField(null=True)),
                ('category_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.menucategory')),
            ],
            options={
                'verbose_name_plural': 'Our Popular Dishes',
            },
        ),
        migrations.CreateModel(
            name='DishesMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=27, null=True)),
                ('dish_title', models.CharField(max_length=27, null=True)),
                ('dish_picture', models.ImageField(default='avatar.svg', null=True, upload_to='')),
                ('dish_price', models.CharField(max_length=27, null=True)),
                ('details', models.TextField(null=True)),
                ('category_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.menucategory')),
            ],
            options={
                'verbose_name_plural': 'All Menu List',
            },
        ),
        migrations.CreateModel(
            name='CommentDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('dish_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.populardishes')),
            ],
            options={
                'verbose_name_plural': 'Dish Reviews',
            },
        ),
        migrations.CreateModel(
            name='CommentBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('blog_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.bloglist')),
            ],
            options={
                'verbose_name_plural': 'Blog Comment',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.populardishes')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cart Item',
            },
        ),
    ]

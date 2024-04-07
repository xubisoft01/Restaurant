from django.urls import path
from restaurant import views
#from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name="home"),

    path('about/', views.about, name="about"),
    path('blog/<int:pk>/', views.blog, name='blog'),
    path('contact/', views.contact, name="contact"),
    path('dashboard/', views.dashboard, name="dashboard"),
    
    path('menu/', views.menu, name="menu"),
    path('shop/', views.shop, name="shop"),
    path('shop-details/<int:shop_id>/', views.shopdetails, name="shop-details"),
    path('shopping-cart/', views.shoppingcart, name="shopping-cart"),

    path('search/', views.search, name="search"),
    path('reservation/', views.reservation, name="reservation"),
    path('login-page/', views.loginpage, name="login-page"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),

    path('thank-you/', views.thankyou, name="thank-you"),
    path('404/', views.error404, name="error404"),

    # path('reset_password/', auth_views.PasswordResetView.as_view(template_name="base/reset_password.html"), name="reset_password"),
    # path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    # #template_name="base/reset_password_complete.html"
    # path('change_password/', auth_views.PasswordChangeView.as_view(), name="change_password"),
    # path('change_password_done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
]

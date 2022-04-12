from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.GuitarList.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('guitars/', views.GuitarList.as_view(), name="guitar_list"),
    path('guitars/new/', views.Guitar_Create.as_view(), name="guitar_create"),
    path('guitars/<int:pk>/', views.GuitarDetail.as_view(), name="guitar_detail"),
    path('guitars/<int:pk>/update', views.GuitarUpdate.as_view(), name="guitar_update"),
    path('guitars/<int:pk>delete', views.GuitarDelete.as_view(), name="guitar_delete"),
    path('user/<username>/', views.profile, name='profile'),
    path('pickups/', views.pickups_index, name='pickups_index'),
    path('pickups/<int:pickup_id>', views.pickups_show, name='pickups_show'),
    path('pickups/create/', views.PickupCreate.as_view(), name='pickups_create'),
    path('pickups/<int:pk>/update/', views.PickupUpdate.as_view(), name='pickups_update'),
    path('pickups/<int:pk>/delete/', views.PickupDelete.as_view(), name='pickups_delete'),
    path('tuner/', views.Tuner.as_view(), name='tuner'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
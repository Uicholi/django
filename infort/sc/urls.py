from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('schematic/', SchematicView.as_view(), name='schematic'),
    path('schematic/<slug:result>/', schema, name='shema'),
    path('addschema/', addschema, name='addschema'),
    path('addvendor/', addvendor),
    path('addorder/', AddOrderView.as_view(), name='addorder'),
    path('service/', ServicesView.as_view(), name='service'),
    path('service/<slug:stage_slug>/', ServicesView.as_view(),name='services'),
    path('order/<int:pk>/', OrderView.as_view(), name='order'),
]


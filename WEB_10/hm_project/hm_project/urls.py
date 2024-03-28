
from django import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quotes.urls')),
    path('quotes/', include(('quotes.urls', 'quotes'), namespace='quotes')),
    path('note/', views.note, name='note'),
    #path('users/', include('users.urls'))
]

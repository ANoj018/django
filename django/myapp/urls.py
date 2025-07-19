
from django.contrib import admin
from django.urls import path, include
from ecommerce import urls as ecommerce_urls
from users import urls as users_urls

urlpatterns = [
    # Use a function that is actually defined
    path('admin/', admin.site.urls),
    path('api/v1/', include(users_urls)),  # Include the users app URLs
    path('ecommerce/', include(ecommerce_urls)), # Include the ecommerce app URLs
    path('api/v1/orders/', include('order.urls')),
    path('api/v1/products/', include('products.urls')),
]

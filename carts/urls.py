"""
URL configuration for carts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        "api/v1/",
        views.api_overview,
        name="api-urls"
    ),
    path(
        "api/v1/get_reviews/",
        views.get_product_reviews,
        name="get-reviews"
    ),
    path(
        "api/v1/get_review/<int:pk>/",
        views.get_product_review,
        name="get-review"
    ),
    path(
        "api/v1/create_review/",
        views.create_product_review,
        name="create-review"
    ),
    path(
        "api/v1/update_review/<int:pk>/",
        views.update_product_review,
        name="update-review"
    ),
    path(
        "api/v1/delete_review/<int:pk>/",
        views.delete_product_review,
        name="delete-view"
    ),
]

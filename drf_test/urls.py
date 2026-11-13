"""
URL configuration for drf_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

from famous_people import views as people_views
from library import views as library_views
from the_meal import views as the_meal

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/people/', people_views.FamousApiView.as_view()),
    # path('api/v1/people/<int:pk>/', people_views.FamousPeopleDetailAPIView.as_view()),


    path('api/v2/get/books', library_views.BookAPI.as_view()),
    path('api/v2/create/books', library_views.BookCreateAPI.as_view()),
    path('api/v2/books/<int:pk>', library_views.BookDetailAPI.as_view()), # filter by id
    path('api/v2/books/title/<str:title>', library_views.BooksAPIViewByName.as_view()),
    path('api/v2/books/author/<str:author>', library_views.BooksAPIViewByAuthor.as_view()),
    path('api/v2/books/category/<int:pk>', library_views.BooksAPIViewByCategory.as_view()),
    path('api/v2/books/<int:pk>/update', library_views.BookUpdateAPI.as_view()),
    path('api/v2/books/<int:pk>/delete', library_views.BookDeleteAPI.as_view()),


    path('api/v2/get/meals/', the_meal.MealAPI.as_view()),
    path('api/v2/get/meals/details', the_meal.MealDetailsAPI.as_view()),
    path('api/v2/get/meals/category', the_meal.CategoryAPI.as_view()),
    path('api/v2/get/meals/area', the_meal.AreaAPI.as_view())
]

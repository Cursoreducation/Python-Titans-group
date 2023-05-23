from django.urls import path
from .views import category_page


urlpatterns = [
    path("category/<slug>", category_page, name="category_page")
]

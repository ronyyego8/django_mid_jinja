from django.urls import path
from jinja_app import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("about_us/", views.about_us, name="about_us"),
    path("contact_us/", views.contact_us, name="contact_us"),
    path("gallery/", views.gallery, name="gallery"),
]

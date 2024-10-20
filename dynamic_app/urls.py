from django.urls import path
from .views import *
from service_page.views import *
from blog_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", indesx, name="index"),
    path("aboutus/", aboutUs, name="about"),
    # path("blog/", blog, name="blog"),
    # path("stamps/", stamps, name="stamp"),
    path("printingservice/", printingServices, name="printing"),
    path("itservice/", itServices, name="itservice"),
    path("photographyservice/", photographyServices, name="photographyservice"),
    path("contact/", contact, name="contacts"),
    path("search/", search, name="search"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

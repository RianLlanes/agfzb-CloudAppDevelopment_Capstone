from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import static_page
from .views import about
from .views import contact_us


app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path('static/', static_page, name='static_page'),
    # path for about view
    path('about/', about, name='about'),
    # path for contact us view
    path('contact_us/', contact_us, name='contact_us'),
    # path for registration

    # path for login

    # path for logout

    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

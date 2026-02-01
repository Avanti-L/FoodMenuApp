from django.urls import path
from . import views
# This is called namespacing: When there are more than one apps,
# If urlpatterns in different apps have the same name, conflict will occur.
# So to avoid it, we use namespacing as follows:
app_name = 'myapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('items/', views.item),
    # The name attribute is used for dynamic urls in html page
    path('<int:id>/', views.detail, name="detail"), 
]

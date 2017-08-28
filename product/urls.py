from django.conf.urls import url
from views import CategoryView, ProductView, ProductPostView

urlpatterns = [
    url(r'^product/new', ProductPostView.as_view()),
    url(r'^product/', ProductView.as_view()),
    url(r'^category/', CategoryView.as_view()),
]
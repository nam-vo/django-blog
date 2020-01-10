from django.urls import path
from blogging.views import list_view, detail_view

urlpatterns = [
    path('', list_view, name="post_index"),
    path('posts/<int:post_id>/', detail_view, name="post_detail"),
]
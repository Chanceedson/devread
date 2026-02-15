from django.urls import path
from . import views
from reviews import views as reviews_views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('reviews/', reviews_views.review_list, name='review_list'),
    path('review/<int:review_id>/edit/', reviews_views.edit_review, name='edit_review'),
    path('<slug:slug>/add-review/', reviews_views.add_review, name='add_review'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
]

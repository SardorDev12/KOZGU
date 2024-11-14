from django.urls import path
from ..posts.views import PostDeleteView, PostListView,PostCreateView, PostUpdateView, PostRetrieveView
from ..categories.views import CategoryListView,CategoryCreateView, CategoryDeleteView, CategoryUpdateView, CategoryRetrieveView
from ..likes.views import LikeListView, LikeCreateView, LikeUndoView, LikeRetrieveView
from ..comments.views import CommentRetrieveView, CommentListView, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='Posts'),
    path('posts/create/', PostCreateView.as_view(), name='Post Create'),
    path('posts/<int:pk>/', PostRetrieveView.as_view(), name='Post Retrieve'),
    path('posts/update/<int:pk>/', PostUpdateView.as_view(), name='Post Update'),
    path('posts/delete/<int:pk>/', PostDeleteView.as_view(), name='Post Delete'),

    path('categories/', CategoryListView.as_view(), name='Categories'),
    path('categories/create/', CategoryCreateView.as_view(), name='Categories Create'),
    path('categories/<int:pk>/', CategoryRetrieveView.as_view(), name='Categories Retrieve'),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='Categories Update'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='Categories Delete'),

    path('likes/', LikeListView.as_view(), name='Like Create'),
    path('likes/<int:pk>/', LikeRetrieveView.as_view(), name='Like Create'),
    path('likes/create/', LikeCreateView.as_view(), name='Like Create'),
    path('likes/delete/<int:pk>/', LikeUndoView.as_view(), name='Like Undo'),

    path('comments/', CommentListView.as_view(), name='Comment Create'),
    path('comments/<int:pk>/', CommentRetrieveView.as_view(), name='Comment Create'),
    path('comments/create/', CommentCreateView.as_view(), name='Comment Create'),
    path('comments/update/<int:pk>/', CommentUpdateView.as_view(), name='Comment Update'),
    path('comments/delete/<int:pk>/', CommentDeleteView.as_view(), name='Comment Delete'),
]



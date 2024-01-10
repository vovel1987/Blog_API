from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostList,PostDetail,UserDetail,UserList
from .views import PostViewSet,UserViewSet


# router = SimpleRouter()

# router.register('users',UserViewSet,basename= 'users')
# router.register('post',PostViewSet,basename = 'post')

# urlpatterns = router.urls


urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
    path('users/',UserList.as_view()),
    path('users/<int:pk>/',UserDetail.as_view()),
]



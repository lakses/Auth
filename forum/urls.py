from django.urls import path
from .views import forum_list, topic_list, topic_detail, create_forum

urlpatterns = [
    path('', forum_list, name='forum_list'),
    path('forum/<int:forum_id>/', topic_list, name='topic_list'),
    path('topic/<int:topic_id>/', topic_detail, name='topic_detail'),
    path('create_forum/', create_forum, name='create_forum'),  
]

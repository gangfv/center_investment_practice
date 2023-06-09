from django.urls import path

from practicum import views
from practicum.views import ArticleDetail, ArticleListView, QuizDetail

urlpatterns = [
    path("article", ArticleListView.as_view(), name="ArticleListView"),
    path("article/<int:pk>/", ArticleDetail.as_view(), name="ArticleDetail"),
    path("article/quiz/<int:pk>/", QuizDetail.as_view(), name="QuizDetail"),
]
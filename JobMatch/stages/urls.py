from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api import StageList, StageAuthentication
from .api import StageLocal, StageStat


urlpatterns = [
    path('', StageList.as_view()),
    path('local', StageLocal.as_view()),
    path('stat', StageStat.as_view()),
    path('auth/', StageAuthentication.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)

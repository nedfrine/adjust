from django.urls import path
from django.urls import re_path
from .views import CustomClickView


urlpatterns = [
    #path('metrics/', ListClickView.as_view(), name="metric-all"),
    #re_path(r'cpi', CPIClickView.as_view()),
    #re_path(r'date_filter', DateClickView.as_view()),
    re_path(r'custom', CustomClickView.as_view())
]

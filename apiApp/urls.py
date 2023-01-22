from django.conf.urls.static import static
from django.conf import settings

from django.urls import path

import apiApp.views as views


urlpatterns = [
    path('userSignUp',views.userSignUp,name='userSignUp'),
    path('userSignIn',views.userSignIn,name='userSignIn'),
    path('userProfile',views.userProfile,name='userProfile'),
    path('userCurriculum',views.userCurriculum,name='userCurriculum'),

] +static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
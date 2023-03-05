from django.conf.urls.static import static
from django.conf import settings

from django.urls import path

import apiApp.views as views
import apiApp.admin_pages.admin_views as ad_views


urlpatterns = [
    path('userSignUp',views.userSignUp,name='userSignUp'),
    path('userSignIn',views.userSignIn,name='userSignIn'),
    path('userProfile',views.userProfile,name='userProfile'),
    path('userCurriculum',views.userCurriculum,name='userCurriculum'),
    path('sideBar',views.sideBar,name='sideBar'),
    path('studentTestView',views.studentTestView,name='studentTestView'),
    path('studentReportView',views.studentReportView,name='studentReportView'),
    
    path('adminCreateBatch',ad_views.adminCreateBatch,name='adminCreateBatch'),
    path('adminBatchList',ad_views.adminBatchList,name='adminBatchList'),
    path('adminDeleteBatch',ad_views.adminDeleteBatch,name='adminDeleteBatch'),
    path('adminStudentList',ad_views.adminStudentList,name='adminStudentList'),
    path('adminUpdateBatch',ad_views.adminUpdateBatch,name='adminUpdateBatch'),
    # path('index',views.index,name='index'),
    

] +static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
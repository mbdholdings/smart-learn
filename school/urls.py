from . import views
from django.urls import path ,include


app_name='school'

urlpatterns = [
    path('', views.GradeListView.as_view(), name='grade_list'),
    path('<slug:slug>/', views.SubjectListView.as_view(), name='subject_list'),
    path('<str:grade>/<slug:slug>/', views.LessonListView.as_view(), name='lesson_list'),
    path('<str:grade>/<str:slug>/create/', views.LessonCreateView.as_view(), name='lesson_create'),
    path('<str:grade>/<str:subject>/<slug:slug>/', views.LessonDetailView.as_view(), name='lesson_detail'),
    path('<str:grade>/<str:subject>/<slug:slug>/update/', views.LessonUpdateView.as_view(), name='lesson_update'),
    path('<str:grade>/<str:subject>/<slug:slug>/delete/', views.LessonDeleteView.as_view(), name='lesson_delete'),
    
]
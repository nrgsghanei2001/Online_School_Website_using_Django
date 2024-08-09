from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path ('' , views.home.as_view() , name ="home"),
    path('login/',views.login.as_view(),name='login'),
    path('logout/',views.logout.as_view(),name='logout'),
    path('teachers/', views.teachers.as_view() ,name='teachers'),
    path ('teachers/exercise' , views.teachers_exercise, name ="teachers_exercise"),
    path('teachers/exercise/upload' , views.teachers_exercise_upload,name="teachers_exercise_upload"),
    path('teachers/exercise/answers/<int:answer_id>' , views.teachers_exercise_answers , name="teachers_exercise_answers"),
    path('teachers/videos/', views.teachers_videos,name='teachers_videos'),
    path('teachers/videos/upload' , views.teachers_videos_upload,name="teachers_videos_upload"),
    path ('teachers/videos/seen/<int:videoid>', views.teachers_videos_seen , name ="teachers_videos_seen"),
    path('students/', views.students.as_view(),name='students'),
    path('students/videos/', views.students_videos,name='students_videos'),
    path ('students/exercise' , views.students_exercise , name ="students_exercise"),
    path ('student/exercise/upload' , views.student_exercise_upload , name ="student_exercise_upload"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

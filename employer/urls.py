from django.urls import path
from employer import views
urlpatterns = [
   path('home',views.EmployerHomeView.as_view(),name="emp_home"),
   path("jobs/add",views.AddJobView.as_view(),name="emp-addjob"),
   path('jobs/all',views.ListJobView.as_view(),name="all-jobs"),
   path('jobs/details/<int:id>',views.JobDetailsView.as_view(),name='job-details'),
   path("jobs/change/<int:id>",views.JobEditView.as_view(),name='job-edit'),
   path("jobs/delete/<int:id>",views.JobDeleteView.as_view(),name="delete-job"),
   path("users/accounts/signup",views.SignUpView.as_view(),name="signup"),
   path("users/accounts/signin",views.SignInView.as_view(),name="signin"),
   path("users/accounts/signout",views.signout_view,name="signout"),
   path("users/password/change",views.ChangePasswordView.as_view(),name="password-change"),
   path("users/password/reset",views.PasswordResetView.as_view(),name="password-reset")

]
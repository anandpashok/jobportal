from django.urls import path

from candidate import views

urlpatterns=[
    path("home",views.CandidateHomeView.as_view(),name="cand-home"),
    path("profile/add",views.CandidateProfileView.as_view(),name="cand-addprofile"),
    path("profile/details",views.CandidateProfileDetailsView.as_view(),name="can-prodetail"),
    path("profile/change",views.CandidateProfileEditView.as_view(),name="can-profileedit"),
    path("job/all",views.CandidateJobListView.as_view(),name="can-joblist"),
    path("job/details/<int:id>",views.CandidateJobDetailView.as_view(),name="can-detailjob"),
    path("jobs/apply-now/<int:id>",views.apply_now,name="applynow"),
    path("applications/all",views.ApplicationListView.as_view(),name="can-applications"),
    path("application/cancell/<int:id>",views.cancell_application,name="can-cancellapplication")


]
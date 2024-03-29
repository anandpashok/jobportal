from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import TemplateView,CreateView,FormView,ListView,DetailView
from candidate.forms import CandidateProfileForm,CandidateProfileUpdateForm
from candidate.models import CandidateProfile
from django.urls import reverse_lazy
from employer.models import User,Jobs,Applications
from django.contrib import messages

class CandidateHomeView(TemplateView):
    template_name = "candidates/can-home.html"




class CandidateProfileView(CreateView):
    model = CandidateProfile
    form_class = CandidateProfileForm
    template_name = "candidates/can-profile.html"
    success_url = reverse_lazy("cand-home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"your profile has been added")
        return super().form_valid(form)

class CandidateProfileDetailsView(TemplateView):
    template_name = "candidates/canprofiledet.html"


class CandidateProfileEditView(FormView):
    template_name = "candidates/can-editprofile.html"
    form_class = CandidateProfileUpdateForm


    def get(self,request,*args,**kwargs):
        prodetails=CandidateProfile.objects.get(user=request.user)
        form=CandidateProfileUpdateForm(instance=prodetails,initial={"first_name":request.user.first_name,
                                                                     "last_name":request.user.last_name,
                                                                     "phn":request.user.phone})
        return render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        prodetails = CandidateProfile.objects.get(user=request.user)
        form=self.form_class(instance=prodetails,data=request.POST,files=request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data.pop("first_name")
            last_name=form.cleaned_data.pop("last_name")
            phone=form.cleaned_data.pop("phn")
            form.save()
            user=User.objects.get(id=request.user.id)
            user.first_name=first_name
            user.last_name=last_name
            user.phn=phone
            user.save()
            messages.success(request,"your profile has been updated")
            return redirect("cand-home")
        else:
            return render(request,self.template_name,{"form":form})

class CandidateJobListView(ListView):
        model=Jobs
        context_object_name = "Jobs"
        template_name = "candidates/can-joblist.html"


        def get_queryset(self):
            return self.model.objects.all().order_by("-created_date")



class CandidateJobDetailView(DetailView):
    model = Jobs
    context_object_name = "job"
    template_name = "candidates/jobdetail.html"
    pk_url_kwarg = "id"


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        try:
            is_applied=Applications.objects.filter(applicant=self.request.user,job=self.object)
            context["application"]=is_applied
            return context
        except:
            return context



def apply_now(request,*args,**kwargs):
    user=request.user
    job_id=kwargs.get("id")
    job=Jobs.objects.get(id=job_id)
    Applications.objects.create(applicant=user,
                                job=job
                                )
    messages.success(request,"your application has been posted successfully")
    return redirect("cand-home")



class ApplicationListView(ListView):
    model = Applications
    template_name = "candidates/can-applications.html"
    context_object_name = "applications"

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user).exclude(status="cancelled")



def cancell_application(request,*args,**kwargs):
    app_id=kwargs.get("id")
    application=Applications.objects.get(id=app_id)
    application.status="cancelled"
    application.save()
    messages.success(request,"your application cancelled")
    return redirect("cand-home")










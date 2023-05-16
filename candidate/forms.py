from django import forms
from candidate.models import CandidateProfile


class CandidateProfileForm(forms.ModelForm):


    class Meta:
        model=CandidateProfile
        exclude=("user",)


class CandidateProfileUpdateForm(forms.ModelForm):
    first_name=forms.CharField()
    last_name=forms.CharField()
    phn=forms.CharField()

    class Meta:
        model=CandidateProfile
        fields=[
            "first_name",
            "last_name",
            "phn",
            "profile_pic",
            "resume",
            "qualification",
            "skills",
            "experience"

        ]


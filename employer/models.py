from django.db import models

# Create your models here.


class Jobs(models.Model):
    job_title=models.CharField(max_length=150)
    company_name=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    salary=models.PositiveIntegerField(null=True)
    experience=models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.job_title


# python manage.py makemigrations
# python manage.py migrate


# Django ORM
#     orm query for creating an resource


# modelname.objects.create(field=value,field=value,.........)
# jobs.objects.create(job_title="front end developer",company_name="tcs",location="kakkanad",salary=25000,experience=4)

# all> mn.objects.all()
# specific object> mn.objects.get(spec ob name=value)
# list >qs=mn.objects.filtre(company_name="value")


# work -create employees app
# Employees(name,salary,dpt,exp)

# emp create
# fetch all employees
# filter



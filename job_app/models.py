from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone

#from accounts.models import User


class Category(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.title

class Jobs(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    count = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, null=True)
    location = models.CharField(max_length=150)
    company_name = models.CharField(max_length=100)
    company_description = models.TextField()
    category = models.ManyToManyField(Category, related_name="job_categoreis")
    last_date = models.DateTimeField()
    website = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    last_date = models.DateTimeField()
    filled = models.BooleanField(default=False)
    salary = models.IntegerField(default=0, blank=True)
    
    
def get_absolute_url(self):
    return reverse("single_jobs", kwargs={"pk": self.pk, "slug": self.slug})

# Create your models here.

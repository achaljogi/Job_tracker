from django.db import models
from django.contrib.auth.models import User


class JobApplication(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="job_applications",
        null=True,
        blank=True
    )
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    applied_date = models.DateField()
    interview_date = models.DateField(null=True, blank=True)
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company_name} - {self.job_title}"
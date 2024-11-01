from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    start_date = models.CharField(max_length=7)  # Format: YYYY-MM
    end_date = models.CharField(max_length=7, null=True, blank=True)  # Optional  # Optional if still employed
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
    
class Education(models.Model):
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    start_date = models.CharField(max_length=7)  # Format: YYYY-MM
    end_date = models.CharField(max_length=7, null=True, blank=True)  # Optional
    description = models.TextField()

    def __str__(self):
        return f"{self.degree} at {self.school}"
    
class Skill(models.Model):
    skill = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.skill}"
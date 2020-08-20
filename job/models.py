from django.db import models

# Create your models here.
job_choices = [
    ('part-time', 'part-time'),
    ('full-time', 'full-time'),
]


class Job(models.Model):

    title = models.CharField(max_length=100)

    # location
    discription = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(max_length=3, default=1)
    salary = models.IntegerField(default=0, max_length=10)
    experience = models.IntegerField(default=1, max_length=2)

    job_type = models.CharField(
        max_length=20,
        choices=job_choices,
        default='full-time',)

    def __str__(self):
        return self.title

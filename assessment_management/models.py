from django.db import models

# Create your models here.
from django.utils.text import slugify

from accounts.models import User

class Assessment(models.Model):

    ASSESSMENT_TYPES=(
        ("quiz","Quize"),
        ("exam","Exam"),
        ("assignment","Assignment"),
        ("mock_pratical_Test","Mock Practical Test"),

    )

    tutor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="assessments"

    )

    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True,blank=True,max_length=200)

    description = models.TextField(blank=True)

    assessment_type = models.CharField(
        max_length=200,
        choices=ASSESSMENT_TYPES,
        default="quiz"
    )

    total_marks = models.PositiveIntegerField()

    duration = models.PositiveIntegerField(
        help_text="Duration in hours"
    )

    start_time = models.DateTimeField()

    end_time = models.DateTimeField()

    is_published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def save(self,*args,**kwargs):

        if not self.slug:

            self.slug=slugify(self.title)

        super().save(*args,**kwargs)

    def __str__(self):
        return self.title

    class Meta:

          ordering = ["-created_at"]  



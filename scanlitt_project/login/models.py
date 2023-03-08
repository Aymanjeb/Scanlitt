from django.core.exceptions import ValidationError
from django.db import models

#define the model that will be used / Database that will be created
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    password_confirm = models.CharField(max_length=50)
    db_choices = models.CharField(max_length=200, choices=[
        ('scopus', 'Scopus'),
        ('pubmed', 'PubMed'),
        ('dimensions', 'Dimensions'),
        ('web_of_science', 'Web of Science'),
    ])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean (self, *args, **kwargs):
        if self.password != self.password_confirm:
            raise ValidationError("Password confirmation does not match password.")
        super().save(*args, **kwargs)



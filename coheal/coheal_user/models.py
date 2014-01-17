from django.db import models


from django.contrib.auth.models import User

class CohealUser(models.Model):
    user = models.OneToOneField(User)
    #picture = models.ImageField(null=True, blank=True, upload_to="picture/")

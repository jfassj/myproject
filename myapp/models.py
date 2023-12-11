from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    # Otros campos que desees almacenar

    def _str_(self):
        return self.username
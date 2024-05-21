from django.db import models


class User(models.Model):
    users_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=10)
    location = models.CharField(max_length=10)

    def __int__(self) -> int:
        return self.users_id

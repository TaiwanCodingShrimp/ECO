from django.db import models


class User(models.Model):
    users_id: int = models.AutoField(primary_key=True)
    title: str = models.CharField(max_length=50)
    email: str = models.CharField(max_length=50, null=False)
    phone: str = models.CharField(max_length=10)
    location: str = models.CharField(max_length=10)

    def __str__(self) -> str:
        return str(self.users_id)

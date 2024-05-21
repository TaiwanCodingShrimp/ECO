from django.db import models


class Waste(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=20, null=False)
    provider = models.CharField(max_length=10, null=False)
    date_put_in = models.DateTimeField(auto_now_add=True)
    label = models.DateTimeField(max_length=20, null=False)
    sent_to = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    def __int__(self) -> int:
        return self.id


class Leftover(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=20, null=False)
    provider = models.CharField(max_length=10, null=False)
    date_put_in = models.DateTimeField(auto_now_add=True)
    label = models.DateTimeField(max_length=20, null=False)
    portion = models.CharField(max_length=20, null=False)
    sent_to = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    def __int__(self) -> int:
        return self.id

from django.db import models

from Users.models.user_info import User


class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    contribution = models.CharField(max_length=10000)
    total_carbon_footprint = models.CharField(max_length=10000)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.report_id)

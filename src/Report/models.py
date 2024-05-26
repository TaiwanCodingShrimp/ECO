from django.db import models

from Users.models.user_info import User


class Report(models.Model):
    report_id: int = models.AutoField(primary_key=True)
    user_id: User = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    contribution: str = models.CharField(max_length=10000)
    total_carbon_footprint: str = models.CharField(max_length=10000)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.report_id)

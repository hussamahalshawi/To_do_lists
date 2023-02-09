from django.db import models
from datetime import datetime,timedelta
from django.urls import reverse
# Create your models here.
def expiry():
    return datetime.today() + timedelta(days=7)

class List(models.Model):
    title = models.CharField(max_length=100, unique=True)
    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=expiry)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )
    def __str__(self):
        return f"{self.title}: due {self.due_date}"
    class Meta:
        ordering = ["date"]

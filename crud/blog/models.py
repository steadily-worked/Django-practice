from django.db import models
from account.models import CustomUser


# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=10)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)

    # def __str__(self):
    #     return self.title
    def summary(self):
        return self.body[:100]
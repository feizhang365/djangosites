from django.db import models

# Create your models here.
class article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 50)
    content = models.CharField(max_length = 200)
    create_date = models.DateTimeField()
    create_user = models.BigIntegerField()
    update_date = models.DateTimeField()

    def __str__(self):
        return self.title


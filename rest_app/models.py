from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=700)
    time = models.DateField(default=datetime.now, editable=False,)
    # image = models.ImageField('Label', upload_to='/media/img')

    def __unicode__(self):
        return self.title



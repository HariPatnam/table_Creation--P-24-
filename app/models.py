from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self) :
        return self.topic_name

class Webpages(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    url=models.URLField()

    def __str__(self) :
        return self.Name

class AccessRecords(models.Model):
    name=models.ForeignKey(Webpages,on_delete=models.CASCADE)
    Author=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self):
        return self.Author

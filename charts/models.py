from django.db import models

# Create your models here.

class Passenger(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    survived = models.BooleanField()
    age = models.FloatField()
    ticket_class = models.PositiveSmallIntegerField()
    embarked = models.CharField(max_length=255)

    def __str__(self):
        #This line makes it so that when Article.object.all() is called,
        #It won't just  return <QuertySet [<Article: Article object (1)>]>
        #Now it will return the title
        return self.name
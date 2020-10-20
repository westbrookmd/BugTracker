from django.db import models

# Create your models here.
class Bugs(models.Model):
    #these are fields (bugs are tables)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.CharField(max_length=100)

#This defines how articles will look in admin section and in the shell
    def __str__(self):
        #This line makes it so that when Article.object.all() is called,
        #It won't just  return <QuertySet [<Article: Article object (1)>]>
        #Now it will return the title
        return self.title

    def snippet(self):
        return str(self.body)[:50] + "..."
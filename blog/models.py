from django.db import models
class Author(models.Model):
    name=models.CharField(max_length=67)
    email=models.EmailField()
    def __str__(self):
        return self.name
    

class Category(models.Model):
    category=models.CharField(max_length=45)
    def __str__(self):
        return self.category

class Article(models.Model):

    reporter=models.ForeignKey(Author,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=45)

    headline=models.TextField()
    image=models.ImageField(upload_to='images')
    content=models.TextField()
    date_pub=models.DateTimeField()
    def __str__(self):
        return self.title
    

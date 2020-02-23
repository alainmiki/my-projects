from django.db import models
# class Author(models.Model):
#     name=models.CharField(max_length=67)
#     email=models.EmailField()
#     def __str__(self):
#         return self.name
    

# class Category(models.Model):
#     category=models.CharField(max_length=45)
#     def __str__(self):
#         return self.category

class Article(models.Model):

    reporter=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    title=models.CharField(max_length=45)

    headline=models.TextField()
    image=models.FileField(upload_to='images')
    content=models.TextField()
    date_pub=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    

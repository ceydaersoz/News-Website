from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify




class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(unique=True, blank=True)
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)  
    
    def __str__(self):
        return self.name
              
              
    
    
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
class Haber(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='haber_resimleri')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)
    
    category = models.ManyToManyField(Category)
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)            
              
    def __str__(self):
        return self.title
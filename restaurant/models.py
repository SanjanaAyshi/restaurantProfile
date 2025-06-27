from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.slug
    
class Food(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    price=models.IntegerField()
    tags=models.ManyToManyField(Tag,blank=True)
    is_special=models.BooleanField(default=False)
    image = models.ImageField(upload_to="restaurant/images/")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

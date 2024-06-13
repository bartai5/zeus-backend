from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)

class Post(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    host_name = models.CharField(max_length=200)
    # host_id = models.IntegerField(null=True, blank=True)
    host_initials = models.CharField(max_length=3)
    property_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='created_at')
    property_type = models.CharField(max_length=200)
    property_price = models.DecimalField(max_digits=10, decimal_places=2)
    bedroom_no = models.CharField(max_length=200)
    bathroom_no = models.CharField(max_length=200)
    property_location = models.CharField(max_length=200)
    property_description = models.TextField()
    contact_info = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.property_title

class PostImages(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(_('Image'), upload_to=upload_to, default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.property_title
    
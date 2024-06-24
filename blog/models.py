from django.db import models
from PIL import Image
from django.core.exceptions import ValidationError

def validate_image_dimensions(image):
    min_width = 1000
    min_height = 500
    img = Image.open(image)
    width, height = img.size

    if width < min_width or height < min_height:
        raise ValidationError(
            f"Image dimensions must be at least {min_width}px wide and {min_height}px tall."
        )
    

class PageBase(models.Model):
  title = models.CharField(max_length=150)
  sub_title = models.CharField(max_length=250)
  bg_image = models.ImageField(upload_to='images/%Y/%m/%d', validators=[validate_image_dimensions])
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    abstract = True
    
  def __str__(self):
    return self.title
  
class HomePage(PageBase):
  pass

class AboutPage(PageBase):
  description = models.TextField()

class ContactPage(PageBase):
  description = models.TextField()
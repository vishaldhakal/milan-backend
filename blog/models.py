from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator

class Post(models.Model):
    title = models.CharField(max_length=100)
    content= RichTextField(config_name='awesome_ckeditor')
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to='posts/', validators=[FileExtensionValidator(['png','jpg','jpeg','webp'])],blank=True)
    author = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title[:20])

    class Meta:
        ordering = ('-created_at',)

    
    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.title)
            if Post.objects.filter(slug=self.slug).exists():
                self.slug = slugify(self.title) + "-" + str(self.id)
            self.save()

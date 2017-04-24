from django.db import models
from django.utils import timezone
from django.db import models

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    categories = models.CharField(max_length=200, null=True)
    text = models.TextField()
    docfile = models.ImageField(upload_to='images/blog/%Y/%m/%d')

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def save(self,*args,**kwargs):
        doc = self.docfile
        if not doc:
            raise Exception("Image has not been provided %s" % doc);
        super(Post,self).save(*args,**kwargs)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    @property
    def img_url(self):
        if self.docfile and hasattr(self.docfile,"url"):
            return self.docfile.url
        return None


            

               
        

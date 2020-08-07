from django.db import models

# Create your models here.
class Category(models.Model):
    objects = models.Manager()
    category_name = models.CharField(max_length=40 ,null=True)
    category_image = models.ImageField(upload_to = 'blog/images', null= True,blank = True)
    created_date = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self):
        return self.category_name
    
class Photo(models.Model):
    objects = models.Manager()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to = 'blog/images' ,null = True)
    text = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, null = True)


    def __str__(self):
        return self.title

# for contacting
class Contact(models.Model):
    status = (('Weddings','Weddings'),
            ('Events','Events'),
            ('Product Shoot','Product Shoot'),
            ('Food Photography','Food Photography'),
            ('Fashion Photography','Fashion Photography'),
            ('Others','Others')
            )
    objects = models.Manager()
    Full_Name = models.CharField(max_length=100, null = True)
    Email = models.EmailField(max_length=100, null = True)
    Contact_No = models.CharField(max_length=12 ,default='',null=True)
    purpose = models.CharField(max_length=120,choices = status,default='Events')
    requirements = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.Email
    


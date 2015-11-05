from django.db import models

class Collect(models.Model):
    first_name = models.CharField(max_length=20, blank=False, null=False, verbose_name="First Name")
    last_name = models.CharField(max_length=20, blank=False, null=False, verbose_name="Last Name")
    email = models.EmailField(max_length=75, blank=False, null=False, verbose_name="Email Field")
    mobile = models.CharField(max_length=10, blank=False, null=False, verbose_name="Mobile No")
    pro = models.BooleanField(default=False)
    pic = models.ImageField(null=True, blank=True, upload_to='user_images')
    contact = models.CharField(max_length=15, blank=False, null=False, verbose_name="Contact Number")
    def __unicode__(self):
            return self.user.username

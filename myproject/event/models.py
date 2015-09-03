from django.db import models
from photologue.models import Photo, Gallery
from django.contrib.postgres.fields import IntegerRangeField

class Venue(models.Model):

    master_contact =  models.CharField(
        verbose_name= "Contact No of Owner",
        max_length=15, blank=False, null=False)

    legal_id =  models.CharField(
        verbose_name = "Official and Legal stuff",
        max_length=25, blank=False, null=False)

    our_id =  models.CharField(
        verbose_name = "Our id",
        max_length=25, unique=True, blank=False, null=False)

    title =  models.CharField(
        verbose_name = "Title",
        max_length=40, blank=False, null=False)

    cover_image = models.ForeignKey(
        Photo,
        verbose_name= "Cover Photo",
        blank=True, null=True, editable=True)

    gallery = models.ForeignKey(
        Gallery,
        blank=True, null=True, editable=True)

    gallery_past = models.ForeignKey(
        Gallery,verbose_name= "Past events Gallery",
        blank=True, null=True, editable=True)

    long_position = models.DecimalField (max_digits=8, decimal_places=3)
    lat_position = models.DecimalField (max_digits=8, decimal_places=3)

    cost_per_person = models.IntegerField (null=False,blank=False)

    group_size = IntegerRangeField()

    duration = models.DurationField()

    fb_url = models.URLField()
    t_url = models.URLField()
    gplus_url = models.URLField()

    customer_care_email = models.EmailField()
    customer_care_contact = models.CharField(max_length=15,blank=False,null=False)

    address = models.CharField(max_length=60,blank=False,null=False)

    overview = models.CharField(max_length=150,blank=False,null=False)

    html_data = models.CharField(max_length=4000,blank=False,null=False)
    
    transportation_tips = models.CharField(max_length=150,blank=True,null=True)
    
    extra_string_param_1 = models.CharField(max_length=150,blank=True,null=True)
    extra_string_param_2 = models.CharField(max_length=150,blank=True,null=True)
    extra_string_param_3 = models.CharField(max_length=150,blank=True,null=True)

    extra_int_param_1 = models.IntegerField(null=True,blank=True)
    extra_int_param_2 = models.IntegerField(null=True,blank=True)
    
    reviews = ArrayField(models.CharField(max_length=150, blank=True), size=10)

def __str__(self):
        return self.title


from django.db import models

class Collect(models.Model):
    first_name = models.CharField(max_length=20, blank=False, null=False, verbose_name="First Name")
    last_name = models.CharField(max_length=20, blank=False, null=False, verbose_name="Last Name")
    email = models.EmailField(max_length=75, blank=False, null=False, verbose_name="Email Field")
    mobile = models.CharField(max_length=10, blank=False, null=False, verbose_name="Mobile No")
    HIGH_SCHOOL = 'HS'
    PRE_COLLEGE = 'PC'
    GRADUATE = 'UG'
    POST_GRADUATE = 'PG'
    YEAR_IN_SCHOOL_CHOICES = (
        (HIGH_SCHOOL, 'Class 10'),
        (PRE_COLLEGE, 'Class 12'),
        (GRADUATE, 'Graduate'),
        (POST_GRADUATE, 'Post Graduate'),
    )
    qualification = models.CharField(max_length=2,
                                    choices=YEAR_IN_SCHOOL_CHOICES,
                                    default=GRADUATE)
    NONE = 'NN'
    PART_TIME = 'PT'
    FULL_TIME = 'FT'
    STATUS_CHOICES = (
        (NONE, 'Not working'),
        (PART_TIME, 'Part Time'),
        (FULL_TIME, 'Full Time'),
    )
    work_status = models.CharField(max_length=2,
                                    choices=STATUS_CHOICES,
                                    default=NONE)
    NEVER = 'NV'
    PAST = 'PT'
    PRESENT = 'PR'
    EXPERIENCE_CHOICES = (
        (NEVER, 'None'),
        (PAST, 'Past'),
        (PRESENT, 'Present'),
    )
    experience = models.CharField(max_length=2,
                                    choices=EXPERIENCE_CHOICES,
                                    default=NONE)
    hours = models.SmallIntegerField(default=2, blank=False, null=False, verbose_name="Hours per week - you can contribute")
    NOT_COMFORTABLE = 'NC'
    OKAY = 'OK'
    VERY_GOOD = 'VG'
    PROFICIENCY_CHOICES = (
        (NOT_COMFORTABLE, 'Not Comfortable'),
        (OKAY, 'Okay'),
        (VERY_GOOD, 'Very Good'),
    )
    math = models.CharField(max_length=2,
                                    choices=PROFICIENCY_CHOICES,
                                    default=OKAY)
    english = models.CharField(max_length=2,
                                    choices=PROFICIENCY_CHOICES,
                                    default=OKAY)
    FINANCIAL = 'FN'
    FLEXIBILITY = 'FX'
    STRESS = 'SF'
    ENJOYMENT = 'EJ'
    HELPING = 'HS'
    PASSION_CHOICES = (
        (FINANCIAL, 'financial incentive'),
        (FLEXIBILITY, 'flexibility'),
        (STRESS, 'stress free'),
        (ENJOYMENT, 'enjoyment'),
        (HELPING, 'helping society'),
    )
    passion = models.CharField(max_length=2,
                                    choices=PASSION_CHOICES,
                                    default=FINANCIAL)
    age = models.SmallIntegerField(default=30, blank=False, null=False, verbose_name="Your age")
    married = models.BooleanField(default=False, blank=False, null=False, verbose_name="Are you married?")
    gender = models.BooleanField(default=True, blank=False, null=False, verbose_name="Are you female?")
    child_age = models.SmallIntegerField(default=0, blank=False, null=False, verbose_name="Age of your first child")
    def __unicode__(self):
        return self.first_name

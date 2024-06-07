from django.db import models

# Create your models here.

from .managers import planManager

CURRENCY = settings.CURRENCY


Primary_ComponentSelect_CHOICES = [
    ('Select', 'Select'),
    ('Manager/Agent', 'Manager/Agent'),
    ('Web Console', 'Web Console'),
    ('Cloud Console', 'Cloud Console'),
    ('Cloud/Agent', 'Cloud/Agent'),
    ('Appliance', 'Appliance'),
    ('Server Platform', 'Server Platform'),
    ]


class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    categoryname = models.CharField(
        max_length=200)

    categorynote = models.CharField(

        blank=True,
        null=True,
        max_length=500)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('title',)

    def __str__(self):
        return self.title

class SecurityTechnology(models.Model):
    title = models.CharField(max_length=150, unique=True)
    securitytechnologydesc = models.CharField(max_length=200)
    technologynote = models.CharField( blank=True, null=True, max_length=500)

    class Meta:
        verbose_name_plural = 'Technologies'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Plantype(models.Model):
    plantype_name = models.CharField(max_length=150, unique=True)
    plantype_desc = models.CharField(max_length=150, blank=True, null=True)
    vendorcategory = models.CharField(max_length=150, blank=True, null=True)
    numplans = models.CharField(max_length=150, default='0', blank=True, null=True)
 
    def __str__(self):
        return self.plantype_name

    class Meta:
        ordering = ('plantype_name',)


class Plan(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=150, unique=True)
    plantype = models.ForeignKey(Plantype, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10, blank=True, null=True)
    discount_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10, blank=True, null=True)
    final_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10, blank=True, null=True)
    qty = models.PositiveIntegerField(default=100000, blank=True, null=True)

    planname = models.CharField(max_length=75)

    plandesc = models.CharField(

        max_length=75,
        blank=True,
        null=True)

    plannote = RichTextUploadingField(blank=True, null=True)


    # plan Tasks and Check Box
    plan_task_desc_1 = models.CharField(blank=True, null=True, max_length=150)
    plan_task_image = models.ImageField(null=True, blank=True)
    plan_task_ck_bx_1 = models.BooleanField(default=False)
    plan_task_assigned_to_1 = models.CharField(blank=True, null=True, max_length=150)
    plan_task_assigned_to_date_1 = models.CharField(blank=True, null=True, max_length=150)
    plan_task_reassigned_1 = models.CharField(blank=True, null=True, max_length=150)

    # Create, Modify, Pause, and time Spent
    plan_task_created_1 = models.CharField(blank=True, null=True, max_length=150)
    plan_task_modified_1 = models.CharField(blank=True, null=True, max_length=150)
    plan_task_time_start_1 = models.CharField(blank=True, null=True, max_length=150)
    plan_task_time_pause_1 = models.CharField(blank=True, null=True, max_length=150)
    plan_task_time_spent_1 = models.CharField(blank=True, null=True, max_length=150)
    # Task assignment
    plan_task_reassigned_by_1 = models.CharField(blank=True, null=True, max_length=150)
    plan_task_reassigned_to_1 = models.CharField(blank=True, null=True, max_length=150)
    plan_task_reassigned_date_1 = models.CharField(blank=True, null=True, max_length=150)
    plan_task_reassigned_time_1 = models.CharField(blank=True, null=True, max_length=150)
    plan_task_reassigned_cost_1 = models.CharField(blank=True, null=True, max_length=150)
    plan_task_completed_ck_bx_1 = models.BooleanField(default=False)


    memoplannote = RichTextUploadingField(blank=True, null=True)
    memotechnicalnote = RichTextUploadingField(blank=True, null=True)
    planimage = models.ImageField(null=True, blank=True)


    objects = models.Manager()
    broswer = planManager()

    class Meta:
        verbose_name_plural = 'plans'
        ordering = ('title',)

    def save(self, *args, **kwargs):
        self.final_value = self.discount_value if self.discount_value > 0 else self.value
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def tag_final_value(self):
        return f'{self.final_value} {CURRENCY}'
    tag_final_value.short_description = 'Value'
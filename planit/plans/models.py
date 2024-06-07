from django.db import models

# Create your models here.

from .managers import ProductManager

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
    plantype = models.ForeignKey(lantyper, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10, blank=True, null=True)
    discount_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10, blank=True, null=True)
    final_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10, blank=True, null=True)
    qty = models.PositiveIntegerField(default=100000, blank=True, null=True)

    productname = models.CharField(max_length=75)

    productdesc = models.CharField(

        max_length=75,
        blank=True,
        null=True)
    producttype = models.CharField(

        max_length=75,
        blank=True,
        null=True)
    producttypefamily = models.CharField(

        max_length=75,
        blank=True,
        null=True)
    productnote = RichTextUploadingField(blank=True, null=True)

    productcomplexitybase = models.IntegerField(
        default='550')

    productcomplexityfac = models.FloatField(blank=True, null=True, default=1.0)

    numcomponent = models.IntegerField(default='0')
    # primarycomp = models.CharField(
    #
    #     max_length=75,
    #     blank=True,
    #     null=True)
    primarycomp = models.CharField(max_length=40, choices=Primary_ComponentSelect_CHOICES, blank=True, null=True, default='Select')

    primarycompdesc = models.CharField(

        max_length=75,
        blank=True,
        null=True)

    primarycomplexity = models.FloatField(
        default='0')

    totalcomplexity = models.FloatField(
        default='1')

    component1 = models.BooleanField(default=False)
    component1desc = models.CharField(

        max_length=75,
        blank=True,
        null=True)
    componentcomplexityhrs1 = models.FloatField(
        default='0.0')

    componentcomplexityfac1 = models.FloatField(

        default='0.0')
    ComponentHours1 = models.FloatField(default='0.0', blank=True, null=True)
    Component1_Wkstn = models.BooleanField(default=False)
    Component1_Svr = models.BooleanField(default=False)
    Component1_IP = models.BooleanField(default=False)
    Component1_Qty = models.FloatField(default=0.00, blank=True, null=True)

    memocomponent1note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent1technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component2 = models.BooleanField(default=False)
    component2desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs2 = models.FloatField(
        default='0.0')

    componentcomplexityfac2 = models.FloatField(

        default='0.0')
    ComponentHours2 = models.FloatField(default='0.0', blank=True, null=True)
    Component2_Wkstn = models.BooleanField(default=False)
    Component2_Svr = models.BooleanField(default=False)
    Component2_IP = models.BooleanField(default=False)
    Component2_Qty = models.FloatField(default='0.0', blank=True, null=True)
    memocomponent2note = models.CharField(
        max_length=150,
        blank=True,
        null=True)
    memocomponent2technote = models.CharField(
        max_length=150,
        blank=True,
        null=True)

    component3 = models.BooleanField(default=False)
    component3desc = models.CharField(
        db_column='Component3Desc',
        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs3 = models.FloatField(
        default='0.0')

    componentcomplexityfac3 = models.FloatField(

        default='0.0')
    ComponentHours3 = models.FloatField(default='0.0', blank=True, null=True)
    Component3_Wkstn = models.BooleanField(default=False)
    Component3_Svr = models.BooleanField(default=False)
    Component3_IP = models.BooleanField(default=False)
    Component3_Qty = models.FloatField(default='0.0', blank=True, null=True)
    memocomponent3note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent3technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component4 = models.BooleanField(default=False)
    component4desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs4 = models.FloatField(
        default='0.0')

    componentcomplexityfac4 = models.FloatField(

        default='0.0')

    ComponentHours4 = models.FloatField(default='0.0', blank=True, null=True)

    Component4_Wkstn = models.BooleanField(default=False)

    Component4_Svr = models.BooleanField(default=False)

    Component4_IP = models.BooleanField(default=False)

    Component4_Qty = models.FloatField(default='0.0', blank=True, null=True)

    memocomponent4note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent4technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component5 = models.BooleanField(default=False)
    component5desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    componentcomplexityhrs5 = models.FloatField(
        default='0.0')

    componentcomplexityfac5 = models.FloatField(

        default='0.0')

    ComponentHours5 = models.FloatField(default='0.0', blank=True, null=True)

    Component5_Wkstn = models.BooleanField(default=False)

    Component5_Svr = models.BooleanField(default=False)

    Component5_IP = models.BooleanField(default=False)

    Component5_Qty = models.FloatField(default='0.0', blank=True, null=True)

    memocomponent5note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent5technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component6 = models.BooleanField(default=False)
    component6desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs6 = models.FloatField(
        default='0.0')

    componentcomplexityfac6 = models.FloatField(

        default='0.0')

    ComponentHours6 = models.FloatField(default='0.0', blank=True, null=True)

    Component6_Wkstn = models.BooleanField(default=False)

    Component6_Svr = models.BooleanField(default=False)

    Component6_IP = models.BooleanField(default=False)

    Component6_Qty = models.FloatField(default='0.0', blank=True, null=True)

    memocomponent6note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent6technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component7 = models.BooleanField(default=False)
    component7desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs7 = models.FloatField(
        default='0.0')

    componentcomplexityfac7 = models.FloatField(

        default='0.0')

    ComponentHours7 = models.FloatField(default='0.0', blank=True, null=True)

    Component7_Wkstn = models.BooleanField(default=False)

    Component7_Svr = models.BooleanField(default=False)

    Component7_IP = models.BooleanField(default=False)

    Component7_Qty = models.FloatField(default='0.0', blank=True, null=True)

    memocomponent7note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent7technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    component8 = models.BooleanField(default=False)
    component8desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs8 = models.FloatField(
        default='0.0')

    componentcomplexityfac8 = models.FloatField(

        default='0.0')

    ComponentHours8 = models.FloatField(default='0.0', blank=True, null=True)

    Component8_Wkstn = models.BooleanField(default=False)

    Component8_Svr = models.BooleanField(default=False)

    Component8_IP = models.BooleanField(default=False)

    Component8_Qty = models.FloatField(default='0.0', blank=True, null=True)

    memocomponent8note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent8technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component9 = models.BooleanField(default=False)
    component9desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs9 = models.FloatField(
        default='0.0')

    componentcomplexityfac9 = models.FloatField(

        default='0.0')

    ComponentHours9 = models.FloatField(default='0.0', blank=True, null=True)

    Component9_Wkstn = models.BooleanField(default=False)

    Component9_Svr = models.BooleanField(default=False)

    Component9_IP = models.BooleanField(default=False)

    Component9_Qty = models.FloatField(default='0.0', blank=True, null=True)

    memocomponent9note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent9technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component10 = models.BooleanField(default=False)
    component10desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs10 = models.FloatField(
        default='0.0')

    componentcomplexityfac10 = models.FloatField(

        default='0.0')

    ComponentHours10 = models.FloatField(default='0.0', blank=True, null=True)

    Component10_Wkstn = models.BooleanField(default=False)

    Component10_Svr = models.BooleanField(default=False)

    Component10_IP = models.BooleanField(default=False)

    Component10_Qty = models.FloatField(default='0.0', blank=True, null=True)

    memocomponent10note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent10technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component11 = models.BooleanField(default=False)
    component11desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs11 = models.FloatField(
        default='0.0')

    componentcomplexityfac11 = models.FloatField(

        default='0.0')

    ComponentHours11 = models.FloatField(default='0.0', blank=True, null=True)

    Component11_Wkstn = models.BooleanField(default=False)

    Component11_Svr = models.BooleanField(default=False)

    Component11_IP = models.BooleanField(default=False)

    Component11_Qty = models.FloatField(default='0.0', blank=True, null=True)

    memocomponent11note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent11technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component12 = models.BooleanField(default=False)
    component12desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs12 = models.FloatField(
        default='0.0')

    componentcomplexityfac12 = models.FloatField(

        default='0.0')

    ComponentHours12 = models.FloatField(default='0.0', blank=True, null=True)

    Component12_Wkstn = models.BooleanField(default=False)

    Component12_Svr = models.BooleanField(default=False)

    Component12_IP = models.BooleanField(default=False)

    Component12_Qty = models.FloatField(default='0.0', blank=True, null=True)

    memocomponent12note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent12technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component13 = models.BooleanField(default=False)
    component13desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs13 = models.FloatField(
        default='0.0')
    componentcomplexityfac13 = models.FloatField(

        default='0.0')

    ComponentHours13 = models.FloatField(default='0.0', blank=True, null=True)

    Component13_Wkstn = models.BooleanField(default=False)

    Component13_Svr = models.BooleanField(default=False)

    Component13_IP = models.BooleanField(default=False)

    Component13_Qty = models.FloatField(default='0.0', blank=True, null=True)

    memocomponent13note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent13technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component14 = models.BooleanField(default=False)
    component14desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs14 = models.FloatField(
        default='0.0')

    componentcomplexityfac14 = models.FloatField(

        default='0.0')

    ComponentHours14 = models.FloatField(default='0.0', blank=True, null=True)

    Component14_Wkstn = models.BooleanField(default=False)

    Component14_Svr = models.BooleanField(default=False)

    Component14_IP = models.BooleanField(default=False)

    Component14_Qty = models.FloatField(default='0.0', blank=True, null=True)

    memocomponent14note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent14technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component15 = models.BooleanField(default=False)
    component15desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs15 = models.FloatField(
        default='0.0')
    componentcomplexityfac15 = models.FloatField(

        default='0.0')

    ComponentHours15 = models.FloatField(default='0.0', blank=True, null=True)

    Component15_Wkstn = models.BooleanField(default=False)

    Component15_Svr = models.BooleanField(default=False)

    Component15_IP = models.BooleanField(default=False)

    Component15_Qty = models.FloatField(default='0.0', blank=True, null=True)

    memocomponent15note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent15technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)


    component16 = models.BooleanField(default=False)
    component16desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs16 = models.FloatField(
        default='0.0')
    componentcomplexityfac16 = models.FloatField(

        default='0.0')

    ComponentHours16 = models.FloatField(default='0.0', blank=True, null=True)

    component16_Wkstn = models.BooleanField(default=False)

    component16_Svr = models.BooleanField(default=False)

    component16_IP = models.BooleanField(default=False)

    component16_Qty = models.FloatField(default='0.0', blank=True, null=True)

    memocomponent16note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent16technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)


    component17 = models.BooleanField(default=False)
    component17desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs17 = models.FloatField(
        default='0.0')
    componentcomplexityfac17 = models.FloatField(

        default='0.0')

    ComponentHours17 = models.FloatField(default='0.0', blank=True, null=True)

    component17_Wkstn = models.BooleanField(default=False)

    component17_Svr = models.BooleanField(default=False)

    component17_IP = models.BooleanField(default=False)

    component17_Qty = models.FloatField(default='0.0', blank=True, null=True)

    memocomponent17note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent17technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)


    component18 = models.BooleanField(default=False)
    component18desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs18 = models.FloatField(
        default='0.0')
    componentcomplexityfac18 = models.FloatField(

        default='0.0')

    ComponentHours18 = models.FloatField(default='0.0', blank=True, null=True)

    component18_Wkstn = models.BooleanField(default=False)

    component18_Svr = models.BooleanField(default=False)

    component18_IP = models.BooleanField(default=False)

    component18_Qty = models.FloatField(default='0.0', blank=True, null=True)

    memocomponent18note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent18technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component19 = models.BooleanField(default=False)
    component19desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs19 = models.FloatField(
        default='0.0')
    componentcomplexityfac19 = models.FloatField(

        default='0.0')

    ComponentHours19 = models.FloatField(default='0.0', blank=True, null=True)

    component19_Wkstn = models.BooleanField(default=False)

    component19_Svr = models.BooleanField(default=False)

    component19_IP = models.BooleanField(default=False)

    component19_Qty = models.FloatField(default='0.0', blank=True, null=True)

    memocomponent19note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent19technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)

    component20 = models.BooleanField(default=False)
    component20desc = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    componentcomplexityhrs20 = models.FloatField(
        default='0.0')
    componentcomplexityfac20 = models.FloatField(

        default='0.0')

    ComponentHours20 = models.FloatField(default='0.0', blank=True, null=True)

    component20_Wkstn = models.BooleanField(default=False)

    component20_Svr = models.BooleanField(default=False)

    component20_IP = models.BooleanField(default=False)

    component20_Qty = models.FloatField(default='0.0', blank=True, null=True)

    memocomponent20note = models.CharField(

        max_length=150,
        blank=True,
        null=True)
    memocomponent20technote = models.CharField(

        max_length=150,
        blank=True,
        null=True)


    # Product Question and Check Box
    prod_quest_desc_1 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_1 = models.BooleanField(default=False)
    prod_long_quest_answer_1 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_1 = models.BooleanField(default=False)

    prod_quest_desc_2 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_2 = models.BooleanField(default=False)
    prod_long_quest_answer_2 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_2 = models.BooleanField(default=False)

    prod_quest_desc_3 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_3 = models.BooleanField(default=False)
    prod_long_quest_answer_3 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_3 = models.BooleanField(default=False)

    prod_quest_desc_4 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_4 = models.BooleanField(default=False)
    prod_long_quest_answer_4 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_4 = models.BooleanField(default=False)

    prod_quest_desc_5 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_5 = models.BooleanField(default=False)
    prod_long_quest_answer_5 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_5 = models.BooleanField(default=False)

    prod_quest_desc_6 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_6 = models.BooleanField(default=False)
    prod_long_quest_answer_6 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_6 = models.BooleanField(default=False)

    prod_quest_desc_7 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_7 = models.BooleanField(default=False)
    prod_long_quest_answer_7 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_7 = models.BooleanField(default=False)

    prod_quest_desc_8 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_8 = models.BooleanField(default=False)
    prod_long_quest_answer_8 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_8 = models.BooleanField(default=False)

    prod_quest_desc_9 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_9 = models.BooleanField(default=False)
    prod_long_quest_answer_9 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_9 = models.BooleanField(default=False)

    prod_quest_desc_10 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_10 = models.BooleanField(default=False)
    prod_long_quest_answer_10 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_10 = models.BooleanField(default=False)

    prod_quest_desc_11 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_11 = models.BooleanField(default=False)
    prod_long_quest_answer_11 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_11 = models.BooleanField(default=False)

    prod_quest_desc_12 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_12 = models.BooleanField(default=False)
    prod_long_quest_answer_12 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_12 = models.BooleanField(default=False)

    prod_quest_desc_13 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_13 = models.BooleanField(default=False)
    prod_long_quest_answer_13 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_13 = models.BooleanField(default=False)

    prod_quest_desc_14 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_14 = models.BooleanField(default=False)
    prod_long_quest_answer_14 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_14 = models.BooleanField(default=False)

    prod_quest_desc_15 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_15 = models.BooleanField(default=False)
    prod_long_quest_answer_15 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_15 = models.BooleanField(default=False)

    prod_quest_desc_16 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_16 = models.BooleanField(default=False)
    prod_long_quest_answer_16 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_16 = models.BooleanField(default=False)

    prod_quest_desc_17 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_17 = models.BooleanField(default=False)
    prod_long_quest_answer_17 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_17 = models.BooleanField(default=False)

    prod_quest_desc_18 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_18 = models.BooleanField(default=False)
    prod_long_quest_answer_18 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_18 = models.BooleanField(default=False)

    prod_quest_desc_19 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_19 = models.BooleanField(default=False)
    prod_long_quest_answer_19 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_19 = models.BooleanField(default=False)

    prod_quest_desc_20 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_ck_bx_20 = models.BooleanField(default=False)
    prod_long_quest_answer_20 = models.CharField(blank=True, null=True, max_length=150)
    prod_quest_numeric_ck_bx_20 = models.BooleanField(default=False)


    componentcomplexityhrstotal = models.FloatField(
        default='0.0', blank=True, null=True)

    # numcomponents = models.IntegerField(default=False)

    memoproductnote = RichTextUploadingField(blank=True, null=True)
    memotechnicalnote = RichTextUploadingField(blank=True, null=True)
    endpoint_ip = models.BooleanField(default=False, null=True, blank=True)
    prodimage =     models.ImageField(null=True, blank=True)
    addlconsole = models.PositiveIntegerField(default=0, null=True, blank=True)

    objects = models.Manager()
    broswer = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('title',)

    def save(self, *args, **kwargs):
        self.final_value = self.discount_value if self.discount_value > 0 else self.value
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def tag_final_value(self):
        return f'{self.final_value} {CURRENCY}'
    tag_final_value.short_description = 'Value'